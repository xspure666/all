# 日志级别等级排序：critical > error > warning > info > debug
#
# 级别越高打印的日志越少，反之亦然，即
#
# debug : 打印全部的日志( notset 等同于 debug )
# info : 打印 info, warning, error, critical 级别的日志
# warning : 打印 warning, error, critical 级别的日志
# error : 打印 error, critical 级别的日志
# critical : 打印 critical 级别


import logging


# 打印日志级别
def test_logging():
    logging.basicConfig(filename='example.log', level=logging.ERROR, format='%(asctime)s %(message)s',
                        datefmt='%Y-%m-%d %I:%M:%S %p')
    logging.debug('Python debug')
    logging.info('Python info')
    logging.warning('Python warning')
    logging.error('Python Error')
    logging.critical('Python critical')


test_logging()
