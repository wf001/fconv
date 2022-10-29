import json
import yaml
from abc import ABCMeta, abstractmethod


class IFormat(meta_class=ABCMeta):
    @abstractmethod
    def load(self):
        raise Exception()

    @abstractmethod
    def parse(self):
        raise Exception()


class Json(IFormat):
    def load(self):
        pass

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

    def former(self):
        self._get_input()
        self._to_dict()
        self._from_dict()
        self._send_output()

    def _to_dict(self):
        self.src.load()

    def _from_dict(self):
        self.target.dump()

    @staticmethod
    def _get_input():
        pass

    @staticmethod
    def _send_output(self):
        pass


if __name__ == '__main__':
    # Former().former()
    print(json.load)
