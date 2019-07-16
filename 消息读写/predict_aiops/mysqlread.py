import pymysql
import pandas as pd
import time
d = pymysql.connect(db='aiops_monitor', user='root', passwd='1234', host='58.16.78.136', port=23306)
cursor = d.cursor()
timestamp = 1558379035.0
id=17
#转换成localtime
time_local = time.localtime(timestamp)
#转换成新的时间格式(2016-05-05 20:28:54)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
value = {"t":dt,'id':id}

sql = "SELECT * FROM predict where timestamp=%(t)s and item_id=%(id)s"
   # 执行SQL语句
cursor.execute(sql,value)


   # 获取所有记录列表
results = cursor.fetchall()
print(results)

# 关闭数据库连接
d.close()
