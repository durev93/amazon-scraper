import os
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

# Pfade angeben
data_lake = "./data-lake"
output_dir = "./output"
imported_dir = os.path.join(data_lake, "imported")
os.makedirs(imported_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# BeautifulSoup-Objekt erstellen
def create_soup(html_content):
    return BeautifulSoup(html_content, "html.parser")

# Daten extrahieren und in Liste speichern
def extract_data(soup):
    data = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Beispielhafter Scraping-Code, anpassen nach Bedarf
    for item in soup.select('.zg-item'):
        rank = item.select_one('.zg-badge-text')
        asin = item.get('data-asin')
        if rank and asin:
            rank = rank.get_text(strip=True).replace("#", "")
            data.append([rank, asin, now])
    
    print(f"[DEBUG] Extracted data: {data}")  # Debugging-Ausgabe
    return data

# DataFrame erstellen und in SQLite-Datenbank speichern
def create_dataframe_and_save_to_db(data):
    if not data:
        print("[DEBUG] No data to save.")
        return False
    
    df = pd.DataFrame(data, columns=["Rank", "ASIN", "Timestamp"])
    db_filename = os.path.join(output_dir, "amazon_analytics.db")
    conn = sqlite3.connect(db_filename)
    
    try:
        print(f"[DEBUG] Saving DataFrame to database: {df}")  # Debugging-Ausgabe
        df.to_sql("bestsellers", conn, if_exists="append", index=False)
        conn.close()
        return True
    except Exception as e:
        print(f"[ERROR] Failed to save data to database: {e}")
        conn.close()
        return False

# HTML-Datei in den "imported"-Ordner verschieben
def move_html_to_imported(website_path):
    new_path = os.path.join(imported_dir, os.path.basename(website_path))
    os.rename(website_path, new_path)
    print(f"[DEBUG] Moved {website_path} to {new_path}")  # Debugging-Ausgabe

# Hauptfunktion
def main():
    website_files = [file for file in os.listdir(data_lake) if file.endswith(".html")]

    for website_file in website_files:
        website_path = os.path.join(data_lake, website_file)
        with open(website_path, "rb") as file:
            html_content = file.read()
        
        soup = create_soup(html_content)
        data = extract_data(soup)
        
        # Nur verschieben, wenn die Daten erfolgreich gespeichert wurden
        if create_dataframe_and_save_to_db(data):
            move_html_to_imported(website_path)
        else:
            print(f"[ERROR] Failed to process {website_path}. Not moving the file.")

if __name__ == "__main__":
    main()
