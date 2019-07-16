import logging
import logging.config
import log_config
def get_logger(name='detection.online'):
    """
    获取logger
    :param name:
    :return:
    """
    logging.config.dictConfig(log_config.LOGGING_DIC)
    return logging.getLogger(name)


logger=get_logger()


for i in range(10000):
    msg=i
    logger.warn(i)














# logging.basicConfig(level=logging.INFO,
#                     filename='output.log',
#                     datefmt='%Y/%m/%d %H:%M:%S',
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')
# logger = logging.getLogger(__name__)
#
# logger.info('This is a log info')
# logger.debug('Debugging')
# logger.warning('Warning exists')
# logger.info('Finish')
# logger.critical('crtical something')
