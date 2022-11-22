from typing import Any, Dict

from .base import BaseDictionalizeFormat


class Yaml(BaseDictionalizeFormat):
    def __init__(self):
        super().__init__(load_data_key="stream", dump_data_key="data")

    @staticmethod
    def load(src_ctx: Dict[str, Any]) -> Dict[str, Any]:
        import yaml

        return yaml.safe_load(**src_ctx)

    @staticmethod
    def dump(internal: Dict[str, Any]) -> str:
        import yaml

        return yaml.dump(**internal)
