# -*- coding:gbk -*-
'''示例1: 最简单的函数,表示调用了两次'''


'''
为什么使用内嵌保障函数就能够确保每次新函数被调用？

'''
# def deco(func):
#     def _deco():
#
#         print("before myfunc called")
#         func()
#         print("after myfunc( called")
#     return _deco

def deco(func):
    print("before myfunc called")
    func()
    print("after myfunc( called")
    return func

@deco
def myfunc():
    print("myfunc() called.")





myfunc()
myfunc()