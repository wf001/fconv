from abc import ABC, abstractmethod
from typing import Any, Dict


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
    def get_load_kwargs(self, src_ctx: str, opt: Dict[str, Any]):
        _opt = opt if opt else {}
        _opt[self.load_data_key] = src_ctx
        return _opt

    def get_dump_kwargs(self, internal: Dict[str, Any], opt: Dict[str, Any]):
        _opt = opt if opt else {}
        _opt[self.dump_data_key] = internal
        return _opt


class XML:
    pass
