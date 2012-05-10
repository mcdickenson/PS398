"""TSA Wait Times Scraper
Final Project Draft
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/FinalProj/

# Which libraries do we need? 
import urllib2, urllib, datetime, re, string, time, csv, random, cookielib
from urllib import FancyURLopener

# Which site/page do we want to scrape? 
page_to_scrape = 'http://apps.tsa.dhs.gov/mytsa/'

# What is the name of this scrape (for output file)?
scrape_name = 'TSAwait'

# What info do we want? 
Headers = ["Airport","Terminal","Time","Date"]

# Open output file
nameFile = "WebScrape-"+str(scrape_name)+".csv"
writeFile = open(nameFile,"wb")
csvwriter = csv.writer(writeFile)
csvwriter.writerow(Headers)

def get_page_source(url_to_get):
    cj = cookielib.MozillaCookieJar()
    cj.load('cookies2.txt')

    user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:11.0) Gecko/20100101 Firefox/11.0'
    ]

    headers = {
    'HTTP_USER_AGENT': random.choice(user_agents),
    'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml; q=0.9,*/*; q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded'
    }


    formFields = (
   # the viewstate is actualy 800+ characters in length! I truncated it
   # for this sample code.  It can be lifted from the first page
   ## (r'__VSTATE', r'7TzretNIlrZiKb7EOB3AQE ... ...2qd6g5xD8CGXm5EftXtNPt+H8B'),

   # following are more of these ASP form fields
   ## (r'__VIEWSTATE', r''),
   ## (r'__EVENTVALIDATION', r'/wEWDwL+raDpAgKnpt8nAs3q+pQOAs3q/pQOAs3qgpUOAs3qhpUOAoPE36ANAve684YCAoOs79EIAoOs89EIAoOs99EIAoOs39EIAoOs49EIAoOs09EIAoSs99EI6IQ74SEV9n4XbtWm1rEbB6Ic3/M='),
   ## (r'ctl00_RadScriptManager1_HiddenField', ''), 
   ## (r'ctl00_tabTop_ClientState', ''), 
   ## (r'ctl00_ContentPlaceHolder1_menuMain_ClientState', ''),
   ## (r'ctl00_ContentPlaceHolder1_gridMain_ClientState', ''),

   # search criteria
   (r'search_form$ContentPlaceHolder1$search_field', 'IAH'),   # Search text
   (r'search_form$ContentPlaceHolder1$search_btn', 'Submit')  # Search button itself
        )

    # these have to be encoded    
    encodedFields = urllib.urlencode(formFields)

    req = urllib2.Request(url_to_get, encodedFields, headers)
    handle= urllib2.urlopen(req)
    pageSource = handle.read()
    pageSource = pageSource.decode('ascii','ignore')
    time.sleep(random.uniform(1,3)) # wait between 1 and 3 seconds
    return pageSource

temp = get_page_source(page_to_scrape)
print temp
    




