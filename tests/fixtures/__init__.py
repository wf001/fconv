from pathlib import Path

from former.format import AbstractFormat
from former.typing import InternalValue

FIXTURES_ROOT = Path(__file__).parent
JSON_FILE_PATH = FIXTURES_ROOT / "test.json"
YAML_FILE_PATH = FIXTURES_ROOT / "test.yaml"


class FakeValidFormat(AbstractFormat):
    def load(self, str: dict) -> InternalValue:
        return {}  # type: ignore

    def dump(self, internal: InternalValue) -> str:
        return ""

    def _gen_input_kwargs(self, ctx, opt, k):
        pass

    def _gen_output_kwargs(self, ctx, opt):
        pass


class FakeInvalidFormat:
    pass
