"""Класс Counter (Задание 8 средней сложности)."""


class Counter:
    """Класс-счётчик с поддержкой инкремента, декремента и сброса."""

    def __init__(self, initial: int = 0, step: int = 1):
        if step <= 0:
            raise ValueError("Шаг изменения должен быть положительным числом.")
        self._value = initial
        self._step = step

    @property
    def value(self) -> int:
        """Текущее значение счётчика."""
        return self._value

    def increment(self) -> int:
        """Увеличивает счётчик на величину шага."""
        self._value += self._step
        return self._value

    def decrement(self) -> int:
        """Уменьшает счётчик на величину шага."""
        self._value -= self._step
        return self._value

    def reset(self, new_value: int = 0) -> None:
        """Сбрасывает счётчик к заданному значению."""
        self._value = new_value
