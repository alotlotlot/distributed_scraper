

import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Add your scraping logic here
        data = soup.find('div', class_='example')
        return data.text if data else 'No data found'
    else:
        return 'Failed to retrieve the webpage'

if __name__ == '__main__':
    url = 'https://example.com'
    scraped_data = scrape_website(url)
    print(scraped_data)

# This is a comment added to demonstrate committing changes in Git
