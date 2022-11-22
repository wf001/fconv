from typing import Any, Dict

from .base import BaseDictionalizeFormat


class Toml(BaseDictionalizeFormat):
    def __init__(self):
        super().__init__(load_data_key="s", dump_data_key="o")

    @staticmethod
    def load(src_ctx: Dict[str, Any]) -> Dict[str, Any]:
        import toml

        return toml.loads(**src_ctx)

    @staticmethod
    def dump(internal: Dict[str, Any]) -> str:
        import toml

        return toml.dumps(**internal)
