import argparse

from former import HELP, __doc__, __prog__, __version__
from former.core import Former
from former.formats import SUPPORTED_FORMATS, get_supported_formats
from inspect import stack, currentframe
from logging import getLogger, StreamHandler, Formatter, DEBUG, ERROR


def parse_args():
    p = argparse.ArgumentParser(prog=__prog__, description=__doc__)

    p.add_argument(
        "--v", help=HELP["version"], action="version", version=f"version: {__version__}"
    ),
    p.add_argument("-o", help=HELP["outfile"]),
    p.add_argument("--verbose", help=HELP["verbose"], action="store_true")

    p.add_argument("source", help=HELP["source"],
                   choices=get_supported_formats())
    p.add_argument("-i", required=True, help=HELP["infile"])
    p.add_argument("target", help=HELP["target"],
                   choices=get_supported_formats())
    args = p.parse_args()

    return args


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyLogger(object, metaclass=SingletonType):
    _logger = None

    def __init__(self, level):
        self._logger = getLogger()
        self._logger.setLevel(level)
        formatter = Formatter(
            f'%(module)s.py %(funcName)s() ln.%(lineno)s | [%(levelname)s] %(message)s')

        streamHandler = StreamHandler()
        streamHandler.setFormatter(formatter)
        self._logger.addHandler(streamHandler)
        print("Generate new instance")

    @property
    def logger(self):
        return self._logger


def main():
    p = parse_args()
    l = MyLogger(DEBUG).logger
    l.debug(p)

    # inlclude_verbose = p.verbose
    src_fmt = p.source
    target_fmt = p.target
    src_path = p.i
    target_path = p.o

    Former(
        src_format=SUPPORTED_FORMATS.get(src_fmt),
        target_format=SUPPORTED_FORMATS.get(target_fmt),
        src_path=src_path,
        target_path=target_path,
    ).form()
    return 0


if __name__ == "__main__":
    _main()
