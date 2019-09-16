#__str__定义在类内部，必须返回一个字符串类型，
#什么时候会出发它的执行呢？打印由这个类产生的对象时，会触发执行
class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '<name:%s,age:%s>' %(self.name,self.age)

p1=People('egon',18)
print(p1)
# str(p1) #----->p1.__str__()