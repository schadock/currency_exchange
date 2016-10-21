from pretenders.client.http import HTTPMock

def get_rate_date_in_json(base_currency, exchange_currency, date, rate):
    """
    Get request for fake fixed.io API

    :param   str      base_currency     : Base currency code
    :param   str      exchange_currency : Exchange currency code
    :param   datetime date              : Date for rating
    :param   float    rate              : Currency exchange rating
    """

    mock = HTTPMock('localhost', 31000, name='ex')
    mock.when('GET /{0}?symbols={1},{2}'.format(date, base_currency, exchange_currency))
    mock.reply('{{ "base":"{0}" , "date":"{1}" , "rates":{{"{2}":{3} }} }}'.format(base_currency, date, exchange_currency, rate).encode('utf-8'),
                                                                    headers={'Content-Type': 'application/json'})