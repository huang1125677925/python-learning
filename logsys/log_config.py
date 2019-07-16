"""
日志配置文件
"""
import os

# BASE_LOG = os.path.join(BASE_DIR, 'logs/run.log')

FILENAME = "run.log"
if os.name == 'nt':
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    BASE_LOG = BASE_DIR + '\\logs\\%s' % FILENAME
else:
    BASE_LOG = os.path.join('%s' % FILENAME)

standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'  # 其中name为getlogger指定的名字

simple_format = '%(name)s-%(levelname)s-%(asctime)s-%(message)s'

id_simple_format = '[task_id:%(name)s][%(levelname)s][%(asctime)s] %(message)s'

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,

    # 1、定义日志的格式
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'id_simple': {
            'format': id_simple_format
        }
    },
    'filters': {},

    # 2、定义日志输出的目标：文件或者终端
    'handlers': {
        # 打印到终端的日志
        'stream': {
            'level': 'DEBUG',  # 定义接收级别
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'  # 定义什么的格式输出
        },
        # 打印到文件的日志,收集info及以上的日志
        'access': {
            'level': 'DEBUG',  # 定义接收级别
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'simple',  # 定义什么的格式输出
            'filename': BASE_LOG,  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,  # 存5个文件
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        # 打印到文件的日志,收集info及以上的日志
        'day': {
            'level': 'DEBUG',  # 定义接收级别
            'class': 'logging.handlers.TimedRotatingFileHandler',  # 保存到文件
            'formatter': 'simple',  # 定义什么的格式输出
            'filename': BASE_LOG,  # 日志文件
            'when': 'D',  # D表示天，还有H，M
            'interval': 1,  # 增量的频率，1天
            'backupCount': 15,  # 存15个文件
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },

    },

    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['day', 'stream'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'INFO',
            'propagate': False,  # 向上（更高level的logger）传递
        },
    },
}
