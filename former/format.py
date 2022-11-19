import json
from abc import ABC, abstractmethod
from typing import Any, Dict

import yaml


class AbstractFormat(ABC):
    def __init__(self, load_data_key, dump_data_key):
        self._load_data_key = load_data_key
        self._dump_data_key = dump_data_key

    @property
    @abstractmethod
    def load_data_key(self):
        return self._load_data_key

    @property
    @abstractmethod
    def dump_data_key(self):
        return self._dump_data_key

    @abstractmethod
    def load(self, src_ctx: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def dump(self, internal: Dict[str, Any]) -> str:
        raise NotImplementedError

    @classmethod
    def _get_valid_format(cls):
        return list(map(lambda x: x.__name__, cls.__subclasses__()))


class BaseFormat(AbstractFormat):
    def gen_input_kwargs(self, src_ctx: str, opt: Dict[str, Any]):
        _opt = opt if opt else {}
        _opt[self.load_data_key] = src_ctx
        return _opt

    def gen_output_kwargs(self, internal: Dict[str, Any], opt: Dict[str, Any]):
        _opt = opt if opt else {}
        _opt[self.dump_data_key] = internal
        return _opt


class Json(BaseFormat):
    def __init__(self):
        super().__init__(self.load_data_key, self.dump_data_key)

    @property
    def load_data_key(self):
        return "s"

    @property
    def dump_data_key(self):
        return "obj"

    @staticmethod
    def load(src_ctx: Dict[str, Any]) -> Dict[str, Any]:
        return json.loads(**src_ctx)

    @staticmethod
    def dump(internal: Dict[str, Any]) -> str:
        return json.dumps(**internal)


class Yaml(BaseFormat):
    def __init__(self):
        super().__init__(self.load_data_key, self.dump_data_key)

    @property
    def load_data_key(self):
        return "stream"

    @property
    def dump_data_key(self):
        return "data"

    @staticmethod
    def load(src_ctx: Dict[str, Any]) -> Dict[str, Any]:
        return yaml.safe_load(**src_ctx)

    @staticmethod
    def dump(internal: Dict[str, Any]) -> str:
        return yaml.dump(**internal)


class XML:
    pass
