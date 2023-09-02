import requests
from bs4 import BeautifulSoup
import re

def parse_website():
    url = "https://luckperms.net/editor/"  # URL сайта для парсинга
    response = requests.get(url)  # Отправляем GET-запрос на сайт
    soup = BeautifulSoup(response.text, "html.parser")  # Создаем объект BeautifulSoup для парсинга HTML

    links = soup.find_all("a")
    
    pattern = re.compile(r'[a-zA-Z0-9]{10}')

    for link in links:
        href = link.get("href")
        match = pattern.search(href)
        if match:
            code = match.group()
            print(code)
            
parse_website()