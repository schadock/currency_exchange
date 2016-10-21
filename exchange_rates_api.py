class ExchangeRatesAPI:
    """
    Interface of exchange rates API
    """

    def _get_exchange_rates(self, date_of_exchange):
        """
        Geting Exchange rate from api

        :param datetime.date date_of_exchange: Date of exchange

        :rtype: dict
        """

        raise NotImplementedError

    def rate_for_date(self, base_currency, exchange_currency, date_of_exchange):
        """
        Public API to get exchange rate

        :param str      base_currency       : Base currency code
        :param str      exchange_currency   : Base currency code
        :param datetime date_of_exchange    : Date of exchange

        :rtype: ExchangeRate
        """

        raise NotImplementedError