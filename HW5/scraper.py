"""Homework 4: Data Structures
Computational Frameworks, POLS 398
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/HW5/

# Which libraries do we need? 
import urllib2, urllib, datetime, re, string, os, csv, sys, os, time
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

# How many pages do we want?
startPage = 1
endPage = 172 # checked Gelman's max page count manually

# What info do we want? 
Headers = ["Post Number", "Tweets", "Likes", "Comments", "Title", "Date", "Author", "Categories", "Graphics", "Length", "Videos"]

# How do we want to store it? 
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


# Open output file

nameFile = "GelmanData-"+str(startpage)+"-"+str(endPage)+".csv"
readFile = open(nameFile,"wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(Headers)

postCounter = 1

# Loop through pages
for i in range(endPage - (startPage-1)):
pageNum = i + startpage

    # Navigate to the page
    #go(str(page_to_scrape)+'/page/'+str(pageNum)+"/")
    #time.sleep(1)
    #initialText = show()
    #soupA = BeautifulSoup(initialText)

    #Open the webpage
    current_page = str(page_to_scrape)+'/page/'+str(pageNum)+"/")
    time.sleep(1)
    webpage = urllib2.urlopen(current_page) # comparable to open() in csvstuff.py

    #Parse it
    soup = BeautifulSoup(webpage.read())
    soup.prettify()
        
    # Extract posts on a page
    headers = soup.findAll("h2","posttitle")
    
    posts = []
    for entry in headers:
        url = re.search('href=".*?"',str(entry.find("a"))).group(0)
        url = url.lstrip("href=")
        url = url.rstrip('"')
        url = url.lstrip('"')
        
        posts.append(url)

    # Loop through all posts on a page
    for postPage in posts:
        # Navigate to single post
        sub_page = urllib2.urlopen(postPage)
        
        
        time.sleep(1)
        text = show()
        soup = BeautifulSoup(text)

        #Get Title
        postTitle = re.sub("â",'"',re.sub("â",'"',re.sub("â","'",util.clean_html(str(soup.find("h1","title"))))))

        #Get Date

        postDate = str(soup.find("postdate")['span']) # not sure about this line

        # Get Categories
        postCategories = []
        categoryHeader = soup.findAll("span","postcat")[1]
        linkHeads = BeautifulSoup(str(categoryHeader)).findAll("a")
        for cat in linkHeads:
            postCategories.append(util.clean_html(str(cat)))
    
        # Get Author
        postAuthor = util.clean_html(str(soup.find("span","postauthor)))
        # Get Comments
        commentHeader = soup.findAll("a","#comments")[0]
    




