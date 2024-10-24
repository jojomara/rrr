import unittest
from tax_calculator import calculate_tax

class TestTaxCalculator(unittest.TestCase):

    def test_no_tax_for_low_income(self):
        self.assertEqual(calculate_tax(11000), 0)

    def test_twenty_percent_tax(self):
        # Earnings between 12,000 and 36,000
        self.assertEqual(calculate_tax(20000), 1600)  # 20% on 8000

def test_forty_percent_tax(self):
    # Earnings above 36,000
    self.assertEqual(calculate_tax(40000), 6400)  # 20% on 24,000 and 40% on 4000


    def test_forty_percent_tax(self):
        # Earnings above 36,000
        self.assertEqual(calculate_tax(40000), 6800)  # 20% on 24,000 and 40% on 4000

if __name__ == '__main__':
    unittest.main()
