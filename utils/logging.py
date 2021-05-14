import logging
import logging.config

class LoggingInfo:
    logging.basicConfig(filename='../application.log', format='%(asctime)s %(name)s %(levelname)s : %(message)s', datefmt='%m-%d-%Y %I:%M:%S %p', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    @staticmethod
    def log_messages():
        return logger