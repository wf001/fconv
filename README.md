# fconv

![GitHub](https://img.shields.io/github/license/wf001/fconv)
![Github](https://img.shields.io/static/v1?label=fconv&message=for%20Terminal&color=FA9BFA)
![GitHub release (latest by date)](https://img.shields.io/pypi/v/fconv)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/wf001/fconv/Python%20application)
![PyPI version](https://img.shields.io/pypi/pyversions/fconv)

fconv is a Command-Line utility and library for converting between multiple file formats such as JSON, YAML.

## Getting started
```
pip install fconv
```

```
$ fconv --v
version: x.x.x
```

## Features
- Convert a file into other formatted file

- Supported format 
	- json
	- yaml
	- toml

- To be supported
	- xml
	- ini

You can use fconv as command-line tool and Python module.In condition of using as a module, fconv supports optional arguments.

To know which options are available,

See the reference:

- json:https://docs.python.org/3/library/json.html
- yaml:https://pyyaml.org/wiki/PyYAMLDocumentation
- toml:https://github.com/uiri/toml

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


## Contribution
Have a look through existing Issues and Pull Requests that you could help with. If you'd like to request a feature or report a bug, please create a GitHub Issue using one of the templates provided.

[See contribution guide->](https://github.com/wf001/fconv/blob/master/CONTRIBUTING.md)


### License
Licensed under the MIT License.
