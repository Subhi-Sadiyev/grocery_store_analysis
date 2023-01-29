import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep

###reading a list of item id's from binaz_az_items_id_half.txt (24045 items)"

items_list_file = open('binaz_az_items_id_half.txt', 'r')

reading = items_list_file.read()

items_list = reading.split(',')


#print(len(items_list))




###fetching limited amount of items from bina_az

URL = 'https://bina.az/items/'
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

for item in items_list:
    request = requests.get(URL + str(item) + '/', headers=headers)
    soup = BeautifulSoup(request.text, 'html.parser')

    titles = soup.find('title').text
    print(request)
    print(titles)
    with open("bina_az_500_items.txt", "a", encoding="utf8") as f:
        f.write(str(titles))

    sleep(randint(20,25))
