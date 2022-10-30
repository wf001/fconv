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


class Json(IFormat):
    def load(self, str: str) -> dict:
        res = json.loads(str)
        return res

    def parse(self):
        pass


class Yaml(IFormat):
    def load(self):
        pass

    def parse(self, data: dict) -> str:
        return yaml.dump(data, Dumper=yaml.CDumper)


class Former:
    def __init__(self, src, src_path, target, target_path):
        self.src = src
        self.src_path = src_path
        self.target = target
        self.target_path = target_path
        self.data = None
        self.df = None

    def former(self):
        self._get_input(self.src_path)
        self._to_dict()
        self._from_dict()
        self._send_output(self.target_path)

    def _to_dict(self):
        self.data = self.src().load(self.df)

    def _from_dict(self):
        self.data = self.target().parse(self.data)

    def _get_input(self, file: str) -> None:
        with open(file) as f:
            self.df = f.read()

    def _send_output(self, file: str) -> None:
        f = open(file, 'x+')
        f.write(self.data)


if __name__ == '__main__':
    in_name = 'assets/sample01.json'
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    out_name = f'assets/result-{dt}.yaml'
    f = Former(Json, in_name, Yaml, out_name)
    f.former()
