import argparse
from argparse import Namespace
from logging import DEBUG, ERROR

from fconv import HELP, __doc__, __prog__, __version__
from fconv.core import Former
from fconv.formats import SUPPORTED_FORMATS, get_supported_formats
from fconv.util import Logger


def _set_opts() -> Namespace:
    p = argparse.ArgumentParser(prog=__prog__, description=__doc__)

    # Required
    p.add_argument(
        "source",
        help=HELP["source"],
        choices=get_supported_formats(),
        metavar="source-format",
    )
    p.add_argument("-i", required=True, help=HELP["infile"])
    p.add_argument(
        "target",
        help=HELP["target"],
        choices=get_supported_formats(),
        metavar="target-format",
    )

    # Optional
    p.add_argument(
        "--v",
        help=HELP["version"],
        action="version",
        version=f"{__prog__}: v{__version__}",
    ),
    p.add_argument("--debug", help=HELP["debug"], action="store_true")

    p.add_argument("-o", help=HELP["outfile"])
    # json input
    p.add_argument(
        "--json-float-as-int", help=HELP["json_float_as_int"], action="store_true"
    )
    p.add_argument(
        "--json-float-as-str", help=HELP["json_float_as_str"], action="store_true"
    )
    p.add_argument(
        "--json-int-as-float", help=HELP["json_int_as_float"], action="store_true"
    )
    p.add_argument(
        "--json-int-as-str", help=HELP["json_int_as_str"], action="store_true"
    )
    # json output
    p.add_argument("--json-skip-keys", help=HELP["json_skip_keys"], action="store_true")
    p.add_argument(
        "--json-ignore-check-circular",
        help=HELP["json_ignore_check_circular"],
        action="store_true",
    )
    p.add_argument(
        "--json-disallow-nan", help=HELP["json_disallow_nan"], action="store_true"
    )
    p.add_argument("--json-indent", help=HELP["json_indent"], type=int)
    p.add_argument("--json-sort-keys", help=HELP["json_sort_keys"], action="store_true")

    # yaml output
    p.add_argument(
        "--yaml-explicit-start", help=HELP["yaml_explicit_start"], action="store_true"
    )
    p.add_argument(
        "--yaml-explicit-end", help=HELP["yaml_explicit_end"], action="store_true"
    )
    p.add_argument("--yaml-indent", help=HELP["yaml_indent"], type=int)

    # xml intput
    p.add_argument(
        "--xml-process-namespaces",
        help=HELP["xml_process_namespaces"],
        action="store_true",
    )
    p.add_argument(
        "--xml-process-comments", help=HELP["xml_process_comments"], action="store_true"
    )

    # xml output
    p.add_argument(
        "--xml-particle-document",
        help=HELP["xml_particle_document"],
        action="store_true",
    )
    p.add_argument(
        "--xml-disable-pretty", help=HELP["xml_disable_pretty"], action="store_true"
    )

    a = p.parse_args()
    return a


def parse_args(a):
    in_opt, out_opt = {}, {}
    if a.json_float_as_int and a.json_float_as_str:
        raise ValueError(
            "It can use either --json-float-as-int or --json-float-as-str "
        )
    if a.json_int_as_str and a.json_int_as_float:
        raise ValueError("It can use either --json-int-as-float or --json-int-as-str ")

    # FIXME: too redundant
    # json input
    if a.json_float_as_int:
        in_opt["parse_float"] = __int
    elif a.json_float_as_str:
        in_opt["parse_float"] = str

    if a.json_int_as_float:
        in_opt["parse_int"] = float
    elif a.json_int_as_str:
        in_opt["parse_int"] = str

    # json output
    if a.json_skip_keys:
        out_opt["skipkeys"] = True

    if a.json_ignore_check_circular:
        out_opt["check_circular"] = False

    if a.json_disallow_nan:
        out_opt["allow_nan"] = False

    if a.json_indent is not None:
        out_opt["indent"] = a.json_indent  # type:ignore

    if a.json_sort_keys:
        out_opt["sort_keys"] = a.json_sort_keys

    # yaml output
    if a.yaml_explicit_start:
        out_opt["explicit_start"] = True
    if a.yaml_explicit_end:
        out_opt["explicit_end"] = True
    if a.yaml_indent is not None:
        out_opt["indent"] = a.yaml_indent
    # xml input
    if a.xml_process_namespaces:
        in_opt["process_namespaces"] = True  # type:ignore
    if a.xml_process_comments:
        in_opt["process_comments"] = True  # type:ignore
    # xml output
    if a.xml_particle_document:
        out_opt["full_document"] = False
    if a.xml_disable_pretty:
        out_opt["pretty"] = False
    return in_opt, out_opt


def __int(x):
    return int(float(x))


def main() -> None:
    """
    Enterypoint for CLI command 'fconv'
    """
    p = _set_opts()
    llevel = DEBUG if p.debug else ERROR
    Logger(llevel)

    src_fmt = p.source
    target_fmt = p.target
    src_path = p.i
    target_path = p.o

    in_opt, out_opt = parse_args(p)

    r = Former(
        src_format=SUPPORTED_FORMATS.get(src_fmt),
        target_format=SUPPORTED_FORMATS.get(target_fmt),
        src_path=src_path,
        target_path=target_path,
        in_opt=in_opt,
        out_opt=out_opt,
    ).form()

    if not target_path:
        print(r)


if __name__ == "__main__":
    main()
