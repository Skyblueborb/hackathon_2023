import unittest
import currency
class TestAddNumbers(unittest.TestCase):
    def test_numCleaner(self):
        self.assertEqual(currency.numCleaner("10"), 10.0)
        self.assertEqual(currency.numCleaner("10 000"), 10000.0)
        self.assertEqual(currency.numCleaner("10,0"), 10.0)
        self.assertEqual(currency.numCleaner("10 000,0"), 10000.0)
    def test_factor(self):
        self.assertEqual(currency.factor(1964), 21792.0)
        self.assertEqual(currency.factor(1969), 26088.0)
        self.assertEqual(currency.factor(1972), 30108.0)
    def test_polishify(self):
        self.assertEqual(currency.polishify(5.5), "5,50")
        self.assertEqual(currency.polishify(2.56), "2,56")
        self.assertEqual(currency.polishify(172.8), "172,80")
        self.assertEqual(currency.polishify(0.0), "0,00")