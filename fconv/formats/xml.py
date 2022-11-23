from typing import Any, Dict

from .base import BaseDictionalizeFormat


class Xml(BaseDictionalizeFormat):
    def __init__(self):
        super().__init__(load_data_key="xml_input", dump_data_key="input_dict")

    @staticmethod
    def load(src_ctx: Dict[str, Any]) -> Dict[str, Any]:
        import xmltodict as xml

        return xml.parse(**src_ctx)

    @staticmethod
    def dump(internal: Dict[str, Any]) -> str:
        import xmltodict as xml

        _wrapped = {}
        _internal = internal

        _body = internal["input_dict"]
        _wrapped["root"] = _body
        _internal["input_dict"] = _wrapped

        return xml.unparse(**_internal)
