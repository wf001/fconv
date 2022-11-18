import json
from abc import ABC, abstractmethod

import yaml


class AbstractFormat(ABC):
    @abstractmethod
    def load(self, src_ctx: dict) -> dict:
        pass

    @abstractmethod
    def dump(self, internal: dict) -> str:
        pass

    @abstractmethod
    def _gen_input_kwargs(self, src_ctx, opt):
        pass

    @abstractmethod
    def _gen_output_kwargs(self, internal, opt):
        pass

    def gen_input_kwargs(self, src_ctx, opt, k):
        _opt = opt if opt else {}
        _opt[k] = src_ctx
        return _opt

    def gen_output_kwargs(self, internal, opt, k):
        _opt = opt if opt else {}
        _opt[k] = internal
        return _opt

    @classmethod
    def _get_valid_format(cls):
        return list(map(lambda x: x.__name__, cls.__subclasses__()))


class Format:
    class Json(AbstractFormat):
        def _gen_input_kwargs(self, src_ctx, opt):
            return super().gen_input_kwargs(src_ctx, opt, "s")

        def _gen_output_kwargs(self, internal, opt):
            return super().gen_output_kwargs(internal, opt, "obj")

        @staticmethod
        def load(src_ctx: dict) -> dict:
            return json.loads(**src_ctx)

        @staticmethod
        def dump(internal: dict) -> str:
            return json.dumps(**internal)

    class Yaml(AbstractFormat):
        def _gen_input_kwargs(self, src_ctx, opt):
            return super().gen_input_kwargs(src_ctx, opt, "stream")

        def _gen_output_kwargs(self, internal, opt):
            _opt = super().gen_output_kwargs(internal, opt, "data")
            _opt["Dumper"] = yaml.CDumper
            return _opt

        def load(self, src_ctx: dict) -> dict:
            return yaml.safe_load(**src_ctx)

        def dump(self, internal: dict) -> str:
            return yaml.dump(**internal)

    class XML:
        pass
