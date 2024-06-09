# Amazon Bestsellers Scraper

This project is a web scraper designed to retrieve and store the Amazon bestsellers in the DIY category. The scraper saves the data to a SQLite database and runs daily on PythonAnywhere.

The goal of this project is to monitor the Amazon ranking of a specific product to perform analyses and predictions.

## Files Description

- **lib_py/scraping_amazonranking.py**: Python script to scrape Amazon bestsellers.
- **lib_py/dwh_amazonranking.py**: Python script to process and store scraped data into SQLite database.
- **run.sh**: Shell script to run the scraper and update the database.
- **data-lake/**: Directory where the HTML files of the scraped webpages are stored.
- **data-lake/imported/**: Directory where processed HTML files are moved.
- **output/**: Directory where the SQLite database is stored (created if not present).
- **README.md**: This readme file.

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/username/repository.git
    cd repository
    ```
2. **Run the scraper**:
    You can manually run the scraper using:
    ```bash
    bash run.sh
    ```
