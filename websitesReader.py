import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('span', class_='text')

    for i, quote in enumerate(quotes, start=1):
        print(f"Quote {i}: {quote.text}")
else:
    print(f'Failed to fetch quotes. Status code: {response.status_code}')
