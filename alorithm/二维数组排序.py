students = [[3,'Jack',12],[2,'Rose',13],[1,'Tom',10],[5,'Sam',12],[4,'Joy',8]]

sorted(students,key=(lambda x:x[0]))
# 按年龄倒序
sorted(students,key=(lambda x:x[2]),reverse=True)
# 按年龄为主要关键字，名字次
sorted(students,key=(lambda x:[x[2],x[1]]),reverse=True)
# 按三元进行排序
sorted(students,key=(lambda x:[x[2],x[1],x[0]]),reverse=True)