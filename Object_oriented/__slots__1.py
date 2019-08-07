#coding=utf-8
'''
https://www.liaoxuefeng.com/wiki/1016959663602400/1017501655757856
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
https://zhuanlan.zhihu.com/p/25930288
'''
from __future__ import print_function
class MyClass(object):
  __slots__ = ['name', 'identifier']
  # def __init__(self, name, identifier):
  #     self.name = name
  #     self.identifier = identifier
  pass
  

s=MyClass()
s.name='huangchuang'
s.identifier='hhhh'
      

import resource


class A(object):
    def __init__(self):
        self.a = 'string'
        self.b = 10
        self.c = True


class B(object):
    __slots__ = ['a', 'b', 'c']
    def __init__(self):
        self.a = 'string'
        self.b = 10
        self.c = True


def test(cls):
    mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    l = []
    for i in range(500000):
        l.append(cls())
    mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    del l
    print('Class: {}:\n'.format(getattr(cls, '__name__')))
    print('Initial RAM usage: {:14,}'.format(mem_init))
    print('  Final RAM usage: {:14,}'.format(mem_final))
    print('-' * 20)


# if __name__ == '__main__':
#     import sys
#     test(globals()[sys.argv[1].upper()])

a=dict()
import inspect
print(inspect.getmembers(a).keys())


