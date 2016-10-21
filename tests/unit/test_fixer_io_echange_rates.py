import unittest
import datetime
from fixer_io_exchange_rates import FixerIOExchangeRates
from exchange_rate import ExchangeRate
from tests.support.mock_fixed_io_api import get_rate_date_in_json

class FixerIOExchangeRatesTest(unittest.TestCase):
    """
    Test class FixerIOExchangeRates if it get correct data from API.
    """
    def date_to_string(self, date_in_date_time):

        date_in_string = date_in_date_time.strftime("%Y-%m-%d")
        return date_in_string

    def test_get_correct_rate_for_date(self):
        """
        Check correction of get day rate at the date.
        """
        base_currency = 'EUR'
        exchange_currency = 'USD'
        date_of_exchange = datetime.date(2016,7,1)
        rate = 1.5
        get_rate_date_in_json(base_currency, exchange_currency, self.date_to_string(date_of_exchange), rate)
        FixerIOExchangeRates.EXCHANGE_RATES_API_URL = 'http://localhost:31000/mockhttp/ex/'
        exchange_rate = FixerIOExchangeRates().rate_for_date(base_currency, exchange_currency, date_of_exchange)
        expected_rate = ExchangeRate(base_currency, exchange_currency, rate)

        self.assertEquals(exchange_rate, expected_rate)