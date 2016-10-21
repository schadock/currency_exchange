import unittest
import datetime
from period import Period
from currency_exchange_rate import AverageCurrencyExchangeRates
from exchange_rate import ExchangeRate
from tests.support.fake_currency_exchange_api import FakeCurrencyExchangeAPI

class AverageCurrencyExchangeRatesTest(unittest.TestCase):
    """

    """
    def setUp(self):
        self.base_currency = 'EUR'
        self.exchange_currency = 'USD'
        self.rates_average = 1.5

    def test_average_rate_in_period(self):
        """
        Test correct counting average rate in period
        """

        period = Period(datetime.date(2016, 7, 1), datetime.date(2016, 7, 4))
        fake_api = FakeCurrencyExchangeAPI()
        average_exchange_rates = AverageCurrencyExchangeRates(fake_api)
        average_rate = average_exchange_rates.average_rate_in_period('EUR', 'USD', period)
        expected_rate = ExchangeRate('EUR', 'USD', 1.5)
        self.assertEquals(average_rate, expected_rate)