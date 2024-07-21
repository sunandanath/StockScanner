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

Note: Make folder named data and keep your targated .CSV file there, ex. ind_nifty200list.csv
