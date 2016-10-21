import unittest
import datetime
from period import Period

class PeriodTest(unittest.TestCase):
    """
    Test Period class for creating dates list.
    """
    def test_create_correct_dates_list(self):
        """
        Check creating dates list
        """

        period = Period(datetime.date(2016, 7, 1), datetime.date(2016, 7, 3))
        dates_lists = period.dates()
        expected_list = [datetime.date(2016, 7, 1), datetime.date(2016, 7, 2)]

        self.assertAlmostEqual(dates_lists, expected_list)