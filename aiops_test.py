

time_local = time.localtime(timestamp)
# 转换成新的时间格式(2016-05-05 20:28:54)
dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
v = {"t": dt, 'id': id}

sql = "SELECT * FROM predict where timestamp=%(t)s and item_id=%(id)s"
# 执行SQL语句
cursor.execute(sql, v)
results = cursor.fetchall()
d.close()
