from typing import Any, Dict

from .base import BaseFormat


class Yaml(BaseFormat):
    def __init__(self):
        super().__init__(self.load_data_key, self.dump_data_key)

    @property
    def load_data_key(self):
        return "stream"

    @property
    def dump_data_key(self):
        return "data"

    @staticmethod
    def load(src_ctx: Dict[str, Any]) -> Dict[str, Any]:
        import yaml

        return yaml.safe_load(**src_ctx)

    @staticmethod
    def dump(internal: Dict[str, Any]) -> str:
        import yaml

        return yaml.dump(**internal)
