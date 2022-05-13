# given API log files, write program to time log from start to end
# API calls log file
# Read file 
# -> Remove empty lines 
# -> Separate API calls
# -> Add start and end timestamps to specific API call 
# -> Compute average for specific API call
# -> Print API calls and average time

# lowermodule.py
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s')
logger = logging.getLogger(__name__)

def hypotenuse(a, b):
    """Compute the hypotenuse"""
    return (a**2 + b**2)**0.5

kwargs = {'a':3, 'b':4, 'c':hypotenuse(3, 4)}
logging.debug("a = {a}, b = {b}".format(**kwargs))
logging.info("Hypotenuse of {a}, {b} is {c}".format(**kwargs))
logging.warning("a={a} and b={b} are equal".format(**kwargs))
logging.error("a={a} and b={b} cannot be negative".format(**kwargs))
logging.critical("Hypotenuse of {a}, {b} is {c}".format(**kwargs))

