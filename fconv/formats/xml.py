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
        """
        {
            'input_dict':{'country': ...,'..:..'},
            'opt1':...,
            'opt2':...
        }
        ->
        {
            'input_dict':{'root':{'country':'...'}},
            'opt1':...,
            'opt2':...
        }
        """
        _internal = {}
        _body = internal['input_dict']
        _internal['root'] = _body
        __internal = internal
        __internal['input_dict'] = _internal

        return xml.unparse(**__internal)
