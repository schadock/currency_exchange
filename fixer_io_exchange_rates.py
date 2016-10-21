import requests
from exchange_rates_api import ExchangeRatesAPI
from exchange_rate import ExchangeRate

class FixerIOExchangeRates(ExchangeRatesAPI):
    """
    Get JSON data from fixer.io API and retrive day rate.

    :rtype: None:
    """

    EXCHANGE_RATES_API_URL = "http://api.fixer.io/"
    def _date_to_string(self, rate_date):
        """
        Convert date in datetime.time to string

        :param  datetime.time   rate_date: Date of rate

        :rtype: str
        """

        rate_date_string = rate_date.strftime("%Y-%m-%d")
        return rate_date_string

    def _create_full_url(self, base_currency, exchange_currency, rate_date):
        """
        Create full url of exchange currency for single date

        :param   str base_currency:     Base currency code
        :param   str exchange_currency: Exchange currency code
        :param   str rate_date:         Day for exchange

        :rtype:  str
        """

        date = self._date_to_string(rate_date)
        base_currency_path = "base=" + base_currency
        exchange_currency_path = "symbols=" + exchange_currency
        full_url = '%s%s?%s&%s' % (self.EXCHANGE_RATES_API_URL, date, base_currency_path, exchange_currency_path)
        return full_url

    def _get_exchange_rate(self, request_url):
        """
        Get exchange rates base_currency to exchange_currency from API.

        :param  str   request_url : Full request url

        :rtype: dict
        """

        data_response = requests.get(request_url)
        data_from_request = data_response.json()
        return data_from_request

    def _extract_rate_from_json(self, data_from_day, exchange_currency):
        """
        Extracting rate from dictionary

        :param  dict data_from_day      : Data of exchange from API
        :param  str  exchange_currency  : Base currency code

        :rtype: float
        """
        rates_line = data_from_day["rates"]
        rate = rates_line[exchange_currency]
        rate = float(rate)
        return rate

    def rate_for_date(self, base_currency, exchange_currency, date_of_exchange):
        """

        :param  str      base_currency       : Base currency code
        :param  str      exchange_currency   : Exchange currency code
        :param  datetime date_of_exchange    : Date of exchange

        :rtype: ExchangeRate
        """
        full_url = self._create_full_url(base_currency, exchange_currency, date_of_exchange)
        data_from_api = self._get_exchange_rate(full_url)
        rate = self._extract_rate_from_json(data_from_api , exchange_currency)
        exchange_rate = ExchangeRate(base_currency, exchange_currency, rate)
        return exchange_rate