# Billing System with PDF Generation - README

This Python script implements a billing system that allows customers to add products, generate bills, and output the bill in PDF format. The system utilizes CSV files to store product information and MySQL database to store customer information.

## Requirements

- Python 3.x
- `mysql-connector-python` library for MySQL database connectivity
- `reportlab` library for PDF generation

You can install the required libraries using pip:

```bash
pip install mysql-connector-python reportlab
```

## Usage

1. Ensure MySQL server is running and accessible.
2. Create a MySQL database named `customer` with a table named `customer` having columns: `ID`, `Name`, and `Password`.
3. Ensure the script file `BillingSystem.py` and CSV files (`products.csv` and `Billings.csv`) are in the same directory.
4. Run the script using Python:

```bash
python BillingSystem.py
```

5. Follow the prompts to navigate through the billing system:
   - Choose whether you are a new customer or a returning customer.
   - For new customers, enter your details which will be stored in the `customer` table.
   - For returning customers, enter your name and password. If the credentials are correct, access will be granted.
   - Add products by providing the barcode, name, and cost.
   - Review the final list of products.
   - Choose to continue or exit.
   - Provide the payment method (Cash/Card/UPI).
6. A PDF bill will be generated and saved in the same directory.

## PDF Bill Naming Convention

The PDF bill file will be named with the format `bill_hour_minute_second__day_month_year.pdf`. For example, if the bill is generated at 10:30:45 on 5th February 2024, the file will be named `bill_10_30_45__05_02_2024.pdf`.

## Notes

- Ensure proper error handling and validation of user inputs.
- Customize the database credentials and file paths as per your setup.
- Adjust the PDF bill layout and styling according to your requirements.
- The script assumes a simple CSV-based product management system and a MySQL-based customer management system. Adjustments may be needed for different environments.
