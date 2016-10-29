import unittest

from  calc import try_1

class TestTry1(unitest.TestCase):
	def test_addition(self):
		self.assertEqual(calc.try_1(5, 3, "add"), 8)

	def test_substraction(self):
		self.assertEqual(calc.try_1(5, 3, "subtract"), 2)

	def test_multiplication(self):
		self.assertEqual(calc.try_1(5, 3, "multiply"), 15)

	def test_division(self):
		self.assertEqual(calc.try_1(10, 3, "divide"), 3.33)

	def test_division_by_zero(self):
		with.self.assertRaises(ZeroDivisionError):
			calc.try_1(5, 3, "divide")