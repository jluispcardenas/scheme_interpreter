import unittest
from scheme_interpreter.primitives import Primitives
from scheme_interpreter.parse import Parse
from scheme_interpreter.enviroment import Environment
from scheme_interpreter.scheme import Scheme
from scheme_interpreter.utils import *

class Tests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Tests, self).__init__(*args, **kwargs)
        Primitives.install()

    def test_sum(self):
        self.assertEqual(self.execute("(+ 4 3)"), "7", "Should be 7")

    def test_car(self):
        self.assertEqual(self.execute("(car '(a b c))"), "a", "Should be a")

    def test_cdr(self):
        self.assertEqual(self.execute("(cdr '(a b c))"), "(b, c)", "Should be (b, c)")

    def test_list(self):
        self.assertEqual(self.execute("'(a b c)"), "(a, b, c)", "Should be (a, b, c)")

    def test_lambda(self):
        self.assertEqual(self.execute("(apply + (list 1 2 3 4))"), "10", "Should be 10")

    def test_equal(self):
        self.assertEqual(self.execute("(equal? 2 2)"), "True", "Should be True")

    def test_if(self):
        self.assertEqual(self.execute("(if (equal? 2 2) 2 3)"), "2", "Should be 2")

    def test_length(self):
        self.assertEqual(self.execute("(length '(2 2))"), "2", "Should be 2")


    def execute(self, exp):
        parsed = Parse.parse(exp)
        env = Environment([], [], None)

        result = Scheme.evaluate(parsed, env)

        return Utils.stringtify(result)

if __name__ == '__main__':
    unittest.main(verbosity=2)
