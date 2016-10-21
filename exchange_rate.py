class ExchangeRate:
    """
    Class contains base currency, exchange currency and counted rates average from period.

    :param str base_currency       : Base currency code
    :param str exchange_currency   : Exchange currency code
    :param float rate                : Rate from base currency to exchange currency
    """

    def __init__(self, base_currency, exchange_currency, rate):
        self._base_currency = base_currency
        self._exchange_currency = exchange_currency
        self._rate = rate

    def __add__(self, other):
        rate_sum = self._rate + other._rate
        return ExchangeRate(self._base_currency, self._exchange_currency, rate_sum)

    def __truediv__(self, other):
        new_rate = self._rate / other
        return ExchangeRate(self._base_currency, self._exchange_currency, new_rate)

    def __eq__(self, other):
        return (self._base_currency == other._base_currency and
                self._exchange_currency == other._exchange_currency and
                self._rate == other._rate)

    def __repr__(self):
        return "{} {} {}".format(self._base_currency, self._exchange_currency, self._rate)