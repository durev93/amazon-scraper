# Amazon Bestsellers Scraper

This project is a web scraper designed to retrieve and store the Amazon bestsellers in the DIY category. The scraper saves the data to a SQLite database and runs daily on PythonAnywhere.

## Directory Structure
repository/
│
├── lib_py/
│ ├── scraping_amazonranking.py
│ ├── dwh_amazonranking.py
│
├── run.sh
├── README.md
└── data-lake/
└── imported/


## Files Description

- **notebooks/**: Directory for Jupyter notebooks (if any).
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

## Scheduling on PythonAnywhere

1. **Login to PythonAnywhere**.
2. **Clone the repository** and navigate to the directory:
    ```bash
    git clone https://github.com/username/repository.git
    cd repository
    ```
3. **Schedule a daily task**:
    - Go to the "Tasks" section on the PythonAnywhere dashboard.
    - Schedule a new task with the following command:
      ```bash
      bash /home/username/repository/run.sh
      ```

This will ensure that your scraper runs daily and updates the database with the latest Amazon bestseller data.
