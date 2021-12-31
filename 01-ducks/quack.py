from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self) -> str:
        raise NotImplementedError


class Quack(QuackBehavior):
    def quack(self) -> str:
        return 'Кря!'


class Squeak(QuackBehavior):
    def quack(self) -> str:
        return 'Резиновая утка пищит'


class MuteQuack(QuackBehavior):
    def quack(self) -> str:
        return 'Не издаёт ни звука'
