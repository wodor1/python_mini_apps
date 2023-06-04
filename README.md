# Currency Converter Application

==========================

This application implements a simple command-line currency converter in Python.

## Dependencies

- Python 3.7 or later
- forex-python

You can install the dependencies with the following command:

pip install -r requirements.txt

## Usage

Run the currency_converter.py script from the command line, then follow the instructions on the console:

Enter the amount you want to convert.
Enter the currency you want to convert from (e.g., USD, EUR, HUF).
Enter the currency you want to convert to (e.g., USD, EUR, HUF).

For example:

python converter.py
Enter the amount: 100
Enter the currency (e.g., USD): usd
Which currency would you like to convert to (e.g., EUR): eur

# Password Generator Application

==========================

This application is a simple command-line Python program that generates a password based on the parameters provided by the user.

## Usage

Run the `password_generator.py` file in a Python environment. The program will ask three questions:

1. How long should the password be (number of characters)?
2. Should it include numbers (yes/no)?
3. Should it include special characters (yes/no)?

Provide answers to these questions, and the program will generate a password based on the provided parameters.

## Requirements

The program uses the Python standard library, so there is no need to install any additional packages.

## Caution

This program does not handle invalid inputs, such as negative numbers for the password length or non-"yes" and "no" answers for the numbers or special characters question. In real-world applications, it is advisable to handle such situations as well.

# Python Google Sheets App

==========================

This application can read and write data to a Google Sheets document.

## Installation

1. Install the necessary Python packages using the following command: `pip install -r requirements.txt`

2. Create a Google Cloud project, enable the Google Sheets and Google Drive APIs, and then create a service account. Download the authentication data for the service account in JSON format and rename it to 'credentials.json'.

3. Place the 'credentials.json' file in the project directory.

## Usage

Run the `python_google_sheet.py` file with Python. The application will read data from the Google Sheets document and then write new data into it.

## Security

Do not disclose the 'credentials.json' file as it poses a significant security risk. If you accidentally make your authentication data public, create new authentication data.
