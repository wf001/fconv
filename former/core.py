import typing as t
from typing import Any, Dict

from former.formats import get_supported_formats
from former.formats.base import BaseFormat
from former.util import Logger, logg


class Former:
    @logg
    def __init__(
        self,
        src_format,
        target_format,
        src_path: t.Optional[str] = "",
        target_path: t.Optional[str] = "",
        in_opt: t.Optional[Dict[str, Any]] = None,
        out_opt: t.Optional[Dict[str, Any]] = None,
    ):

        self._src_format = src_format
        self._target_format = target_format

        if not self.is_valid_format:
            raise ValueError(f"Invalid format. expect: {get_supported_formats()}")

        self.src_path = src_path
        self.target_path = target_path
        self.in_opt = in_opt
        self.out_opt = out_opt

    def __repr__(self):
        return f"{self.__class__.__module__}, {self.__dict__}"

    # move to Abstract class or utility
    @property
    def is_valid_format(self) -> bool:
        return issubclass(self._src_format, BaseFormat) and issubclass(
            self._target_format, BaseFormat
        )

    @logg
    def form(self, src_ctx: str = "") -> str:
        log = Logger().logger
        log.debug(f"{self=}")
        if self.src_path and not src_ctx:
            src_ctx = self._read_file(self.src_path)

        target_ctx = self._parse_from_internal(
            self._parse_to_internal(src_ctx, self.in_opt), self.out_opt
        )

        if self.target_path:
            self._write_file(target_ctx, self.target_path)

        return target_ctx

    def _parse_to_internal(self, ctx: str, opt: t.Optional[Dict[str, Any]]) -> Any:
        """
        1. Combine  ctx(raw input) and option passed by client.
        2. Convert them into dictionary.
        """
        src_format = self._src_format()
        return src_format.load(src_format.get_load_kwargs(ctx, opt))

    def _parse_from_internal(
        self, internal: Any, opt: t.Optional[Dict[str, Any]]
    ) -> str:
        """
        1. Combine  intrernal(dictionary converted by load function) and
        option passed by client.
        2. Convert them into string.
        """
        target_format = self._target_format()
        return target_format.dump(target_format.get_dump_kwargs(internal, opt))

    @staticmethod
    def _read_file(fname: str) -> str:
        with open(fname) as f:
            return f.read()

    @staticmethod
    def _write_file(ctx: str, fname: str) -> None:
        f = open(fname, "x+")
        f.write(ctx)
