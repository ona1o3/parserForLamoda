from email import header
from aiohttp import request
import requests
import json
import lxml
from bs4 import BeautifulSoup

# url_cards = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

# for i in range(1, 6, 1):
#     url = f'https://www.lamoda.ru/c/5856/shoes-zhenkrossovki/?sitelink=topmenuW&l=11&page={i}'
#     response = requests.get(url, headers = headers)

#     result = BeautifulSoup(response.text, 'lxml')

#     links = result.find_all(class_='x-product-card__link')


#     for link in links:
#         url_card = link.get('href')
#         url_cards.append(url_card)
        
    
    
# with open('file.txt', 'w') as file:
#     for line in url_cards:
#         file.write(f'https://www.lamoda.ru{line}\n')




with open('file.txt') as file:
    lines = [line.strip() for line in file.readlines()]

    data_dict = []
    count = 0

    for line in lines:
    
        q = requests.get(line)
        result = q.content

        soup = BeautifulSoup(result, 'lxml')

        card_name = soup.find(class_='product-title__model-name').text
        product_name = soup.find(class_='product-title__brand-name').text
        price = soup.find(class_='product-prices__price').text

        # print(f'Цена: {price} {card_name} {product_name}')

        data = {
            'type': card_name,
            'name': product_name,
            'price': price,
            'link':line
        }
        count += 1
        print(f'#{count}: completed!')

        data_dict.append(data)

        with open ('data.json', 'w' , encoding='utf-8') as file_json:
            json.dump(data_dict, file_json, indent=4, ensure_ascii = False)