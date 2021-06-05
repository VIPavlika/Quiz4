import csv
import time
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
website = BeautifulSoup(requests.get(url).text, 'html.parser')
quotes = website.find_all('div', class_='quote')
header = ['Text', 'Author', 'Tags']
text, author, tags = [], [], []
for quote in quotes:
    text.append(quote.find(class_='text').text.strip())
    author.append(quote.find(class_='author').text.strip())
    tags_container = quote.find('div', class_='tags').find_all('a')
    tags.append([tags_container[i].text for i in range(len(tags_container))])

with open('quotes.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(text)
    writer.writerow(author)
    writer.writerow(tags)