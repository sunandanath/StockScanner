import unittest
import pandas as pd
from technical_indicators import calculate_technical_indicators

class TestTechnicalIndicators(unittest.TestCase):

    def setUp(self):
        data = {
            'Close': [i for i in range(100, 130)]  # Simple range for testing
        }
        self.df = pd.DataFrame(data)

    def test_calculate_technical_indicators(self):
        df_with_indicators = calculate_technical_indicators(self.df)
        self.assertIn('20 Day MA', df_with_indicators.columns, "Should include '20 Day MA' column")
        self.assertIn('50 Day MA', df_with_indicators.columns, "Should include '50 Day MA' column")
        self.assertIn('Upper Band', df_with_indicators.columns, "Should include 'Upper Band' column")
        self.assertIn('Lower Band', df_with_indicators.columns, "Should include 'Lower Band' column")
        self.assertEqual(len(df_with_indicators['20 Day MA'].dropna()), 11, "Should calculate 20 Day MA for last 11 days")
        self.assertEqual(len(df_with_indicators['50 Day MA'].dropna()), 0, "Should have no 50 Day MA due to insufficient data")

if __name__ == '__main__':
    unittest.main()
