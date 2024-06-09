#!/usr/bin/env python

import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup

# Pfad erstellen
data_lake = "./data-lake"
os.makedirs(data_lake, exist_ok=True)

# URL of the Amazon Bestsellers page
url = "https://www.amazon.de/gp/bestsellers/diy/2076264031"

# Überschrift
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, wie Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Send an HTTP GET request to the URL
response = requests.get(url, headers=headers, allow_redirects=True)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Generate a timestamp for the filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create a filename for the HTML file
    website_filename = os.path.join(data_lake, f"website_{timestamp}.html")

    # Save the website content to the data-lake directory
    with open(website_filename, "w", encoding="utf-8") as file:
        file.write(str(soup))
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
