# Automated Daily Report via Web Scraping and Email

## Objective
Scrape food shop information from the Mafengwo travel website and automatically send a daily report via email to designated recipients.

## Process
1. Send a request to retrieve the webpage source code.  
2. Parse the HTML to extract food shop names and ratings, then write the data into an Excel file.  
3. Parse the HTML to extract attraction names and ticket prices, then write the data into the same Excel file.  
4. Read the Excel file and send it as an email report.  

- For practice, scraping the first 10 pages is sufficient.  
- An Excel file containing the scraped data is provided as a reference.  