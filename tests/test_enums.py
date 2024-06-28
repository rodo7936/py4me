import unittest
from py4me.enums import Locale, Plan, Currency, AddressLabel


class TestEnums(unittest.TestCase):
    def test_locale(self):
        self.assertEqual(Locale('en-US'), Locale.enUS)

    def test_plan(self):
        self.assertEqual(Plan('basic'), Plan.basic)

    def test_currency(self):
        self.assertEqual(Currency('usd'), Currency.usd)

    def test_address_label(self):
        self.assertEqual(AddressLabel('home'), AddressLabel.home)


if __name__ == '__main__':
    unittest.main()