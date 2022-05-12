# given API log files, write program to time log from start to end
# API calls log file
# Read file 
# -> Remove empty lines 
# -> Separate API calls
# -> Add start and end timestamps to specific API call 
# -> Compute average for specific API call
# -> Print API calls and average time

import logging

# Gets or creates a logger
logger = logging.getLogger(__name__)  

# set log level
logger.setLevel(logging.WARNING)

# define file handler and set formatter
file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)

# Logs
logger.debug('A debug message')
logger.info('An info message')
logger.warning('Something is not right.')
logger.error('A Major error has happened.')
logger.critical('Fatal error. Cannot continue')