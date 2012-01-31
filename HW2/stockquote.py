# Corey Goldberg's Stock Quote Module
# http://www.goldb.org/goldblog/2007/09/14/PythonStockQuoteModule.aspx

import urllib
import re

def get_quote(symbol):
    base_url = 'http://finance.google.com/finance?q='
    content = urllib.urlopen(base_url + symbol).read()
    m = re.search('class="pr".*?>(.*?)<', content)
    if m:
        quote = m.group(1)
    else:
        quote = 'no quote available for: ' + symbol
    return quote
