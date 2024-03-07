import unittest
from Calculate import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_string(self):  # empty string
        #Given
        txt = ""
        #When
        result = self.calculator.Calculate(txt)
        #Then
        self.assertEqual(result, 0)

    def test_single_number(self):  # single number
        #Given
        txt = "5"
        #When
        result = self.calculator.Calculate(txt)
        #Then
        self.assertEqual(result, 5)

    def test_two_numbers_comma(self):  # two numbers, comma delimited
        #Given:
        txt = "7,3"
        #When:
        result = self.calculator.Calculate(txt)
        #Then:
        self.assertEqual(result, 10)

    def test_two_numbers_newline(self):  # two numbers, newline delimited
        #Given:
        txt = "4\n6"
        #When:
        result = self.calculator.Calculate(txt)
        #Then:
        self.assertEqual(result, 10)

    def test_three_numbers_any_delimiter(self):  # three numbers, delimited either way
        #Given:
        txt = "2,3,5"
        #When:
        result = self.calculator.Calculate(txt)
        #Then:
        self.assertEqual(result, 10)
        #Given:
        txt = "1\n2\n3"
        # When:
        result = self.calculator.Calculate(txt)
        # Then:
        self.assertEqual(result, 6)

    def test_negative_numbers(self):  # negative numbers throw an exception
        #Given:
        txt = "-1,2,-3"
        #Then:
        with self.assertRaises(ValueError):
            self.calculator.Calculate(txt)

    def test_ignore_numbers_greater_than_1000(self):  # numbers greater than 1000 are ignored
        #Given:
        txt = "2,1001,6"
        #When:
        result = self.calculator.Calculate(txt)
        #Then:
        self.assertEqual(result, 8)

    def test_single_char_delimiter(self):  # single char delimiter defined on the first line
        #Given:
        txt = "//;\n1;2;3"
        #When:
        result = self.calculator.Calculate(txt)
        #Then:
        self.assertEqual(result, 6)

    def test_multi_char_delimiter(self):  # multi char delimiter defined on the first line
        #Given:
        txt = "//[###]\n1###2###3"
        #When:
        result = self.calculator.Calculate(txt)
        #Then:
        self.assertEqual(result, 6)

    def test_many_delimiters(self):  # many single or multi-char delimiters defined
        #Given:
        txt = "//[;][%]\n1;2%3"
        #When:
        result = self.calculator.Calculate(txt)
        #Then:
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
