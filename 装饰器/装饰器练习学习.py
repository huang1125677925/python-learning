# -*- coding:gbk -*-
'''ʾ��1: ��򵥵ĺ���,��ʾ����������'''


'''
Ϊʲôʹ����Ƕ���Ϻ������ܹ�ȷ��ÿ���º��������ã�

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