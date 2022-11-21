import argparse

from former import HELP, __doc__, __prog__, __version__
from former.core import Former
from former.formats import SUPPORTED_FORMATS, get_supported_formats
from inspect import stack, currentframe
from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO, ERROR

llevel = ERROR

logger = getLogger(__name__)
logger.setLevel(llevel)

formatter = Formatter(
    f'%(module)s.py %(funcName)s() ln.%(lineno)s | [%(levelname)s] %(message)s')

sh = StreamHandler()
sh.setLevel(llevel)
sh.setFormatter(formatter)
logger.addHandler(sh)

def main():
    logger.debug("hoge")
    logger.error("hoge")


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


def _main():
    p = parse_args()
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
