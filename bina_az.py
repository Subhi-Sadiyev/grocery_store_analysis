import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep

###Single page

#URL = 'https://webscraper.io/test-sites/e-commerce/static/product/547'

#request = requests.get(URL)

#soup = BeautifulSoup(request.text, 'html.parser')

#titles = soup.find('title')

#print(titles)



###Multiple page

URL = 'https://bina.az/items/'

for item in range(3221096,3221110):
    request = requests.get(URL + str(item) + '/')
    soup = BeautifulSoup(request.text, 'html.parser')

    titles = soup.find('title')
    print(titles)
    with open("binaz_az_items.txt", "a", encoding="utf8") as f:
        f.write(str(titles))

    sleep(randint(6,10))
