import json
from abc import ABC, abstractmethod

import yaml

from .typing import InternalValue


class AbstractFormat(ABC):
    def __init__(self, input_data_key, output_data_key):
        self.input_data_key = input_data_key
        self.output_data_key = output_data_key

    @abstractmethod
    def load(self, src_ctx: dict) -> InternalValue:
        pass

    @abstractmethod
    def dump(self, internal: InternalValue) -> str:
        pass

    def gen_input_kwargs(self, src_ctx: str, opt: dict):
        _opt = opt if opt else {}
        _opt[self.input_data_key] = src_ctx
        return _opt

    def gen_output_kwargs(self, internal: InternalValue, opt: dict):
        _opt = opt if opt else {}
        _opt[self.output_data_key] = internal
        return _opt

    @classmethod
    def _get_valid_format(cls):
        return list(map(lambda x: x.__name__, cls.__subclasses__()))


class Format:
    class Json(AbstractFormat):
        INPUT_DATA_KEY = "s"
        OUTPUT_DATA_KEY = "obj"

        def __init__(self):
            super().__init__(self.INPUT_DATA_KEY, self.OUTPUT_DATA_KEY)

        @staticmethod
        def load(src_ctx: dict) -> InternalValue:
            return json.loads(**src_ctx)

        @staticmethod
        def dump(internal: InternalValue) -> str:
            return json.dumps(**internal)

    class Yaml(AbstractFormat):
        INPUT_DATA_KEY = "stream"
        OUTPUT_DATA_KEY = "data"

        def __init__(self):
            super().__init__(self.INPUT_DATA_KEY, self.OUTPUT_DATA_KEY)

        @staticmethod
        def load(src_ctx: dict) -> InternalValue:
            return yaml.safe_load(**src_ctx)

        @staticmethod
        def dump(internal: InternalValue) -> str:
            return yaml.dump(**internal)

    class XML:
        pass
