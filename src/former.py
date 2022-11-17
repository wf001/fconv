import json
import yaml
from abc import ABC, abstractmethod
import typing as t


class AbstractFormat(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def dump(self):
        pass


class Format:

    class Json(AbstractFormat):
        def __init__(self, **kwargs):
            # load opt
            self.cls = kwargs.get('cls', None)
            self.object_hook = kwargs.get('object_hook', None)
            self.parse_float = kwargs.get('parse_float', None)
            self.parse_int = kwargs.get('parse_int', None)
            self.parse_constant = kwargs.get('parse_constant', None)
            self.object_pairs_hook = kwargs.get(
                'object_pairs_hook', None)
            # dump opt
            self.skipkeys = kwargs.get('skipkeys', False)
            self.ensure_ascii = kwargs.get('ensure_ascii', True)
            self.check_circular = kwargs.get('check_circular', True)
            self.allow_nan = kwargs.get('allow_nan', True)
            self.cls = kwargs.get('cls', None)
            self.indent = kwargs.get('indent', None)
            self.separators = kwargs.get('separators', None)
            self.default = kwargs.get('default', None)
            self.sort_keys = kwargs.get('sort_keys', False)

        def load(self, src_ctx: str) -> dict:
            return json.loads(
                src_ctx,
                cls=self.cls,
                object_hook=self.object_hook,
                parse_float=self.parse_float,
                parse_int=self.parse_int,
                parse_constant=self.parse_constant,
                object_pairs_hook=self.object_pairs_hook
            )

        def dump(self, internal: dict) -> str:
            return json.dumps(
                internal,
                skipkeys=self.skipkeys,
                ensure_ascii=self.ensure_ascii,
                check_circular=self.check_circular,
                allow_nan=self.allow_nan,
                cls=self.cls,
                indent=self.indent,
                separators=self.separators,
                default=self.default,
                sort_keys=self.sort_keys
            )

    class Yaml(AbstractFormat):
        def load(self, str: str) -> dict:
            return yaml.safe_load(str)

        def dump(self, internal: dict) -> str:
            return yaml.dump(internal, Dumper=yaml.CDumper)

    class XML():
        pass


class Former:
    def __init__(
            self,
            src_format: object = None,
            target_format: object = None,
            src_path: t.Optional[str] = None,
            target_path: t.Optional[str] = None
    ):
        # TODO: self.src = src_dict[input_format]
        self._src_format = src_format
        self._target_format = target_format

        if not self.is_valid_format:
            raise Exception

        self.src_path = src_path
        self.target_path = target_path

    @property
    def is_valid_format(self):
        return issubclass(self._src_format, AbstractFormat) and \
            issubclass(self._target_format, AbstractFormat)

    def form(self, src_ctx: str = None) -> str:
        if self.src_path and not src_ctx:
            src_ctx = self._get_input(self.src_path)

        target_ctx = self._from_internal(self._to_internal(src_ctx))

        if self.target_path:
            self._send_output(target_ctx, self.target_path)

        return target_ctx

    @staticmethod
    def _get_input(fname: str) -> str:
        with open(fname) as f:
            return f.read()

    def _to_internal(self, ctx: str) -> t.Any:
        return self._src_format().load(ctx)

    def _from_internal(self, internal: t.Any) -> str:
        return self._target_format().dump(internal)

    @staticmethod
    def _send_output(ctx: str, fname: str) -> None:
        f = open(fname, 'x+')
        f.write(ctx)


if __name__ == '__main__':
    pass
