import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape data from a single source(according to need)
def scrape_data(url):
    # Fetch HTML content
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        # Extract relevant information
        # Example: title = soup.find('h1').text
        #           description = soup.find('p').text
        #           status = soup.find('div', class_='status').text
        # Return a dictionary containing the extracted data
        # return {'title': title, 'description': description, 'status': status}
        return soup
    else:
        print(f"Failed to fetch data from {url}")
        return None

urls = [
    'https://www.ci.richmond.ca.us/1404/Major-Projects',
    # 'https://www.bakersfieldcity.us/518/Projects-Programs',
    # Add more URLs as needed
]

data = []

for url in urls:
    scraped_data = scrape_data(url)
    if scraped_data:
        # data.append(scraped_data)
        print(scraped_data)

df = pd.DataFrame(data)

df.to_csv('scraped_data.csv', index=False)
