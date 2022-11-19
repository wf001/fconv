from typing import Any, Dict

from .base import BaseFormat

__format__ = "yaml"


class Yaml(BaseFormat):
    def __init__(self):
        super().__init__(__format__)

    @staticmethod
    def load(src_ctx: Dict[str, Any]) -> Dict[str, Any]:
        import yaml

        return yaml.safe_load(**src_ctx)

    @staticmethod
    def dump(internal: Dict[str, Any]) -> str:
        import yaml

        return yaml.dump(**internal)
