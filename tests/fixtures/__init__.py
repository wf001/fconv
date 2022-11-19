from pathlib import Path
from typing import Any, Dict

from former.format import AbstractFormat

FIXTURES_ROOT = Path(__file__).parent
JSON_FILE_PATH = FIXTURES_ROOT / "test.json"
YAML_FILE_PATH = FIXTURES_ROOT / "test.yaml"


class FakeValidFormat(AbstractFormat):
    def __init__(self):
        super().__init__(self.input_data_key, self.output_data_key)

    @property
    def input_data_key(self):
        return "fake"

    @property
    def output_data_key(self):
        return "fake"

    def load(self, str: Dict[str, Any]) -> Dict[str, Any]:
        return {}  # type: ignore

    def dump(self, internal: Dict[str, Any]) -> str:
        return ""


class FakeInvalidFormat:
    pass
