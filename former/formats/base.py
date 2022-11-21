from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class BaseFormat(ABC):
    """Base class for implementing all the format"""

    @abstractmethod
    def load(self, src_ctx: Any) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def dump(self, internal: Any) -> Optional[str]:
        raise NotImplementedError()


class BaseDictionalizeFormat(BaseFormat):
    """Base class for implementing format that can convert to/from dict"""

    def __init__(self, load_data_key: str = "", dump_data_key: str = ""):
        self.load_data_key = load_data_key
        self.dump_data_key = dump_data_key

    def get_load_kwargs(self, src_ctx: str, opt: Dict[str, Any]) -> Dict[str, Any]:
        _opt = opt if opt else {}
        _opt[self.load_data_key] = src_ctx
        return _opt

    def get_dump_kwargs(
        self, internal: Dict[str, Any], opt: Dict[str, Any]
    ) -> Dict[str, Any]:
        _opt = opt if opt else {}
        _opt[self.dump_data_key] = internal
        return _opt
