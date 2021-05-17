import os
from moviestore.start_up import StartUp

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def bootstrap():
    StartUp().run(ROOT_DIR)


if __name__ == "__main__":
    bootstrap()
