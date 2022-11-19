from pathlib import Path

from former.format import AbstractFormat
from former.typing import InternalValue

FIXTURES_ROOT = Path(__file__).parent
JSON_FILE_PATH = FIXTURES_ROOT / "test.json"
YAML_FILE_PATH = FIXTURES_ROOT / "test.yaml"


class FakeValidFormat(AbstractFormat):
    INPUT_DATA_KEY = "fake"
    OUTPUT_DATA_KEY = "fake"

    def __init__(self):
        super().__init__(self.INPUT_DATA_KEY, self.OUTPUT_DATA_KEY)

    def load(self, str: dict) -> InternalValue:
        return {}  # type: ignore

    def dump(self, internal: InternalValue) -> str:
        return ""


class FakeInvalidFormat:
    pass
