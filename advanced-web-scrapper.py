import requests
import re
from bs4 import BeautifulSoup

# The URL of the website to scrape
url = "https://www.example.com"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all links on the website
links = soup.find_all('a')

# Create a list to store the unique links
unique_links = []

# Iterate through the links and add unique links to the list
for link in links:
    link = link.get('href')
    if link not in unique_links:
        unique_links.append(link)

# Open a text file to save the data
with open('scraped_data.txt', 'w') as file:
    # Write the unique links to the file
    for link in unique_links:
        file.write(link + '\n')

# Find all emails on the website
emails = re.findall(r'[\w\.-]+@[\w\.-]+', response.text)

# Open a text file to save the data
with open('emails.txt', 'w') as file:
    # Write the emails to the file
    for email in emails:
        file.write(email + '\n')
