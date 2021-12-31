from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self) -> str:
        raise NotImplementedError


class FlyWithWings(FlyBehavior):
    def fly(self) -> str:
        return 'Летает с помощью крыльев'


class FlyNoWay(FlyBehavior):
    def fly(self) -> str:
        return 'Не летает'
