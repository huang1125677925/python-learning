# import urllib2
# url ='http://www.baidu.com'
# data = urllib2.urlopen(url)
# print(data.read())

class CapStr(str):
    def __new__(cls, string):
        string=string.upper()
        return str.__new__(cls,string)
    
    

print(CapStr('huangchuang'))