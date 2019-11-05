import unittest
from strcalculator import StrCalculator

class TestStrCalculator(unittest.TestCase):

    def test_an_empty_arg_return_0(self):
        self.assertEqual(StrCalculator('').add, 0)

    def test_an_integer_will_return_an_error(self):
        with self.assertRaises(ValueError):
            StrCalculator(7)

    def test_1_will_return_1(self):
        self.assertEqual(StrCalculator('1').add, 1)

    def test_add_two_numbers(self):
        self.assertEqual(StrCalculator('1, 2, 4').add, 7)
        self.assertEqual(StrCalculator('43, 32').add, 75)
        self.assertEqual(StrCalculator('103, 2').add, 105)

    def test_can_handle_new_lines_betweem(self):
        self.assertEqual(StrCalculator('1\n2\n3').add, 6)
        self.assertEqual(StrCalculator('41\n12\n3').add, 56)

    def test_can_support_different_delimeters(self):
        self.assertEqual(StrCalculator('//;\n1;2').add, 3)
        self.assertEqual(StrCalculator('//+\n1+10').add, 11)
        self.assertEqual(StrCalculator('//a20560bc\n1abc2abc3').add, 6)

    def test_negative_numbers_raise_error(self):
        with self.assertRaises(ValueError):
            StrCalculator('3, 4, -1').add

        with self.assertRaises(ValueError):
            StrCalculator('-1, 4, -1').add

    def test_ignore_big_numbers(self):
        self.assertEqual(StrCalculator('1000, 1003, 3, 1').add, 4)
        self.assertEqual(StrCalculator('1001, 2').add, 2)
