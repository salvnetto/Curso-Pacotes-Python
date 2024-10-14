import unittest

from calculadora.soma import soma

class TestSoma(unittest.TestCase):
    def test_saudacao(self):
        self.assertEqual(soma(2, 2), 4)