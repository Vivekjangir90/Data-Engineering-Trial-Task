import requests
from bs4 import BeautifulSoup  
import pandas as pd  

def scrape_website(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  projects = soup.find_all('div', class_='project-card')

  project_data = []
  for project in projects:
    title = project.find('h3').text.strip()
    location = project.find('p', class_='location').text.strip()
    project_data.append({
        'title': title,
        'location': location,
        # ... Add other data points ...
    })

  return pd.DataFrame(project_data)


websites = [
    'https://www.ci.richmond.ca.us/1404/Major-Projects',
    'https://www.bakersfieldcity.us/518/Projects-Programs',
    # ... Add more websites ...
]

all_projects = pd.DataFrame()
for website in websites:
  try:
    project_data = scrape_website(website)
    all_projects = pd.concat([all_projects, project_data], ignore_index=True)
  except Exception as e:
    print(f"Error scraping {website}: {e}")


all_projects['date'] = pd.to_datetime(all_projects['date'])  # IF 'date' exists
all_projects['budget'] = all_projects['budget'].str.replace(',', '').astype(float)  # IF 'budget' exists


all_projects.to_csv('california_construction_projects.csv', index=False)
