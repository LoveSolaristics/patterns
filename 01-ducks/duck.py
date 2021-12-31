from fly import FlyBehavior, FlyNoWay, FlyWithWings
from quack import QuackBehavior, Quack, Squeak


class Duck(object):
    def __init__(
            self,
            fly_behavior: "FlyBehavior",
            quack_behavior: "QuackBehavior"
    ):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_quack(self) -> str:
        return self.quack_behavior.quack()

    def perform_fly(self) -> str:
        return self.fly_behavior.fly()


class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())


class RedheadDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())


class RubberDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Squeak())


class DecoyDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Quack())
