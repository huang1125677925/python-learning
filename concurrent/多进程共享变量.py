import multiprocessing


def func(mydict, mylist):
	mydict["index1"] = "aaaaaa"  # 子进程改变dict,主进程跟着改变
	mydict["index2"] = "bbbbbb"
	mylist.append(11)  # 子进程改变List,主进程跟着改变
	mylist.append(22)
	mylist.append(33)

def func1(mydict, mylist):
	mydict["index"] = "aaaaaa"  # 子进程改变dict,主进程跟着改变
	mydict["index4"] = "bbbbbb"
	mylist.append(111)  # 子进程改变List,主进程跟着改变
	mylist.append(212)
	mylist.append(313)


if __name__ == "__main__":
	with multiprocessing.Manager() as MG:  # 重命名
		mydict = multiprocessing.Manager().dict()  # 主进程与子进程共享这个字典
		mylist = multiprocessing.Manager().list(range(5))  # 主进程与子进程共享这个List

		p = multiprocessing.Process(target=func, args=(mydict, mylist))
		q= multiprocessing.Process(target=func1, args=(mydict, mylist))

		p.start()
		q.start()

		p.join()
		q.join()

		print(mylist)
		print(mydict)

