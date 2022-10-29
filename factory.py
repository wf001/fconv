import json
from abc import ABCMeta, abstractmethod


class IFormat(metaclass=ABCMeta):
    @abstractmethod
    def load(self):
        raise Exception()

    @abstractmethod
    def parse(self):
        raise Exception()


class Json(IFormat):
    def load(self, df):
        with open('assets/sample01.json') as f:
            df = json.load(f)
        return df

    def parse(self):
        pass


class Yaml(IFormat):
    def load(self):
        pass

    def parse(self):
        pass


class Former:
    def __init__(self, src, target):
        self.src = src
        self.target = target
        self.data = None

    def former(self):
        self._get_input()
        self._to_dict()
        self._from_dict()
        self._send_output()

    def _to_dict(self):
        self.data = self.src().load()

    def _from_dict(self):
        self.data = self.target().dump()

    @staticmethod
    def _get_input():
        pass

    @staticmethod
    def _send_output():
        pass


if __name__ == '__main__':
    f = Former(Json, Json)
    f._to_dict()
    print(f.data)
