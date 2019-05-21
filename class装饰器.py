class Dog(object):
    name="Jerry"
    def __init__(self,name):
        self.name = name
    @classmethod
    def eat(self):
        print("%s is eating %s" %(self.name,"food"))
    def talk(self):
        print("%s is talking" % self.name)
d = Dog("Tom")
d.eat()
Dog.eat()
d.talk()
# class Dog(object):
#     def __init__(self,name):
#         self.name = name
#
#     @staticmethod
#     def eat(name,food):
#         print("%s is eating %s" %(name,food))
# d = Dog("tom")
# d.eat("tom","包子")
# #通过对象调用方法
# Dog.eat("jerry","面条")
# #通过类调用方法