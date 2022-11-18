from abc import ABC, abstractmethod
import typing as t
import json
import yaml


class AbstractFormat(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def dump(self):
        pass


class Format:

    class Json(AbstractFormat):

        def _gen_input_kwargs(self, ctx, opt):
            _opt = opt if opt else {}
            _opt['s'] = ctx
            return _opt

        def _gen_output_kwargs(self, ctx, opt):
            _opt = opt if opt else {}
            _opt['obj'] = ctx
            return _opt

        def load(self, src_ctx: dict) -> dict:
            return json.loads(**src_ctx)

        def dump(self, internal: dict) -> str:
            return json.dumps(**internal)

    class Yaml(AbstractFormat):

        def _gen_input_kwargs(self, ctx, opt):
            _opt = opt if opt else {}
            _opt['stream'] = ctx
            return _opt

        def _gen_output_kwargs(self, ctx, opt):
            _opt = opt if opt else {}
            _opt['data'] = ctx
            _opt['Dumper'] = yaml.CDumper
            print(_opt)
            return _opt

        def load(self, ctx: dict) -> dict:
            return yaml.safe_load(**ctx)

        def dump(self, internal: dict) -> str:
            return yaml.dump(**internal)

    class XML():
        pass


class Former:
    def __init__(
            self,
            src_format: object = None,
            target_format: object = None,
            src_path: t.Optional[str] = None,
            target_path: t.Optional[str] = None,
            in_opt: t.Optional[dict] = None,
            out_opt: t.Optional[dict] = None
    ):
        # TODO: self.src = src_dict[input_format]
        self._src_format = src_format
        self._target_format = target_format

        if not self.is_valid_format:
            raise ValueError('Invalid format. expect: [JSON, YAML]')

        self.src_path = src_path
        self.target_path = target_path
        self.in_opt = in_opt
        self.out_opt = out_opt

    @property
    def is_valid_format(self):
        return issubclass(self._src_format, AbstractFormat) and \
            issubclass(self._target_format, AbstractFormat)

    def form(self, src_ctx: str = None) -> str:
        if self.src_path and not src_ctx:
            src_ctx = self._get_input(self.src_path)

        target_ctx = self._from_internal(
            self._to_internal(src_ctx, self.in_opt),
            self.out_opt
        )

        if self.target_path:
            self._send_output(target_ctx, self.target_path)

        return target_ctx

    @staticmethod
    def _get_input(fname: str) -> str:
        with open(fname) as f:
            return f.read()

    def _to_internal(self, ctx: str, opt: dict) -> t.Any:
        _s = self._src_format()
        ctx = _s._gen_input_kwargs(ctx, opt)
        return _s.load(ctx)

    def _from_internal(self, internal: t.Any, opt: dict) -> str:
        _t = self._target_format()
        internal = _t._gen_output_kwargs(internal, opt)
        return _t.dump(internal)

    @staticmethod
    def _send_output(ctx: str, fname: str) -> None:
        f = open(fname, 'x+')
        f.write(ctx)


if __name__ == '__main__':
    pass
