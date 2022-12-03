# Options
## JSON
The following are excerpts from the official documentation. For more information, please see the official documentation.

- https://docs.python.org/2/library/json.html#module-json

### input option

`object_hook` is an optional function that will be called with the result of any object literal decoded (a dict). The return value of object_hook will be used instead of the dict. This feature can be used to implement custom decoders (e.g. JSON-RPC class hinting).

`object_pairs_hook` is an optional function that will be called with the result of any object literal decoded with an ordered list of pairs. The return value of object_pairs_hook will be used instead of the dict. This feature can be used to implement custom decoders. If object_hook is also defined, the object_pairs_hook takes priority.

 `parse_float`, if specified, will be called with the string of every JSON float to be decoded. By default, this is equivalent to float(num_str). This can be used to use another datatype or parser for JSON floats (e.g. decimal.Decimal).

 `parse_int`, if specified, will be called with the string of every JSON int to be decoded. By default, this is equivalent to int(num_str). This can be used to use another datatype or parser for JSON integers (e.g. float).

 `parse_constant`, if specified, will be called with one of the following strings: '-Infinity', 'Infinity', 'NaN'. This can be used to raise an exception if invalid JSON numbers are encountered.


### output option
If `skipkeys` is true (default: False), then dict keys that are not of a basic type (str, int, float, bool, None) will be skipped instead of raising a TypeError.


If `ensure_ascii` is true (the default), the output is guaranteed to have all incoming non-ASCII characters escaped. If ensure_ascii is false, these characters will be output as-is.

If `check_circular` is false (default: True), then the circular reference check for container types will be skipped and a circular reference will result in a RecursionError (or worse).

If `allow_nan` is false (default: True), then it will be a ValueError to serialize out of range float values (nan, inf, -inf) in strict compliance of the JSON specification. If allow_nan is true, their JavaScript equivalents (NaN, Infinity, -Infinity) will be used.

If `indent` is a non-negative integer or string, then JSON array elements and object members will be pretty-printed with that indent level. An indent level of 0, negative, or "" will only insert newlines. None (the default) selects the most compact representation. Using a positive integer indent indents that many spaces per level. If indent is a string (such as "\t"), that string is used to indent each level.

If specified, `separators` should be an (item_separator, key_separator) tuple. The default is (', ', ': ') if indent is None and (',', ': ') otherwise. To get the most compact JSON representation, you should specify (',', ':') to eliminate whitespace.

If specified, `default` should be a function that gets called for objects that can’t otherwise be serialized. It should return a JSON encodable version of the object or raise a TypeError. If not specified, TypeError is raised.

If `sort_keys` is true (default: False), then the output of dictionaries will be sorted by key.


### corresponding table

[input]
| namespace in library | Does CLI ver support | namespace in CLI                            |
| ----------------------- | -------------------- | ------------------------------------------- |
| object_hook             | :x:                  | -                                           |
| object_pairs_hook       | :x:                  | -                                           |
| parse_float             | :o:                  | --json-float-as-int <br>--json-float-as-str |
| parse_int               | :o:                  | --json-int-as-int <br>--json-int-as-str     |
| parse_constant          | :x:                  | -                                           |



[output]
| namespace in library  | Does CLI ver support | namespace in CLI             |
| ----------------------- | -------------------- | ---------------------------- |
| skipkeys                | :o:                  | --json-skip-keys             |
| ensure_ascii            | :x:                  | -                            |
| check_circular          | :o:                  | --json-ignore-check-circular |
| allow_nan               | :o:                  | --json-disallow-nan          |
| indent                  | :o:                  | --json-indent                |
| separators              | :x:                  | -                            |
| default                 | :x:                  | -                            |
| sort_keys               | :o:                  | --json-sort-keys             |



## yaml
The following are excerpts from some documentations. For more information, please see the official documentation and confirm YAML specification.

- https://pyyaml.org/wiki/PyYAMLDocumentation
- https://github.com/yaml/pyyaml

### output option
`Dumper`  supports all predefined tags and may represent an arbitrary Python object.

`default_style` indicates the style of the scalar. Possible values are None, '', '\'', '"', '|', '>'.

`default_flow_style` indicates if a collection is block or flow. The possible values are None, True, False.

`encoding` is output encoding, defaults to utf-8. utf-8', 'utf-16-be' and 'utf-16-le' are available.

`explicit_start` if True, adds an explicit start using “—”.

`explicit_end` if True, adds an explicit end using “—”.

`version` is version of the YAML parser, tuple (major, minor), supports only major version 1. 

`tags` sets the preferred type tags.

`canonical` if True export tag type to the output file.

`indent` sets the preferred indentation.

`width` set the preferred line width.

`allow_unicode` allow unicode in out.ut file.

`line_break`  specify the line break you need.


### corresponding table
[output]
| namespace in library  | Does CLI ver supports | namespace in CLI      |
| ----------------------- | --------------------- | --------------------- |
| Dumper                  | :x:                   | -                     |
| default_style           | :x:                   | -                     |
| default_flow_style      | :x:                   | -                     |
| encoding                | :x:                   | -                     |
| explicit_start          | :o:                   | --yaml-explicit-start |
| explicit_end            | :o:                   | --yaml-explicit-end   |
| version                 | :x:                   | -                     |
| tags                    | :x:                   | -                     |
| canonical               | :x:                   | -                     |
| indent                  | :o:                   | --yaml-indent         |
| width                   | :x:                   | -                     |
| allow_unicode           | :x:                   | -                     |
| line_break              | :x:                   | -                     |

## toml
The following are excerpts from the official documentation. For more information, please see the official documentation.

- https://github.com/uiri/toml

### input option
`_dict`specifies the class of the returned toml dictionary



### output option

`f` is a File descriptor where the TOML-formatted output should be stored

`encoder` is an instance of TomlEncoder (or subclass) for encoding the object. If None, will default to TomlEncoder

### corresponding table
[input]
| namespace in library  | Does CLI ver supports | namespace in CLI      |
| ----------------------- | --------------------- | --------------------- |
| _dict                  | :x:                   | -                     |

[output]
| namespace in library  | Does CLI ver supports | namespace in CLI |
| ----------------------- | --------------------- | ---------------- |
| f                       | :x:                   | -                |
| encoder                 | :x:                   | -                |

## xml
The following are excerpts from the official documentation. For more information, please see the official documentation.

- https://github.com/martinblech/xmltodict

### input option

`encoding` sets intput encoding. 'utf-8', 'utf-16', 'ascii' is available.

`expat` indicates parser type.

`process_namespaces`  will make it expand namespaces.

`namepaces` lets you collapse certain namespaces to shorthand prefixes, or skip them altogether.

`namespace_separator` indicates the separator of the namespaces that you want to collapse.

`disable_entities` disallow DOCTYPE declaration feature.

`process_comments` if True, allow to process comments


### output option
`encoding` sets output encoding. 'utf-8', 'iso-8859-1', ''utf-16' and 'ascii' is available.

`full_document` if False, allow to process none-root document.

`short_empty_elements` indicate closing an item that has no element with empty tag

`pretty` sets the preferred indentation.


### corresponding table
[input]
| namespace in library  | Does CLI ver supports | namespace in CLI         |
| ----------------------- | --------------------- | ------------------------ |
| encoding                | :x:                   | -                        |
| expat                   | :x:                   | -                        |
| process_namespaces      | :o:                   | --xml-process-namespaces |
| namespaces              | :x:                   | -                        |
| namespaces_separator    | :x:                   | -                        |
| disable_entities        | :x:                   | -                        |
| process_comments        | :o:                   | --xml-process-comments   |

[output]
| namespace in library  | Does CLI ver supports | namespace in CLI        |
| ----------------------- | --------------------- | ----------------------- |
| encoding                | :x:                   | -                       |
| pretty                  | :o:                   | --xml-disable-pretty    |
| short_empty_elements    | :x:                   | -                       |
| full_document           | :o:                   | --xml-particle-document |
