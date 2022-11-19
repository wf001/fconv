from typing import Any, Dict

from .base import BaseFormat

__format__ = "json"


class Json(BaseFormat):
    def __init__(self):
        super().__init__(__format__)

    @staticmethod
    def load(src_ctx: Dict[str, Any]) -> Dict[str, Any]:
        import json

        return json.loads(**src_ctx)

    @staticmethod
    def dump(internal: Dict[str, Any]) -> str:
        import json

        return json.dumps(**internal)
