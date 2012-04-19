"""Chris Gelpi Web Scrape
Final Project Draft
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/FinalProj/

# Which libraries do we need? 
import urllib2, urllib, datetime, re, string, time, csv, httplib, sqlite3, cookielib, random
from urllib import FancyURLopener
from xml.sax.saxutils import unescape
import nltk
from nltk import util
from nltk.util import clean_html
from twill import get_browser
from BeautifulSoup import BeautifulSoup


# Which site/page do we want to scrape? 
page_to_scrape = 'http://duke.edu/~gelpi/309SPCCoreSpring11.htm'

# What is the name of this course (for output file)?
course_name = 'SPCcore'

# What info do we want? 
Headers = ["Author","Year","Title","Journal/Publisher", "SearchString"]

# Open output file
nameFile = "WebScrape-"+str(course_name)+".csv"
writeFile = open(nameFile,"wb")
csvwriter = csv.writer(writeFile)
csvwriter.writerow(Headers)


def get_citations_from_web(page_to_get):
    # Get HTML of main page
    mainpage = urllib2.urlopen(page_to_get)
    mainsoup = BeautifulSoup(mainpage)
    mainsoup.prettify()
    #print mainsoup

    # Citations are identified by <p> tags with the following style:

    # Search for citations
    paragraphs = mainsoup.findAll("p",'MsoNormal')

    citations = []
    # Loop thru, get only paragraphs with links (a heuristic for cites)
    for par in paragraphs:
        #print par
        links = par.findAll("a")
        numLinks = len(links)
        if numLinks == 1:
            citations.append(par)

    #Info for progress bar
    numErrors = 0
    numSuccessful = 0
    numTotal = len(citations)

    # Create list of search strings
    searchStrings = []

    # Loop thru actual citations, get info
    for cite in citations:
        # Clean cite of HTML tags and '&quot'
        cite2 = clean_html(str(cite))
        cite2 = cite2.replace('&quot;', '') # TODO: use this as information
        cite3 = cite2.split('.')
        # Create string to be searched in Google Scholar
        shortCite = cite2
        #print len(cite3)
        try:
            # Get names of author(s)
            authorName = cite3[0]

            # Get year of publication
            pubYear = cite3[1]
            pubYear = pubYear.lstrip(' ')

            # Get title of the work
            workTitle = cite3[2]
            workTitle = workTitle.lstrip(' ')

            # Get title of journal or publisher
            journPub = cite3[3]

            # Update progress
            numSuccessful += 1

            # Refresh shortCite
            shortCite = authorName + ' ' + pubYear + ' ' + workTitle
            searchStrings.append(shortCite)

            # Write to CSV
            csvwriter.writerow([authorName, pubYear, workTitle, journPub, shortCite])

        except:
            numErrors += 1
            searchStrings.append(shortCite)
        
    # Report success/failure rate
    numChecked = numErrors + numSuccessful
    print "Checked %s of %s pages. %s successful, %s failures." % (numChecked, numTotal, numSuccessful, numErrors)
    return searchStrings

searchStrings = get_citations_from_web(page_to_scrape)


def get_page_source(url_to_get):
    cj = cookielib.MozillaCookieJar()
    cj.load('cookies.txt')

    # http://code.activestate.com/recipes/523047-search-google-scholar/
    # https://ubuntuincident.wordpress.com/2011/09/11/download-cookie-protected-pages-with-python-using-cookielib-part-2/
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'} # fake
    # Optional: trick Google into thinking I'm using Safari
    # browserName = "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312"
    # Or Windows NT
    # 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    # True info:
    #  Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:11.0) Gecko/20100101 Firefox/11.0
    ## cookie_handler= urllib2.HTTPCookieProcessor(cj)
    ## redirect_handler= urllib2.HTTPRedirectHandler()
    ## opener = urllib2.build_opener(redirect_handler,cookie_handler)
    ## urllib2.install_opener(opener)
    #request = urllib2.Request(url_to_get, None, headers) # or GET
    #handle=urllib2.urlopen(request)

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

    class MyOpener(FancyURLopener):
        version = random.choice(user_agents)
        
    myopener = MyOpener()
    handle=myopener.open(url_to_get)
    pageSource = handle.read()
    pageSource = pageSource.decode('ascii','ignore')
    time.sleep(random.uniform(1,3)) # wait between 1 and 3 seconds
    return pageSource
    

def id_finder(search_string): #Search for citation id's in Google Scholar 
    # set up domain to search
    domainStart = "http://scholar.google.com/scholar?q="
    domainMiddle = search_string.replace('\r', '') # TEST CASE
    domainMiddle = domainMiddle.lstrip()
    domainMiddle = domainMiddle.replace(' ', '+')
    #domainEnd = '&hl=en&btnG=Search&as_sdt=1%2C34&as_sdtp=on'
    # try also: 
    domainEnd = "scholar.google.com/&output=citation&hl=en&as_sdt=0,34&ct=citation&cd=0"
    domainCat = (str(domainStart), str(domainMiddle), str(domainEnd))
    domainFull = ''.join(domainCat)

    pageSource = get_page_source(domainFull)

    # break into separate citations
    citesoup = BeautifulSoup(pageSource)
    citesoup.prettify()
    records = citesoup.findAll('div', {'class': 'gs_fl'})

    # TODO: make this less naive; only takes first record
    # take first citation
    rec = str(records[0])
    #print rec
    # identify the part we need
    desiredID = re.split('q=related:', rec, 1)
    desiredID = str(desiredID[1])
    desiredID = desiredID[0:11] # 12 character Google Scholar unique ID
    return desiredID
    
#idWant = id_finder(searchStrings[0])
#print idWant

# TODO fix this function
def bib_getter(uniqID):
    domainStart = "http://scholar.google.com/scholar.bib?q=info:"
    domainMiddle = str(uniqID)
    domainEnd = ":scholar.google.com/scholar.bib?q=info:kirQZFDu-MYJ:scholar.google.com/&output=citation&hl=en&as_sdt=0,34&ct=citation&cd=0"
    domainCat = (str(domainStart), str(domainMiddle), str(domainEnd))
    domainFull = ''.join(domainCat)
    print domainFull

    pageSource = get_page_source(domainFull)
    print pageSource

idWant2 = 'UaAV4gWcL9c'
bib_getter(idWant2)



## SCRATCH:     
# http://www.r-bloggers.com/web-scraping-google-scholar-part-2-complete-success/
# https://bitbucket.org/fccoelho/scholarscrap/src/b5020c74d233/recipe-523047-1.py
# http://bmb-common.blogspot.com/2011/11/google-scholar-still-sucks.html
# http://www.cs.ox.ac.uk/people/stephen.kell/goodies/research/bibtex/
# http://asociologist.com/2012/01/02/google-scholar-scraper/
# On changing cookies: http://code.activestate.com/recipes/523047-search-google-scholar/

