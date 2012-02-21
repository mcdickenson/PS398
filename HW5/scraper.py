"""Homework 4: Data Structures
Computational Frameworks, POLS 398
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/HW5/

# Which libraries do we need? 
import urllib2
from BeautifulSoup import BeautifulSoup
# http://doc.scrapy.org/en/latest/intro/overview.html
from scrapy.item import Item, Field

# Which site do we want to scrape? 
# Optional: get user input 
page_to_scrape = raw_input("Enter the URL to scrape > ")
# expected input: http://www.thisIsASite.com/
#page_to_scrape = aWebSite

# What is the domain name of that site?
remove_http = page_to_scrape.split('//')[-1]
remove_final_slash  = remove_http.rstrip('/')
domainName = remove_final_slash


#Open the webpage
webpage = urllib2.urlopen(page_to_scrape) # comparable to open() in csvstuff.py

#Parse it
soup = BeautifulSoup(webpage.read())
soup.prettify()

# How many pages do we want?
startpage = 1
endPage = 172 # checked Gelman's max page count manually

# What info do we want? 
Headers = ["Post Number", "Tweets", "Likes", "Comments", "Title", "Date", "Author", "Categories", "Graphics", "Length", "Videos"]

class Post(Item):
    url = Field()
    name = Field()
    tweets = Field()
    likes = Field()
    comments = Field()
    title = Field()
    date = Field()
    author = Field()
    categories = Field()
    graphics = Field()
    length = Field()
    videos = Field()

class myCrawler(CrawlSpider):
    name = domainName
    allowed_domains = [domainName]
    start_urls = page_to_scrape
    rules = [Rule(SgmlLinkExtractor(allow=['/page/\d+']), 'parse_torrent')]

    def parse_post(self, response):
        x = HtmlXPathSelector(response)

        post = Post()
        post['url'] = response.url
        post['name'] = x.select("//h1/text()").extract()
        post['description'] = x.select("//div[@id='description']").extract()

        
        post['size'] = x.select("//div[@id='info-left']/p[2]/text()[2]").extract()
        return torrent


# Open output file

nameFile = "GelmanData-"+str(startpage)+"-"+str(endPage)+".csv"
readFile = open(nameFile,"wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(Headers)

postCounter = 1


