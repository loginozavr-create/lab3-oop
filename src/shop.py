"""Классы Product и Cart (Задание 3 повышенной сложности)."""

from typing import Dict


class Product:
    """Класс товара магазина."""

    def __init__(self, name: str, price: float):
        if price < 0:
            raise ValueError("Цена товара не может быть отрицательной.")
        self.name = name
        self.price = float(price)

    def __repr__(self) -> str:
        return f"Product(name='{self.name}', price={self.price})"


class Cart:
    """Класс корзины покупателя."""

    def __init__(self):
        self._items: Dict[str, dict] = {}

    def add_product(self, product: Product, quantity: int = 1) -> None:
        """Добавляет товар в корзину."""
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным числом.")

        if product.name in self._items:
            self._items[product.name]["quantity"] += quantity
        else:
            self._items[product.name] = {
                "product": product,
                "quantity": quantity,
            }

    def remove_product(self, product_name: str, quantity: int = 1) -> None:
        """Уменьшает количество товара или удаляет его из корзины."""
        if product_name not in self._items:
            raise KeyError(f"Товар '{product_name}' отсутствует в корзине.")
        if quantity <= 0:
            raise ValueError("Удаляемое количество должно быть положительным.")

        if self._items[product_name]["quantity"] <= quantity:
            del self._items[product_name]
        else:
            self._items[product_name]["quantity"] -= quantity

    def calculate_total(self) -> float:
        """Возвращает общую стоимость всех товаров в корзине."""
        total = sum(
            item["product"].price * item["quantity"]
            for item in self._items.values()
        )
        return round(total, 2)

    def get_items(self) -> Dict[str, dict]:
        """Возвращает словарь добавленных товаров."""
        return self._items.copy()
