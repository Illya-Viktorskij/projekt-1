import requests
from bs4 import BeautifulSoup as bs

def reqs(url):
    respons = requests.get(url)
    html = respons.content

    if respons.status_code == 200:
        soup = bs(html, "html.parser")

    result = soup.find('ul', class_="wp-block-list").find_all('li')
    text = '\n'.join(paragraph.text for paragraph in result)
    with open("sale", 'w', encoding='utf-8') as file:
        file.write(text)

