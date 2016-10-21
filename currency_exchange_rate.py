import datetime
from period import Period
from fixer_io_exchange_rates import FixerIOExchangeRates
from exchange_rate import ExchangeRate

class AverageCurrencyExchangeRates:
    """
    Count average of rates base currency to exchange currency in time period.

    :param ExchangeRatesAPI

    :rtype: None:
    """

    def __init__(self, exchange_api):
        self._exchange_api = exchange_api

    def average_rate_in_period(self, base_currency, exchange_currency, period):
        """
        Count average of rates in time period.

        :param  str base_currency       : Base currency code
        :param  str exchange_currency   : Exchange currency code
        :param  str period              : Period of time

        :rtype: ExchangeRate
        """

        list_of_dates = period.dates()
        rates_sum = ExchangeRate(base_currency, exchange_currency, 0.0)
        for day in list_of_dates:
            rates_sum += self._exchange_api.rate_for_date(base_currency, exchange_currency, day)
        return rates_sum / len(list_of_dates)

def main():
    period = Period(datetime.date(2016, 7, 1), datetime.date(2016, 7, 10))
    api = FixerIOExchangeRates()
    average_currency_exchange_rates = AverageCurrencyExchangeRates(api)
    x = average_currency_exchange_rates.average_rate_in_period('EUR','USD', period)
    print(x)
#main()