# Create a new directory for your project

mkdir StockScanner
cd StockScanner

# Create a virtual environment

python -m venv venv

# Activate the virtual environment

venv\Scripts\activate # Windows (Use CMD prompt)

# source venv/bin/activate # macOS/Linux

# Upgrade pip

pip install --upgrade pip

# Install Required Modules

pip install -r requirements.txt

# Verify Flask installation

<!-- python -m flask --version -->

# Run the Flask Application

python main.py

# Access the Web Interface

<!-- Open your web browser and go to http://127.0.0.1:5000/. -->

# To run all tests, navigate to the StockScanner directory and run

python -m unittest discover tests

Note: Upload any .csv file via local React App http://localhost:3000/, which includes the symbols of the stock of your choice.
You can also Download the file and keep in your working directory and upload the same.
Ex. from https://www.nseindia.com/products-services/indices-nifty200-index and https://www.nseindia.com/products-services/indices-nifty500-index download
https://nsearchives.nseindia.com/content/indices/ind_nifty200list.csv
https://nsearchives.nseindia.com/content/indices/ind_nifty500list.csv
