import time
'''
https://blog.csdn.net/google19890102/article/details/51355282

'''

class TimeConvert(object):

	# 日期转换成时间戳
	def date_convert_timestamp(self,dt):
		return int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S")))

	# 重新格式化时间
	def convert_date_format(self,dt):
		# 转换成时间数组
		timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
		# 转换成新的时间格式(20160505-20:28:54)
		dt_new = time.strftime("%Y%m%d-%H:%M:%S", timeArray)

		return dt_new


	# 时间转换成日期
	def timestamo_convert_date(self):

		timestamp = 1462451334

		# 转换成localtime
		time_local = time.localtime(timestamp)
		# 转换成新的时间格式(2016-05-05 20:28:54)
		dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

		return timestamp,dt
	# 按格式获取当前时间
	def fetch_now_time(self):

		# 获取当前时间
		time_now = int(time.time())
		# 转换成localtime
		time_local = time.localtime(time_now)
		# 转换成新的时间格式(2016-05-09 18:59:20)
		dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

		return time_now,dt



if __name__ == '__main__':
	time_funs=TimeConvert()
	a='2019-09-03 00:00:00'
	b='2019-09-04 00:00:00'
	print(time_funs.date_convert_timestamp(b)-time_funs.date_convert_timestamp(a))
	



