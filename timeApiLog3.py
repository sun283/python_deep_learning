# Refs https://www.loggly.com/ultimate-guide/python-logging-basics/
#Logging to Standard Output for Systemd

import logging
import os
 
class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return repr(result)
 
    def format(self, record):
        result = super().format(record)
        if record.exc_text:
            result = result.replace("\n", "")
        return result
 
handler = logging.StreamHandler()
formatter = OneLineExceptionFormatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)
 
try:
    exit(main())
except Exception:
    logging.exception("Exception in main(): ")
    exit(1)
    
# import logging
# import logging.handlers
# import os
 
# handler = logging.handlers.WatchedFileHandler(
#     os.environ.get("LOGFILE", "/var/log/yourapp.log"))
# formatter = logging.Formatter(logging.BASIC_FORMAT)
# handler.setFormatter(formatter)
# root = logging.getLogger()
# root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
# root.addHandler(handler)
 
# try:
#     exit(main())
# except Exception:
#     logging.exception("Exception in main()")
#     exit(1)