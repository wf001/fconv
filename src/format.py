import json
from abc import ABC, abstractmethod

import yaml

from .typing import InternalValue


class AbstractFormat(ABC):
    @abstractmethod
    def load(self, src_ctx: dict) -> InternalValue:
        pass

    @abstractmethod
    def dump(self, internal: InternalValue) -> str:
        pass

    @abstractmethod
    def _gen_input_kwargs(self, src_ctx, opt):
        pass

    @abstractmethod
    def _gen_output_kwargs(self, internal, opt):
        pass

    def gen_input_kwargs(self, src_ctx: str, opt: dict, k: str):
        _opt = opt if opt else {}
        _opt[k] = src_ctx
        return _opt

    def gen_output_kwargs(self, internal: InternalValue, opt: dict, k: str):
        _opt = opt if opt else {}
        _opt[k] = internal
        return _opt

    @classmethod
    def _get_valid_format(cls):
        return list(map(lambda x: x.__name__, cls.__subclasses__()))


class Format:
    class Json(AbstractFormat):
        @staticmethod
        def load(src_ctx: dict) -> InternalValue:
            return json.loads(**src_ctx)

        @staticmethod
        def dump(internal: InternalValue) -> str:
            return json.dumps(**internal)

        def _gen_input_kwargs(self, src_ctx: str, opt: dict):
            return super().gen_input_kwargs(src_ctx, opt, "s")

        def _gen_output_kwargs(self, internal: InternalValue, opt: dict):
            return super().gen_output_kwargs(internal, opt, "obj")

    class Yaml(AbstractFormat):
        @staticmethod
        def load(src_ctx: dict) -> InternalValue:
            return yaml.safe_load(**src_ctx)

        @staticmethod
        def dump(internal: InternalValue) -> str:
            return yaml.dump(**internal)

        def _gen_input_kwargs(self, src_ctx, opt):
            return super().gen_input_kwargs(src_ctx, opt, "stream")

        def _gen_output_kwargs(self, internal, opt):
            _opt = super().gen_output_kwargs(internal, opt, "data")
            _opt["Dumper"] = yaml.CDumper
            return _opt

    class XML:
        pass
