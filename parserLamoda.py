import requests
import json
import csv
import lxml
from bs4 import BeautifulSoup

url = 'https://www.lamoda.ru/p/mp002xu03c1j/home_accs-nochnezhna-postelnoe-bele-evro/?source_rec_type=alsobuy'
response = requests.get(url)

html = BeautifulSoup(response.text, 'lxml')

try:
    price = str(html.find(class_='product-prices-root'))
    price = price.split("'")
    decoded_data = json.loads(price[1])
    print('Цена со скидкой : ' + decoded_data['details'][1]['value'])
except:
    print('no sale')


price2 = html.find_all(class_='product-prices-root')


for i in price2:
    total = i.find(class_='product-prices__price').get_text()
    print('Цена на эту хуйню без скидки : ' + total)






