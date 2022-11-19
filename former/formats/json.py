from typing import Any, Dict

from .base import BaseFormat


class Json(BaseFormat):
    def __init__(self):
        super().__init__(self.load_data_key, self.dump_data_key)

    @property
    def load_data_key(self):
        return "s"

    @property
    def dump_data_key(self):
        return "obj"

    @staticmethod
    def load(src_ctx: Dict[str, Any]) -> Dict[str, Any]:
        import json

        return json.loads(**src_ctx)

    @staticmethod
    def dump(internal: Dict[str, Any]) -> str:
        import json

        return json.dumps(**internal)
