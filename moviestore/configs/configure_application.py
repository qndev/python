import os
import logging
import logging.config


class ConfigureApplication:

    @staticmethod
    def logger(name: str) -> logging.Logger:

        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s - [PID %(process)d] : Thread "%(threadName)s" : File "%(pathname)s" : Method "%(name)s.%(funcName)s()", line %(lineno)d : Message "%(message)s"')

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler("moviestore/logs/application.log")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

        return logger
