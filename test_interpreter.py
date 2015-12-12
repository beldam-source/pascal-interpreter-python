#! /usr/bin/env python3

import unittest
from interpreter_main import Token, Interpreter, INTEGER, PLUS, EOF
from interpreter_from_scratch import InterpreterEP, TokenEP, INT


class InterpreterAdditionTestCase(unittest.TestCase):

    def test_single_digit_addition_no_whitespace(self):
        self.interpreter = Interpreter("1+1")
        result = self.interpreter.expr()
        self.assertEqual(result, 2)

    def test_integer_single_digit(self):
        self.interpreter = Interpreter("1")
        one = self.interpreter.integer()
        self.assertEqual(one, 1)

    def test_integer_double_digit(self):
        self.interpreter = Interpreter("12")
        twelve = self.interpreter.integer()
        self.assertEqual(twelve, 12)

    def test_integer_multidigit_plus_digit(self):
        self.interpreter = Interpreter("123+4")
        one = self.interpreter.integer()
        self.assertEqual(one, 123)


class InterpreterSubtractionTestCase(unittest.TestCase):

    def test_subtraction(self):
        self.interpreter = Interpreter("13 - 12")
        result = self.interpreter.expr()
        self.assertEqual(result, 1)


class InterpreterMultiplicationTestCase(unittest.TestCase):
    def test_multiplication(self):
        self.interpreter = Interpreter("2 * 3")
        result = self.interpreter.expr()
        self.assertEqual(result, 6)


class InterpreterFloorDivisionTestCase(unittest.TestCase):
    def test_floor_division_no_truncation(self):
        self.interpreter = Interpreter("4 / 2")
        result = self.interpreter.expr()
        self.assertEqual(result, 2)

    def test_floor_division_with_truncated_result(self):
        self.interpreter = Interpreter("3 / 2")
        result = self.interpreter.expr()
        self.assertEqual(result, 1)


class InterpreterLongExpressionTestCase(unittest.TestCase):
    def test_three_term_expression(self):
        self.interpreter = Interpreter("1 + 5 / 2")
        result = self.interpreter.expr()
        self.assertEqual(result, 3)


class TokenTestCase(unittest.TestCase):
    def setUp(self):
        self.plus_token = Token(PLUS, '+')
        self.eof_token = Token(EOF, None)

    def tearDown(self):
        del self.plus_token
        del self.eof_token

    def test_can_add_two_integer_tokens(self):
        int_token1 = Token(INTEGER, 1)
        int_token2 = Token(INTEGER, 2)
        result = int_token1 + int_token2
        self.assertEqual(result.value, 12)


class InterpreterFromScratchTestCase(unittest.TestCase):
    def test_can_create_interpreter(self):
        txt = "2*3"
        self.interpreter = InterpreterEP(txt)
        self.assertEqual(self.interpreter.text, txt)

    @unittest.skip
    def test_expr_returns_same_input_if_integer(self):
        txt = "3"
        self.interpreter = InterpreterEP(txt)
        self.assertEqual(self.interpreter.expr(), int(txt))

    @unittest.skip
    def test_expr_multiplication(self):
        txt = "2*3"
        self.interpreter = InterpreterEP(txt)
        self.assertEqual(self.interpreter.expr(), eval(txt))

    def test_get_next_token_returns_token_of_current_char(self):
        txt = "12"
        self.interpreter = InterpreterEP(txt)
        token = self.interpreter.get_next_token()
        self.assertIsInstance(token, TokenEP)
        self.assertEqual(token.kind, INT)
        self.assertEqual(token.value, int(txt))

    def test_get_next_token_tokenizes_expression(self):
        txt = "6/2"
        self.interpreter = InterpreterEP(txt)
        tkn1 = self.interpreter.get_next_token()
        self.assertEqual(tkn1.value, 6)
        tkn2 = self.interpreter.get_next_token()
        self.assertEqual(tkn2.value, "/")
        tkn3 = self.interpreter.get_next_token()
        self.assertEqual(tkn3.value, 2)
        self.assertIsNone(self.interpreter.current_token)

    def test_expr_returns_single_int(self):
        txt = "12"
        self.interpreter = InterpreterEP(txt)
        result = self.interpreter.expr()
        self.assertEqual(result, int(txt))

    def test_expr_evaluates_simple_expression(self):
        txt = "6/2"
        self.interpreter = InterpreterEP(txt)
        result = self.interpreter.expr()
        self.assertEqual(result, eval(txt))

    def test_expr_evaluates_long_expression(self):
        txt = "160/2*30"
        self.interpreter = InterpreterEP(txt)
        result = self.interpreter.expr()
        self.assertEqual(result, eval(txt))
