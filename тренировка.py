import requests
from bs4 import BeautifulSoup
import lxml

url ="https://mfd.ru/currency/?currency=USD"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
table = soup.find("table", class_="mfd-table mfd-currency-table").text
print(table)
