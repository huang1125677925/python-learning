import datetime
d1 = datetime.datetime(2018,10,31)   # 第一个日期
d2 = datetime.datetime(2019,02,02)   # 第二个日期
interval = d2 - d1                   # 两日期差距
interval.days                        # 具体的天数

interval.seconds                     # 具体的秒数
