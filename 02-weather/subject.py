from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from observer import Observer


class Subject(object):
    def __init__(self):
        self.observers = []

    def register_observer(self, new_observer: "Observer") -> None:
        self.observers.append(new_observer)

    def remove_object(self, observer: "Observer") -> None:
        if observer in self.observers:
            self.observers.remove(observer)
        else:
            raise KeyError

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.update()
