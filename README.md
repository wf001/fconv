# former
Python library/CLI command that convert between multiple file formats

## Getting started
```
pip install --upgrade git+https://github.com/wf001/former
```

```
$ former --v
version: 1.0.0
```

## Features
- Converting a file into other formatted file

- Supportting format 
	- json
	- yaml

- Plan to support
	- xml
	- toml
	- ini


- In condition of using as a module, former supports optional arguments.

To know which options are available,

See the reference:

- json:https://docs.python.org/3/library/json.html
- yaml:https://pyyaml.org/wiki/PyYAMLDocumentation

## Example
### Use as a module
```
>>> from former.core import Former
>>> from former.formats.json import Json
>>> from former.formats.yaml import Yaml
>>> f = Former(src_format=Json, target_format=Yaml)

>>> f.form('{"key1":"value1"}')
'key1: value1\\n'

>>> f = Former(src_format=Yaml, target_format=Json, out_opt={'indent':3})
>>> f.form('key1: value1\\n')
'{\\n   "key1": "value1"\\n}'
```

### Use as a CLI command
Basic usage
```
former <source format> <target format> -i <source file name>
```

Convert json file into yaml and print out
```
former json yaml -i sample.json
```

Convert yaml file into json formated file
```
former yaml json -i sample.yaml -o result.json
```

### License
Licensed under the MIT License.
