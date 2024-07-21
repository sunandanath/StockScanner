import unittest
import pandas as pd
from analysis import rank_stocks

class TestAnalysis(unittest.TestCase):

    def setUp(self):
        self.data = {
            'RELIANCE.NS': pd.DataFrame({
                'Close': [100, 105, 110, 115, 120],
                'Upper Band': [130, 130, 130, 130, 130],
                'Lower Band': [90, 90, 90, 90, 90]
            }),
            'TCS.NS': pd.DataFrame({
                'Close': [200, 205, 210, 215, 220],
                'Upper Band': [230, 230, 230, 230, 230],
                'Lower Band': [190, 190, 190, 190, 190]
            })
        }

    def test_rank_stocks(self):
        ranking_df = rank_stocks(self.data)
        self.assertEqual(len(ranking_df), 2, "Should rank two stocks")
        self.assertEqual(ranking_df.iloc[0]['Symbol'], 'RELIANCE.NS', "RELIANCE.NS should be first based on ranking")
        self.assertEqual(ranking_df.iloc[1]['Symbol'], 'TCS.NS', "TCS.NS should be second based on ranking")

if __name__ == '__main__':
    unittest.main()
