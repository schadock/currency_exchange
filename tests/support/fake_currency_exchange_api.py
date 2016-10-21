import datetime
from exchange_rate import ExchangeRate

class FakeCurrencyExchangeAPI:
    """
    Fake class for counting average rating in period.
    """

    def rate_for_date(self, base_currency, exchange_currency, date_of_exchange):
        """
        Return currency rate for dates.

        :param   str      base_currency     : Base currency code
        :param   str      exchange_currency : Exchange currency code
        :param   datetime date_of_exchange  :

        :return: ExchangeRate
        """
        if date_of_exchange == datetime.date(2016, 7, 1):
            exchange_rate = 1.4
            rate_day = ExchangeRate(base_currency, exchange_currency, exchange_rate)
            return rate_day
        elif date_of_exchange == datetime.date(2016, 7, 2):
            exchange_rate = 1.5
            rate_day = ExchangeRate(base_currency, exchange_currency, exchange_rate)
            return rate_day
        elif date_of_exchange == datetime.date(2016, 7, 3):
            exchange_rate = 1.6
            rate_day = ExchangeRate(base_currency, exchange_currency, exchange_rate)
            return rate_day
        else:
            exchange_rate = 0
            rate_day = ExchangeRate(base_currency, exchange_currency, exchange_rate)
            return rate_day