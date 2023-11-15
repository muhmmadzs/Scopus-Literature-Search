# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:31:10 2023

@author: muhamzs
"""

import requests
import json
import csv
import webbrowser
import time


def search_scopus(query, api_key, start_year, end_year, max_results=20):
    base_url = "https://api.elsevier.com/content/search/scopus"
    headers = {"X-ELS-APIKey": api_key, "Accept": "application/json"}
    year_range_query = f" AND PUBYEAR AFT {start_year} AND PUBYEAR BEF {end_year}"
    full_query = query + year_range_query
    params = {"query": full_query, "count": max_results}

    response = requests.get(base_url, headers=headers, params=params)
    
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f"Error: {response.status_code}")
        return None

def parse_results(results):
    articles = []

    for item in results.get('search-results', {}).get('entry', []):
        title = item.get('dc:title', 'No Title')
        doi = item.get('prism:doi', 'No DOI')
        year = item.get('prism:coverDate', 'No Date')[:4]  # Extracting the year

        doi_url = f"https://doi.org/{doi}" if doi != 'No DOI' else 'No DOI URL'
        articles.append((title, doi_url, year))

    return articles

def save_to_csv(articles, start_year, end_year, filename=None):
    if filename is None:
        filename = f'scopus_results_{start_year}_to_{end_year}.csv'
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'DOI', 'Year'])
        for article in articles:
            writer.writerow(article)

    return filename

def open_doi_links_from_csv(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            doi_url = row[1]
            if doi_url.startswith("https://doi.org/"):
                webbrowser.open_new_tab(doi_url)
                time.sleep(2)  # Delay to prevent opening too many tabs at once

# Example usage
api_key = 'Api key'   # Replace with your actual API key
query = "TITLE-ABS-KEY(train wheel wear prediction)"
start_year = 2021
end_year = 2023
results = search_scopus(query, api_key, start_year, end_year)

if results:
    parsed_results = parse_results(results)
    filename = save_to_csv(parsed_results, start_year, end_year)
    print(f"Results have been saved to {filename}")
    # Optionally, uncomment the next line to open DOI links after saving the results
    # open_doi_links_from_csv(filename)
else:
    print("No results found or there was an error in the request.")
