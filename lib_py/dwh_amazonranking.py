import os
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

# Pfad angeben
data_lake = "./data-lake"
output = "./output"
imported = os.path.join(data_lake, "imported")
os.makedirs(imported, exist_ok=True)
os.makedirs(output, exist_ok=True)

# BeautifulSoup-Objekt erstellen
def create_soup(html_content):
    return BeautifulSoup(html_content, "html.parser")

# Daten extrahieren und in Liste speichern
def extract_data(soup):
    data = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    rank_elements = soup.find_all("span", class_="zg-badge-text")
    for rank_element in rank_elements:
        rank = rank_element.get_text(strip=True).replace("#", "")
        asin_element = rank_element.find_next("div", class_="zg-item")
        if asin_element and "data-asin" in asin_element.attrs:
            asin = asin_element["data-asin"]
            data.append([rank, asin, now])
    return data

# DataFrame erstellen und in SQLite-Datenbank speichern
def create_dataframe_and_save_to_db(data):
    df = pd.DataFrame(data, columns=["Rank", "ASIN", "Timestamp"])
    db_filename = os.path.join(output, "amazon_analytics.db")
    conn = sqlite3.connect(db_filename)
    df.to_sql("bestsellers", conn, if_exists="append", index=False)
    conn.close()

# HTML-Datei in den "imported"-Ordner verschieben
def move_html_to_imported(website_path):
    new_path = os.path.join(imported, os.path.basename(website_path))
    os.rename(website_path, new_path)

# Hauptfunktion
def main():
    website_files = [file for file in os.listdir(data_lake) if file.endswith(".html")]

    for website_file in website_files:
        website_path = os.path.join(data_lake, website_file)
        with open(website_path, "rb") as file:
            html_content = file.read()
        
        soup = create_soup(html_content)
        data = extract_data(soup)
        create_dataframe_and_save_to_db(data)
        move_html_to_imported(website_path)

if __name__ == "__main__":
    main()
