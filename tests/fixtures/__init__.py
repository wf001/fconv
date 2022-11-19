from pathlib import Path
from typing import Any, Dict

from former.formats.base import BaseFormat

FIXTURES_ROOT = Path(__file__).parent
JSON_FILE_PATH = str(FIXTURES_ROOT / "test.json")
YAML_FILE_PATH = str(FIXTURES_ROOT / "test.yaml")


class FakeValidFormat(BaseFormat):
    def __init__(self):
        super().__init__("")

    def load(self, str: Dict[str, Any]) -> Dict[str, Any]:
        return {}  # type: ignore

    def dump(self, internal: Dict[str, Any]) -> str:
        return ""


class FakeInvalidFormat:
    pass
