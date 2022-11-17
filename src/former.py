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
        def load(self, src_ctx: str) -> dict:
            return json.loads(src_ctx)

        def dump(self, internal: dict) -> str:
            return json.dumps(internal, indent=1)

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
        self.src_path = src_path
        self.target_path = target_path

        if not self.is_valid_format:
            raise Exception

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
    def _get_input(file: str) -> str:
        with open(file) as f:
            ctx = f.read()
        return ctx

    def _to_internal(self, ctx: str) -> t.Any:
        return self._src_format().load(ctx)

    def _from_internal(self, internal: t.Any) -> str:
        return self._target_format().dump(internal)

    @staticmethod
    def _send_output(res: str, file: str) -> None:
        f = open(file, 'x+')
        f.write(res)


if __name__ == '__main__':
    pass
