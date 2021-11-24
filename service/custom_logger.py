import logging
import inspect


def loggers(logLevel=logging.DEBUG):
    loggerName = inspect.stack()[1][3]

    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    fileHandle = logging.FileHandler("automation.log", mode='a')
    fileHandle.setLevel(logLevel)

    logFormat = logging.Formatter("""%(asctime)s %(levelname)s: %(message)s """, datefmt='%d/%m/%y ''%I:%M:%S:%p')
    # File "%(pathname)s," line %(lineno)d in %(module)s



    fileHandle.setFormatter(logFormat)
    logger.addHandler(fileHandle)

    return logger


# logFormat = logging.Formatter("""%(asctime)s
#         File "%(pathname)s," line %(lineno)d in %(module)s
#             %(levelname)s: %(message)s """, datefmt='%d/%m/%y ''%I:%M:%S:%p')