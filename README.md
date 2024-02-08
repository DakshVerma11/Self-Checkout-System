# Self Checkout System

This Python script implements a self-checkout system where customers can add products, update product costs, delete products, and generate bills. The system utilizes CSV files to store product information and MySQL database to store customer information.

## Requirements

- Python 3.x
- `mysql-connector-python` library for MySQL database connectivity

## Setup

1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install `mysql-connector-python` using pip:

```bash
pip install mysql-connector-python
```

3. Set up a MySQL database named `customer` with a table named `customer` having columns: `ID`, `Name`, and `Password`.
4. Ensure the MySQL server is running and accessible.
5. Ensure the script file and CSV files (`products.csv` and `Billings.csv`) are in the same directory.

## Usage

1. Run the script using Python:

```bash
python self_checkout.py
```

2. Follow the prompts to navigate through the self-checkout system.
3. Choose whether you are a new customer or a returning customer.
4. For new customers, you'll be prompted to enter your details which will be stored in the `customer` table.
5. For returning customers, you'll be prompted to enter your name and password. If the credentials are correct, access will be granted.
6. Add products by providing the barcode, name, and cost.
7. Update product costs by providing the barcode and the new cost.
8. Delete products by providing the barcode.
9. After adding all products, review the final list.
10. Choose to continue or exit.
11. If you continue, provide the payment method (Cash/Card/UPI).
12. A bill will be generated and stored in `Billings.csv`.

## Notes

- Make sure to handle errors and edge cases appropriately.
- Ensure proper security measures for handling passwords and database connections.
- Customize the database credentials and file paths as per your setup.
- The script assumes a simple CSV-based product management system and a MySQL-based customer management system. Adjustments may be needed for different environments.
