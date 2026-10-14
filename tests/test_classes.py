"""Модульные тесты для проверки классов (TDD)."""

import unittest
from src.student import Student
from src.counter import Counter
from src.iterator import CountdownIterator
from src.shop import Product, Cart


class TestStudent(unittest.TestCase):
    def test_student_info(self):
        st = Student("Логинов Степан Игоревич", "220042-11", 4.8)
        self.assertIn("Логинов Степан Игоревич", st.get_info())
        self.assertIn("220042-11", st.get_info())
        self.assertIn("4.80", st.get_info())


class TestCounter(unittest.TestCase):
    def test_increment_and_decrement(self):
        cnt = Counter(initial=5, step=2)
        self.assertEqual(cnt.increment(), 7)
        self.assertEqual(cnt.decrement(), 5)

    def test_reset(self):
        cnt = Counter(initial=10)
        cnt.reset(0)
        self.assertEqual(cnt.value, 0)

    def test_invalid_step(self):
        with self.assertRaises(ValueError):
            Counter(step=0)


class TestCountdownIterator(unittest.TestCase):
    def test_iteration(self):
        it = CountdownIterator(start=5, stop=2, step=1)
        self.assertEqual(list(it), [5, 4, 3])

    def test_empty_range(self):
        it = CountdownIterator(start=2, stop=5)
        self.assertEqual(list(it), [])


class TestOrderSystem(unittest.TestCase):
    def setUp(self):
        self.bread = Product("Хлеб", 45.0)
        self.milk = Product("Молоко", 80.5)
        self.cart = Cart()

    def test_cart_total(self):
        self.cart.add_product(self.bread, 2)
        self.cart.add_product(self.milk, 1)
        self.assertEqual(self.cart.calculate_total(), 170.5)

    def test_cart_removal(self):
        self.cart.add_product(self.bread, 3)
        self.cart.remove_product("Хлеб", 1)
        self.assertEqual(self.cart.calculate_total(), 90.0)
        self.cart.remove_product("Хлеб", 2)
        self.assertEqual(self.cart.calculate_total(), 0.0)

    def test_invalid_product_price(self):
        with self.assertRaises(ValueError):
            Product("Брак", -10.0)


if __name__ == "__main__":
    unittest.main()
