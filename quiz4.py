import sqlite3
import time
import requests
from bs4 import BeautifulSoup

conn = sqlite3.connect('quote.sqlite')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS quotes")
cursor.execute("""CREATE TABLE quotes(
                quote TEXT,
                author TEXT,
                tags TEXT)""")

url = 'https://quotes.toscrape.com/'
website = BeautifulSoup(requests.get(url).text, 'html.parser')
quotes = website.find_all('div', class_='quote')
text, author, tags = [], [], []
for quote in quotes:
    text = quote.find(class_='text').text.strip()
    author = quote.find(class_='author').text.strip()
    tags_container = quote.find('div', class_='tags').find_all('a')
    tags = [tags_container[i].text for i in range(len(tags_container))]
    cursor.execute('INSERT INTO quotes VALUES (?,?,?)', (text, author, tags))

print(cursor.execute('SELECT * FROM quotes'))