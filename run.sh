#!/bin/bash

cd "$(dirname "$0")"

echo "[INFO] ***Pull from Github***"
git pull

echo "[INFO] ***Start scraping***"
python ./lib_py/scraping_amazonranking.py

echo "[INFO] ***Update DWH***"
python ./lib_py/dwh_amazonranking.py

echo "[INFO] ***Commit to Github***"
git add data-lake
git commit -a -m "Run daily scraper"
git push
