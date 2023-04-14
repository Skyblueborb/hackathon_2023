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
    def test_calculate(self):
        self.assertAlmostEqual(currency.calculate(100, 1000), 0.1*currency.CURRENT_PAY, delta=0.001)
        self.assertAlmostEqual(currency.calculate(50, 100), 0.5*currency.CURRENT_PAY, delta=0.001)
        self.assertAlmostEqual(currency.calculate(10000, currency.factor(1969)), round((10000/26088)*currency.CURRENT_PAY, 2), delta=0.001)
    def test_polishify(self):
        self.assertEqual(currency.polishify(5.5), "5,5")