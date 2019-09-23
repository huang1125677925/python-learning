class A():
    def __init__(self,name):
        self.name=name
        
    def __str__(self):
        return '我是A类的实力对象，我的名字叫{}'.format(self.name)
    
    
    def __repr__(self):
        return '我是A的实力对象'
    
    
    

a=A('huangchuang')

print(a)