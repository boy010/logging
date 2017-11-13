# coding=utf-8  
__author__ = 'liu.chunming'  
import logging  
  
# logging.basicConfig(level=logging.WARNING,  
                    # format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  

# logging.basicConfig(level=logging.WARNING,
#                     filename='./log/log.txt',
#                     filemode='w',
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

#step 1, create one logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Step 2, create one handler, to write log file
logfile = './log/logger.txt'
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.DEBUG)

#Step 3, create another handler , to output to consle
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

# Step 4, define handler output format
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

#Step 5, add logger to handler
logger.addHandler(fh)
logger.addHandler(ch)

# use logging  
logging.info('this is a loggging info message')  
logging.debug('this is a loggging debug message')  
logging.warning('this is loggging a warning message')  
logging.error('this is an loggging error message')  
logging.critical('this is a loggging critical message') 