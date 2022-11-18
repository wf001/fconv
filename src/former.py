import typing as t

from src.format import AbstractFormat


class Former:
    def __init__(
        self,
        src_format,
        target_format,
        src_path: t.Optional[str] = None,
        target_path: t.Optional[str] = None,
        in_opt: t.Optional[dict] = None,
        out_opt: t.Optional[dict] = None,
    ):
        # TODO: self.src = src_dict[input_format]
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

    def _to_internal(self, ctx: str, opt: t.Optional[dict]) -> t.Any:
        _s = self._src_format()
        ctx = _s._gen_input_kwargs(ctx, opt)
        return _s.load(ctx)

    def _from_internal(self, internal: t.Any, opt: t.Optional[dict]) -> str:
        _t = self._target_format()
        internal = _t._gen_output_kwargs(internal, opt)
        return _t.dump(internal)

    @staticmethod
    def _read_file(fname: str) -> str:
        with open(fname) as f:
            return f.read()

    @staticmethod
    def _write_file(ctx: str, fname: str) -> None:
        f = open(fname, "x+")
        f.write(ctx)


if __name__ == "__main__":
    pass
