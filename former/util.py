from logging import ERROR, Formatter, StreamHandler, getLogger
from typing import Any, Dict


class SingletonType(type):
    _instances: Dict[Any, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(object, metaclass=SingletonType):
    _logger = None

    def __init__(self, level=ERROR):
        self._logger = getLogger()
        self._logger.setLevel(level)
        formatter = Formatter(
            "\033[32m %(module)s.py\033[0m %(funcName)s() ln.%(lineno)s | [%(levelname)s] %(message)s"
        )

        streamHandler = StreamHandler()
        streamHandler.setFormatter(formatter)
        self._logger.addHandler(streamHandler)
        print("Generate new instance")

    @property
    def logger(self):
        return self._logger


def logg(f):
    def wrapped(*arg, **kwargs):
        log = Logger().logger
        log.debug(f"\033[34m[ENTER]:\033[0m {f.__name__ = }")
        log.debug(f"\033[34m[ENTER]:\033[0m {arg = }")
        log.debug(f"\033[34m[ENTER]:\033[0m {kwargs = }")
        r = f(*arg, **kwargs)
        log.debug(f"\033[33m[EXIT]:\033[0m {r=}")
        log.debug("========================================")
        return r

    return wrapped
