import logging
import logging.config


class Config:

    @staticmethod
    def logger(name: str) -> logging.Logger:
        logging.basicConfig(filename="application.log",
                            format="%(asctime)s %(name)s %(levelname)s : %(message)s",
                            level=logging.DEBUG)
        return logging.getLogger(name)
