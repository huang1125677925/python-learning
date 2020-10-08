def write_to_file():
    with open('test.txt','wt') as f:
        for i in range(100):
            print(i,file=f)
            


def read_from_file():
    with open('test.txt','rt') as f:
        for line in f:
            print(line,sep=',')


if __name__ == '__main__':
    read_from_file()

