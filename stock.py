import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

def quarterly():
    SCRIP = input("Enter your stock for analysis:")
    url = f'https://www.screener.in/company/{SCRIP}/#quarters'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    quarterly_results_table = soup.find('table')

    if quarterly_results_table is not None:
        quarterly_results = PrettyTable()
        headers = []
        for header in quarterly_results_table.find_all('th'):
            headers.append(header.text.strip())
        quarterly_results.field_names = headers
        for row in quarterly_results_table.find_all('tr')[1:]:
            quarter_data = []
            for cell in row.find_all('td')[:len(headers)]:
                quarter_data.append(cell.text.strip())
            if quarter_data:
                quarterly_results.add_row(quarter_data)
        print(quarterly_results)
    else:
        print("Quarterly results table not found.")