from forex_python.converter import CurrencyRates
amount = int(input("Please enter the amount you want to convert: "))
from_currency = input("Please enter the currency code that has to be converted: ").upper()
to_currency = input("Please enter the currency code to convert: ").upper()
print("The converted rate is:",  CurrencyRates().convert(from_currency, to_currency, amount))
