import argparse
import datetime
from pathlib import Path

JSON_FILE_PATH = Path(__file__).parent.parent / "tests/fixtures/test.json"

HELP = {
    "source": "data format converting from",
    "infile": "a file converting from",
    "target": "data format converting to",
    "outfile": "a file converting to",
    "in_opt": "option sets of a file converting from",
    "out_opt": "option sets of a file converting to",
    "version": "print version number and exit",
    "verbose": "print more information",
}


def valid_format():
    return ["json", "yaml"]


__doc__ = "Convertion tool among many file formats"
__version__ = "1.0"
__prog__ = None


def parse_args():
    p = argparse.ArgumentParser(prog=__prog__, description=__doc__)

    p.add_argument(
        "--v", help=HELP["version"], action="version", version=f"version: {__version__}"
    ),
    p.add_argument("-o", help=HELP["outfile"]),
    p.add_argument("--verbose", help=HELP["verbose"], action="store_true")

    p.add_argument("source", help=HELP["source"], choices=valid_format())
    p.add_argument("-i", required=True, help=HELP["infile"])
    p.add_argument("target", help=HELP["target"], choices=valid_format())
    args = p.parse_args()

    return args


def main():
    p = parse_args()
    print(p)
    _main()


def _main():
    # from former.core import Former

    dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
    print(dt)


#    out_name = f"{dt}.yaml"
#
#    r = Former(
#        src_format="json",
#        target_format="yaml",
#        src_path=JSON_FILE_PATH,
#        target_path=out_name,
#    ).form()
#    print(r)
#    os.remove(out_name)


if __name__ == "__main__":
    main()
