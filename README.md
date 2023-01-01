![](https://drive.google.com/uc?export=view&id=1qFjfwcWq-C5AY16V916zyz2eYmioWmWX)

# fconv

![GitHub](https://img.shields.io/github/license/wf001/fconv)
![Github](https://img.shields.io/static/v1?label=fconv&message=for%20Terminal&color=FA9BFA)
![GitHub release (latest by date)](https://img.shields.io/pypi/v/fconv)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/wf001/fconv/python.yaml?branch=master)
![PyPI version](https://img.shields.io/pypi/pyversions/fconv)
[![codecov](https://codecov.io/gh/wf001/fconv/branch/master/graph/badge.svg?token=2WQLCPD4AJ)](https://codecov.io/gh/wf001/fconv)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/7a703111e4ec4ccd81b1e6ce67f8b335)](https://www.codacy.com/gh/wf001/fconv/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=wf001/fconv&amp;utm_campaign=Badge_Grade)

fconv is a Command-Line utility and library for converting between multiple file formats such as JSON, YAML.

## Getting started
```
pip install fconv
```

```
$ fconv --v
fconv: vx.x.x
```

## Features
- Convert a format into other format

- Supported format 
	- JSON
	- YAML
	- TOML
	- XML

- To be supported
	- INI
	- JSON5

- You can use fconv as command-line tool and Python module.

- Using fconv as a module, String and file are available as input or output.

- Using fconv as CLI tool, only file is available as input and String and file are available as output.

The options available in the CLI version are different from those available in the module version.

To know which options are available,

See [SPEC.md](https://github.com/wf001/fconv/blob/master/SPEC.md):

## Example
### Use as a module
```
>>> from fconv.core import Former
>>> from fconv.formats.json import Json
>>> from fconv.formats.yaml import Yaml
>>> f = Former(src_format=Json, target_format=Yaml)

>>> f.form('{"key1":"value1"}')
'key1: value1\\n'

>>> f = Former(src_format=Yaml, target_format=Json, out_opt={'indent':3})
>>> f.form('key1: value1\\n')
'{\\n   "key1": "value1"\\n}'
```

### Use as a command-line tool
Basic usage
```
fconv <source format> <target format> -i <source file name>
```

Convert json file into yaml and print out
```
fconv json yaml -i sample.json
```

Convert yaml file into json formated file
```
fconv yaml json -i sample.yaml -o result.json
```

Convert yaml file into json formated file with json indent option
```
fconv yaml json -i sample.yaml -o result.json --json-indent 2
```

```
$ fconv -h
usage: fconv [-h] -i I [--v] [--debug] [-o O] [--json-float-as-int]
             [--json-float-as-str] [--json-int-as-float] [--json-int-as-str]
             [--json-skip-keys] [--json-ignore-check-circular]
             [--json-disallow-nan] [--json-indent JSON_INDENT]
             [--json-sort-keys] [--yaml-explicit-start] [--yaml-explicit-end]
             [--yaml-indent YAML_INDENT] [--xml-process-namespaces]
             [--xml-process-comments] [--xml-particle-document]
             [--xml-disable-pretty]
             source-format target-format

Converter between multiple open-standard file formats.

positional arguments:
  source-format         data format converting from
  target-format         data format converting to

options:
  -h, --help            show this help message and exit
  -i I                  (Required) a file converting from
  --v                   print version number and exit
  --debug               print more information
  -o O                  a file converting to
  --json-float-as-int   JSON float to be decoded with int
  --json-float-as-str   JSON float to be decoded with string
  --json-int-as-float   JSON int to be decoded with float
  --json-int-as-str     JSON int to be decoded with string
  --json-skip-keys      keys that are not of a basic type (str, int, float,
                        bool, None) will be skipped
  --json-ignore-check-circular
                        the circular reference check for container types will
                        be skipped
  --json-disallow-nan   disallow to serialize out of range float values (nan,
                        inf, -inf) in strict compliance of the JSON
                        specification.
  --json-indent JSON_INDENT
                        JSON array elements and object members will be pretty-
                        printed with that indent level.
  --json-sort-keys      the output of dictionaries will be sorted by key.
  --yaml-explicit-start
                        add explicit start marker(See also
                        https://yaml.org/spec/1.2.2/#914-explicit-documents)
  --yaml-explicit-end   add explicit end marker(See also
                        https://yaml.org/spec/1.2.2/#914-explicit-documents)
  --yaml-indent YAML_INDENT
                        YAML array elements and object members will be pretty-
                        printed with that indent level.
  --xml-process-namespaces
                        enable namespace support(See more info at
                        https://github.com/martinblech/xmltodict#namespace-
                        support)
  --xml-process-comments
                        treat comments directives as an attribute
  --xml-particle-document
                        disable to add document root attribute
  --xml-disable-pretty  disable XML document to be pretty-printed with indent

```

## Contribution
Have a look through existing Issues and Pull Requests that you could help with. If you'd like to request a feature or report a bug, please create a GitHub Issue using one of the templates provided. Any kind of contribution and suggestions are highly appreciated!

[See contribution guide->](https://github.com/wf001/fconv/blob/master/CONTRIBUTING.md)


### License
Licensed under the MIT License.
