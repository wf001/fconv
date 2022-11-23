from pathlib import Path
from typing import Any, Dict

from fconv.formats.base import BaseDictionalizeFormat

FIXTURES_ROOT = Path(__file__).parent
JSON_FILE_PATH = str(FIXTURES_ROOT / "test.json")
YAML_FILE_PATH = str(FIXTURES_ROOT / "test.yaml")
TOML_FILE_PATH = str(FIXTURES_ROOT / "test.toml")
XML_FILE_PATH = str(FIXTURES_ROOT / "test.xml")


class FakeValidFormat(BaseDictionalizeFormat):
    def __init__(self):
        super().__init__(load_data_key="", dump_data_key="")

    def load(self, str: Dict[str, Any]) -> Dict[str, Any]:
        return {}  # type: ignore

    def dump(self, internal: Dict[str, Any]) -> str:
        return ""


class FakeInvalidFormat:
    pass
