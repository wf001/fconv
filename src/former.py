import json
import yaml
import datetime
from abc import ABCMeta, abstractmethod


class IFormat(metaclass=ABCMeta):
    @abstractmethod
    def load(self):
        raise Exception()

    @abstractmethod
    def parse(self):
        raise Exception()


class Format:

    class Json(IFormat):
        def load(self, str: str) -> dict:
            res = json.loads(str)
            return res

        def parse(self, data: dict) -> str:
            res = json.dumps(data, indent=1)
            return res

    class Yaml(IFormat):
        def load(self, str: str) -> dict:
            return yaml.safe_load(str)

        def parse(self, data: dict) -> str:
            return yaml.dump(data, Dumper=yaml.CDumper)


class Former:
    def __init__(
            self,
            src,
            target,
            context=None,
            src_path=None,
            target_path=None
    ):
        # TODO: self.src = src_dict[input_format]
        self.src = src()
        self.target = target()
        self.src_path = src_path
        self.target_path = target_path

    def form(self) -> str:
        if self.src_path:
            ctx = self._get_input(self.src_path)

        res = self._to_dict(ctx)
        res = self._from_dict(res)

        if self.target_path:
            self._send_output(res, self.target_path)

        return res

    def _get_input(self, file: str) -> str:
        with open(file) as f:
            ctx = f.read()
        return ctx

    def _to_dict(self, ctx: str) -> dict:
        return self.src.load(ctx)

    def _from_dict(self, res: dict) -> str:
        return self.target.parse(res)

    def _send_output(self, res: str, file: str) -> None:
        f = open(file, 'x+')
        f.write(res)


if __name__ == '__main__':
    pass
