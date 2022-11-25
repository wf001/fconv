__doc__ = "Converter between multiple open-standard file formats."
__version__ = "3.0.0"
__prog__ = "fconv"
__author__ = "wf001"
__license__ = "MIT"
__url__ = "https://github.com/wf001/fconv"

HELP = {
    "source": "data format converting from",
    "infile": "(Required) a file converting from",
    "target": "data format converting to",
    "outfile": "a file converting to",
    "in_opt": "option sets of a file converting from",
    "out_opt": "option sets of a file converting to",
    "version": "print version number and exit",
    "debug": "print more information",
    "json_float_as_str": "JSON float to be decoded with string",
    "json_float_as_int": "JSON float to be decoded with int",
    "json_int_as_str": "JSON int to be decoded with string",
    "json_int_as_float": "JSON int to be decoded with float",
    "json_skip_keys": " keys that are not of a basic type (str, int, float, bool, None) will be skipped",
    "json_ignore_check_circular": "the circular reference check for container types will be skipped",
    "json_disallow_nan": "disallow to serialize out of range float values (nan, inf, -inf) in strict compliance of the JSON specification. ",
    "json_indent": "JSON array elements and object members will be pretty-printed with that indent level. ",
    "json_sort_keys": "the output of dictionaries will be sorted by key.",
}
