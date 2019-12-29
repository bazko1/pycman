from abc import ..

class Movable(metaclass=ABCMeta, Field):
    @abstractmethod
    def step(self):
        pass