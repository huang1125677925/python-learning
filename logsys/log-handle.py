import logging
'''
这玩意有什么用处
也就是可以指定输出格式，输出到



另外我们还可以使用其他的 Handler 进行日志的输出，logging 模块提供的 Handler 有：

StreamHandler：logging.StreamHandler；日志输出到流，可以是 sys.stderr，sys.stdout 或者文件。
FileHandler：logging.FileHandler；日志输出到文件。
BaseRotatingHandler：logging.handlers.BaseRotatingHandler；基本的日志回滚方式。
RotatingHandler：logging.handlers.RotatingHandler；日志回滚方式，支持日志文件最大数量和日志文件回滚。
TimeRotatingHandler：logging.handlers.TimeRotatingHandler；日志回滚方式，在一定时间区域内回滚日志文件。
SocketHandler：logging.handlers.SocketHandler；远程输出日志到TCP/IP sockets。
DatagramHandler：logging.handlers.DatagramHandler；远程输出日志到UDP sockets。
SMTPHandler：logging.handlers.SMTPHandler；远程输出日志到邮件地址。
SysLogHandler：logging.handlers.SysLogHandler；日志输出到syslog。
NTEventLogHandler：logging.handlers.NTEventLogHandler；远程输出日志到Windows NT/2000/XP的事件日志。
MemoryHandler：logging.handlers.MemoryHandler；日志输出到内存中的指定buffer。
HTTPHandler：logging.handlers.HTTPHandler；通过”GET”或者”POST”远程输出到HTTP服务器。
下面我们使用三个 Handler 来实现日志同时输出到控制台、文件、HTTP 服务器：
'''
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler('handle.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')