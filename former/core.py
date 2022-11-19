import typing as t
from typing import Any, Dict

from .format import AbstractFormat


class Former:
    def __init__(
        self,
        src_format,
        target_format,
        src_path: t.Optional[str] = "",
        target_path: t.Optional[str] = "",
        in_opt: t.Optional[Dict[str, Any]] = None,
        out_opt: t.Optional[Dict[str, Any]] = None,
    ):
        # TODO: self.src = src_Dict[str,Any][input_format]
        self._src_format = src_format
        self._target_format = target_format

        if not self.is_valid_format:
            raise ValueError(
                f"Invalid format. expect: {AbstractFormat._get_valid_format()}"
            )

        self.src_path = src_path
        self.target_path = target_path
        self.in_opt = in_opt
        self.out_opt = out_opt

    @property
    def is_valid_format(self) -> bool:
        return issubclass(self._src_format, AbstractFormat) and issubclass(
            self._target_format, AbstractFormat
        )

    def form(self, src_ctx: str = "") -> str:
        if self.src_path and not src_ctx:
            src_ctx = self._read_file(self.src_path)

        target_ctx = self._from_internal(
            self._to_internal(src_ctx, self.in_opt), self.out_opt
        )

        if self.target_path:
            self._write_file(target_ctx, self.target_path)

        return target_ctx

    def _to_internal(self, ctx: str, opt: t.Optional[Dict[str, Any]]) -> Any:
        _s = self._src_format()
        return _s.load(_s.gen_input_kwargs(ctx, opt))

    def _from_internal(self, internal: Any, opt: t.Optional[Dict[str, Any]]) -> str:
        _t = self._target_format()
        return _t.dump(_t.gen_output_kwargs(internal, opt))

    @staticmethod
    def _read_file(fname: str) -> str:
        with open(fname) as f:
            return f.read()

    @staticmethod
    def _write_file(ctx: str, fname: str) -> None:
        f = open(fname, "x+")
        f.write(ctx)
