import argparse
from argparse import Namespace
from logging import DEBUG, ERROR

from fconv import HELP, __doc__, __prog__, __version__
from fconv.core import Former
from fconv.formats import SUPPORTED_FORMATS, get_supported_formats
from fconv.util import Logger


def parse_args() -> Namespace:
    p = argparse.ArgumentParser(prog=__prog__, description=__doc__)

    # Required
    p.add_argument("source", help=HELP["source"], choices=get_supported_formats())
    p.add_argument("-i", required=True, help=HELP["infile"])
    p.add_argument("target", help=HELP["target"], choices=get_supported_formats())

    # Info
    p.add_argument(
        "--v", help=HELP["version"], action="version", version=f"version: {__version__}"
    ),
    p.add_argument("--debug", help=HELP["debug"], action="store_true")

    # Optional
    p.add_argument("-o", help=HELP["outfile"])
    p.add_argument("--json-float-as-int", help=HELP["json_float_as_int"], action="store_true")
    p.add_argument("--json-float-as-str", help=HELP["json_float_as_str"], action="store_true")
    p.add_argument("--json-int-as-float", help=HELP["json_int_as_float"], action="store_true")
    p.add_argument("--json-int-as-str", help=HELP["json_int_as_str"], action="store_true")
    #p.add_argument("--json-skip-keys", help=HELP["json_skip_keys"], action="store_true")
    #p.add_argument("--json-ignore-check-circular", help=HELP["json_ignore_check_circular"], action="store_true")
    #p.add_argument("--json-disallow-nan", help=HELP["json_disallow_nan"], action="store_true")
    #p.add_argument("--json-indent", help=HELP["json_indent"])
    #p.add_argument("--json-sort-keys", help=HELP["json_sort_keys"], action="store=true")

    args = p.parse_args()

    return args

def __int(x):
    return int(float(x))

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

    in_opt = {}
    out_opt = {}
    if p.json_float_as_int and p.json_float_as_str:
        raise Exception()
    if p.json_int_as_str and p.json_int_as_float:
        raise Exception()
    if p.json_float_as_int:
        in_opt['parse_float'] = __int
    elif p.json_float_as_str:
        in_opt['parse_float'] = str

    if p.json_int_as_float:
        in_opt['parse_int'] = float
    elif p.json_int_as_str:
        in_opt['parse_int'] = str


    r = Former(
        src_format=SUPPORTED_FORMATS.get(src_fmt),
        target_format=SUPPORTED_FORMATS.get(target_fmt),
        src_path=src_path,
        target_path=target_path,
        in_opt=in_opt,
        out_opt=out_opt
    ).form()

    if not target_path:
        print(r)


if __name__ == "__main__":
    main()
