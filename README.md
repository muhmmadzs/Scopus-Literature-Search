# Scopus Literature Search and DOI Browser

## Description
This repository contains an advanced Python script that automates literature searches using the Scopus API, catering to academic researchers and students. It enables keyword-based searches within a specified publication year range in the Scopus database. The search results, including article titles, DOI links, and publication years, are saved into a CSV file. Additionally, the script can open all DOI links from the CSV file in new browser tabs, streamlining the process of accessing the full texts of these articles.

## Key Features
- Automated literature search in the Scopus database using custom keywords and year ranges.
- Results include article titles, DOI links, and publication years.
- Output saved in a structured CSV file, named according to the year range.
- Functionality to open all DOI links from the CSV file in new browser tabs.
- Delays between opening tabs to manage system resources effectively.

## How to Use
1. Replace `your_api_key` with your actual Scopus API key.
2. Set your desired search query and publication year range in the script.
3. Run the script to fetch and save the search results in a CSV file.
4. (Optional) Run the `open_doi_links_from_csv` function to open all DOI links in your web browser.



## Requirements.
- Python 3
- Libraries: `requests` (for API calls), `csv` (for file operations), `webbrowser` (for opening URLs)
   
## Potential Use Cases.
- Academic researchers conducting extensive literature reviews.
- University students gathering sources for thesis or dissertation research.
- Data analysts and librarians compiling bibliographic datasets for academic studies.

## Note.
- Ensure compliance with Scopus API terms of use.
- The DOI link opening feature should be used responsibly to avoid system overload.

## Installation
Install the required Python libraries using:
```bash
pip install requests

