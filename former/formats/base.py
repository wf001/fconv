from abc import ABC, abstractmethod
from typing import Any, Dict

from .constants import const


class AbstractFormat(ABC):
    """Interface for implementing format"""

    def __init__(self, format: str):
        self.load_data_key = const[format].get("LOAD_DATA_KEY", "") if format else ""
        self.dump_data_key = const[format].get("DUMP_DATA_KEY", "") if format else ""

    @abstractmethod
    def load(self, src_ctx: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError()

    @abstractmethod
    def dump(self, internal: Dict[str, Any]) -> str:
        raise NotImplementedError()

    @classmethod
    def _get_valid_format(cls):
        return list(map(lambda x: x.__name__, cls.__subclasses__()))


class BaseFormat(AbstractFormat):
    """Base class for implementing format"""

    def get_load_kwargs(self, src_ctx: str, opt: Dict[str, Any]) -> Dict[str, Any]:
        _opt = opt if opt else {}
        _opt[self.load_data_key] = src_ctx
        return _opt

    def get_dump_kwargs(self, internal: Dict[str, Any], opt: Dict[str, Any]):
        _opt = opt if opt else {}
        _opt[self.dump_data_key] = internal
        return _opt


class XML:
    pass
