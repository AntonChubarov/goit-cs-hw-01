import unittest
from interpreter import Lexer, Parser, Interpreter, LexicalError, ParsingError


def evaluate_expression(expression):
    lexer = Lexer(expression)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    return interpreter.interpret()


class TestInterpreter(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(evaluate_expression("2 + 3"), 5)

    def test_subtraction(self):
        self.assertEqual(evaluate_expression("5 - 2"), 3)

    def test_multiplication(self):
        self.assertEqual(evaluate_expression("4 * 3"), 12)

    def test_division(self):
        self.assertEqual(evaluate_expression("8 / 2"), 4)

    def test_precedence(self):
        self.assertEqual(evaluate_expression("2 + 3 * 4"), 14)

    def test_parentheses(self):
        self.assertEqual(evaluate_expression("(2 + 3) * 4"), 20)

    def test_complex_expression(self):
        self.assertEqual(evaluate_expression("7 + 3 * (10 / (12 / (3 + 1) - 1))"), 22)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate_expression("10 / (5 - 5)")

    def test_invalid_token(self):
        with self.assertRaises(LexicalError):
            evaluate_expression("2 + $")

    def test_mismatched_parentheses(self):
        with self.assertRaises(ParsingError):
            evaluate_expression("(3 + 5")


if __name__ == "__main__":
    unittest.main()
