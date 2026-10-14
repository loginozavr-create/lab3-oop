"""Класс CountdownIterator (Задание 10 средней сложности)."""


class CountdownIterator:
    """Итератор обратного отсчёта от start до stop с заданным шагом."""

    def __init__(self, start: int, stop: int = 0, step: int = 1):
        if step <= 0:
            raise ValueError("Шаг итератора должен быть строго больше нуля.")
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current <= self.stop:
            raise StopIteration
        val = self.current
        self.current -= self.step
        return val
