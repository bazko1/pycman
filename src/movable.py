from abc import ABCMeta, abstractmethod
from .field import Field

class Movable(Field, metaclass=ABCMeta):
    def __init__(self):
        pass
    @abstractmethod
    def step(self):
        pass