import time
# class Date:
# 	def __init__(self,year,month,day):
# 		self.year=year
# 		self.month=month
# 		self.day=day
# 	# @staticmethod
# 	# def now():
# 	#     t=time.localtime()
# 	#     return Date(t.tm_year,t.tm_mon,t.tm_mday)
#
# 	@classmethod #改成类方法
# 	def now(cls):
# 		t=time.localtime()
# 		cls.year = t.tm_year
# 		cls.month = t.tm_mon
# 		cls.day = t.tm_mday
# 		cls.hour=t.tm_hour
# 	#哪个类来调用,即用哪个类cls来实例化
#
# class EuroDate(Date):
# 	def __str__(self):
# 		return 'year:%s month:%s day:%s ' %(self.year,self.month,self.day)
#
# e=EuroDate.now()
# print(e) #我们的意图是想触发EuroDate.__str__,此时e就是由EuroDate产生的,所以会如我们所愿
'''
输出结果:
year:2017 month:3 day:3
'''

class Date:
  def __init__(self, month, day, year):
    self.month = month
    self.day   = day
    self.year  = year


  def display(self):
    return "{0}-{1}-{2}".format(self.month, self.day, self.year)


  @staticmethod
  def millenium(month, day):
    return Date(month, day, 2000)


new_year = Date(1, 1, 2013)               # Creates a new Date object
millenium_new_year = Date.millenium(1, 1) # also creates a Date object.

# Proof:
new_year.display()           # "1-1-2013"
millenium_new_year.display() # "1-1-2000"

isinstance(new_year, Date) # True
isinstance(millenium_new_year, Date) # True
