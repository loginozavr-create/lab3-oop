"""Класс Student (Задание 2 средней сложности)."""


class Student:
    """Класс, представляющий студента."""

    def __init__(self, full_name: str, group: str, gpa: float = 0.0):
        self.full_name = full_name
        self.group = group
        self.gpa = gpa

    def get_info(self) -> str:
        """Возвращает строку с подробной информацией о студенте."""
        return (
            f"Студент: {self.full_name} | "
            f"Группа: {self.group} | "
            f"Средний балл: {self.gpa:.2f}"
        )

    def __str__(self) -> str:
        return self.get_info()
