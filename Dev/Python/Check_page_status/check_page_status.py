import requests
import time
from lxml import html
from bs4 import BeautifulSoup

url = "https://guitarsgarden.com/collections/fflp-electric-guitars/products/new-new-firefly-fflp-electric-guitars-1?variant=30318694727780"
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, features="html.parser")
while True:
    page = requests.get(url)
    if "Sold Out" not in response.text:
        print("Item is in stock")
    print("Item is sold out")
    time.sleep(60)


