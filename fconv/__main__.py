import argparse
from argparse import Namespace
from logging import DEBUG, ERROR

from fconv import HELP, __doc__, __prog__, __version__
from fconv.core import Former
from fconv.formats import SUPPORTED_FORMATS, get_supported_formats
from fconv.util import Logger


def parse_args() -> Namespace:
    p = argparse.ArgumentParser(prog=__prog__, description=__doc__)

    p.add_argument(
        "--v", help=HELP["version"], action="version", version=f"version: {__version__}"
    ),
    p.add_argument("-o", help=HELP["outfile"]),
    p.add_argument("--debug", help=HELP["debug"], action="store_true")

    p.add_argument("source", help=HELP["source"], choices=get_supported_formats())
    p.add_argument("-i", required=True, help=HELP["infile"])
    p.add_argument("target", help=HELP["target"], choices=get_supported_formats())
    args = p.parse_args()

    return args


def main() -> None:
    """
    Enterypoint for CLI command 'fconv'
    """
    p = parse_args()
    llevel = DEBUG if p.debug else ERROR
    Logger(llevel)

    src_fmt = p.source
    target_fmt = p.target
    src_path = p.i
    target_path = p.o

    r = Former(
        src_format=SUPPORTED_FORMATS.get(src_fmt),
        target_format=SUPPORTED_FORMATS.get(target_fmt),
        src_path=src_path,
        target_path=target_path,
    ).form()

    if not target_path:
        print(r)


if __name__ == "__main__":
    main()
