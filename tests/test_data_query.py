import unittest
import data_query as query

class testDataQuery(unittest.TestCase):

    def testQuery(self):
        stats = ["release_speed"]
        dateRange = ["2017-04-01", "2017-04-02"]
        df = query.query(573186, "", stats, dateRange, "", "")
        self.assertEqual(df, 0)
