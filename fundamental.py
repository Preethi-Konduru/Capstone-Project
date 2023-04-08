from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

def fundamental():
    SCRIP = input("Enter your stock for analysis:")
    link = f'https://www.screener.in/company/{SCRIP}'
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(link, headers=hdr)

    try:
        page = urlopen(req)
        soup = BeautifulSoup(page, features="lxml")

        div_html = soup.find('div', {'class': 'company-ratios'})
        ul_html = div_html.find('ul', {'id': 'top-ratios'})
        market_cap = 0.0
        stock_pe = 0.0
        book_value = 0.0
        dividend_yield = 0.0
        roce = 0.0
        roe = 0.0
        face_value = 0.0

        for li in ul_html.find_all("li"):
            name_span = li.find('span', {'class': 'name'})
            if 'Market Cap' in name_span.text:
                num_span = li.find('span', {'class': 'number'})
                num_span = num_span.text.replace(',', '')
                market_cap = float(num_span) if (num_span != '') else 0.0
            elif 'Stock P/E' in name_span.text:
                num_span = li.find('span', {'class': 'number'})
                stock_pe = float(num_span.text) if (num_span != '') else 0.0
            elif 'Book Value' in name_span.text:
                num_span = li.find('span', {'class': 'number'})
                book_value = float(num_span.text) if (num_span != '') else 0.0
            elif 'Dividend Yield' in name_span.text:
                num_span = li.find('span', {'class': 'number'})
                dividend_yield = float(num_span.text[:-1]) if (num_span != '') else 0.0
            elif 'ROCE' in name_span.text:
                num_span = li.find('span', {'class': 'number'})
                roce = float(num_span.text[:-1]) if (num_span != '') else 0.0
            elif 'ROE' in name_span.text:
                num_span = li.find('span', {'class': 'number'})
                roe = float(num_span.text[:-1]) if (num_span != '') else 0.0
            elif 'Face Value' in name_span.text:
                num_span = li.find('span', {'class': 'number'})
                face_value = float(num_span.text[:-3]) if (num_span != '') else 0.0

        print("Market Cap: ", market_cap)
        print("Stock P/E: ", stock_pe)
        print("Book Value: ", book_value)
        print("Dividend Yield: ", dividend_yield)
        print("ROCE: ", roce)
        print("ROE: ", roe)
        print("Face Value: ", face_value)

    except:
        print("Sorry not available")