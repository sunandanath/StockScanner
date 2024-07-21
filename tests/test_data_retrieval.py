import unittest
import os
import pandas as pd
from data_retrieval import get_nifty_200_symbols, fetch_market_data, save_data_to_csv

class TestDataRetrieval(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a sample CSV file for testing
        cls.test_csv = 'data/ind_nifty200list_test.csv'
        df = pd.DataFrame({'Symbol': ['RELIANCE', 'TCS', 'INFY']})
        df.to_csv(cls.test_csv, index=False)
        
        # Backup the original CSV file and replace it with the test CSV
        cls.original_csv = 'data/ind_nifty200list.csv'
        cls.backup_csv = f'{cls.original_csv}.bak'
        if os.path.exists(cls.original_csv):
            if os.path.exists(cls.backup_csv):
                os.remove(cls.backup_csv)
            os.rename(cls.original_csv, cls.backup_csv)
        os.rename(cls.test_csv, cls.original_csv)

    @classmethod
    def tearDownClass(cls):
        # Restore the original CSV file
        if os.path.exists(cls.backup_csv):
            if os.path.exists(cls.original_csv):
                os.remove(cls.original_csv)
            os.rename(cls.backup_csv, cls.original_csv)
        if os.path.exists(cls.test_csv):
            os.remove(cls.test_csv)

    def test_get_nifty_200_symbols(self):
        symbols = get_nifty_200_symbols()
        self.assertEqual(len(symbols), 3, "Should fetch symbols from CSV file")
        self.assertIn('RELIANCE.NS', symbols, "Should include RELIANCE.NS in the symbols list")

    def test_fetch_market_data(self):
        symbol = 'RELIANCE.NS'
        df = fetch_market_data(symbol)
        self.assertIsNotNone(df, "DataFrame should not be None")
        self.assertFalse(df.empty, "DataFrame should not be empty")
        required_columns = {'Open', 'High', 'Low', 'Close', 'Volume'}
        self.assertTrue(required_columns.issubset(df.columns), "DataFrame should contain required columns")

    def test_save_data_to_csv(self):
        symbol = 'RELIANCE.NS'
        df = fetch_market_data(symbol)
        save_data_to_csv(symbol, df)
        saved_csv_path = f'data/{symbol}.csv'
        self.assertTrue(os.path.exists(saved_csv_path), "CSV file should be saved")
        if os.path.exists(saved_csv_path):
            os.remove(saved_csv_path)

if __name__ == '__main__':
    unittest.main()
