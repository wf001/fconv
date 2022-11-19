from typing import Any, Dict

from .base import BaseDictionalizeFormat


class Json(BaseDictionalizeFormat):
    def __init__(self):
        super().__init__(load_data_key="s", dump_data_key="obj")

    @staticmethod
    def load(src_ctx: Dict[str, Any]) -> Dict[str, Any]:
        import json

        return json.loads(**src_ctx)

    @staticmethod
    def dump(internal: Dict[str, Any]) -> str:
        import json

        return json.dumps(**internal)
