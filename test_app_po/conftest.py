import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d]%'
                           '(levelname)%(message)s',
                    datefmt='%a,%d %b %Y %H:%M:%S',
                    filename='log.log',
                    filemode='w')