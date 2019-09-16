# a、全局变量：在模块内、在所有函数外面、在class外面，这就是全局变量。
#
# b、局部变量：在函数内、在class的方法（构造、类方法、静态方法、实例方法）内（变量未加self修饰），这就是局部变量
#
#             c、 类变量：在class内的，但不在class的方法内的，这就是静态变量
#
#             d、 实例变量：在class的方法内的，用self修饰的变量，这就是实例变量

class test(object):
    # a为类变量
    a = 10
    
    @staticmethod
    def test(self):
        test.a += -1


x = test()
y = test()
x.test(x)  # 对类变量操作
print(x.a)  # 输出9
y.test(y)  # 对类变量操作
print(x.a)  # 输出8
print(y.a)  # 输出8

x.a = 5  # 一旦被赋值就会退出作用域，重新划出内存区域变成成员变量或者叫做对象变量，这样设计不会影响到其他对象
print(x.a)  # 输出5

x.test(x)  # 对类变量操作
print(x.a)  # 输出仍然为5
print(y.a)  # 输出7