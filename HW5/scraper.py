# -*- coding: cp1252 -*-
"""Homework 4: Data Structures
Computational Frameworks, POLS 398
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/HW5/

# Which libraries do we need? 
import urllib2, urllib, datetime, re, string, os, csv, sys, os, time
#from nltk import util
import nltk
from nltk import util
from nltk.util import clean_html
import cookielib
from twill import get_browser
from BeautifulSoup import BeautifulSoup
# http://doc.scrapy.org/en/latest/intro/overview.html
from scrapy.item import Item, Field

# Which site do we want to scrape? 
# Optional: get user input 
# page_to_scrape = raw_input("Enter the URL to scrape > ")
# expected input: http://www.thisIsASite.com/
page_to_scrape = 'http://andrewgelman.com/'

# What is the domain name of that site?
remove_http = page_to_scrape.split('//')[-1]
remove_final_slash  = remove_http.rstrip('/')
domainName = remove_final_slash

# How many pages do we want?
startPage = 1
endPage = 3 # checked Gelman's max page count manually: 172

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

nameFile = "GelmanData-"+str(startPage)+"-"+str(endPage)+".csv"
readFile = open(nameFile,"wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(Headers)

postCounter = 1

# Loop through pages
for i in range(endPage - (startPage-1)):
    pageNum = i + startPage

    # Navigate to the page
    #go(str(page_to_scrape)+'/page/'+str(pageNum)+"/")
    #time.sleep(1)
    #initialText = show()
    #soupA = BeautifulSoup(initialText)

    #Open the webpage
    current_page = str(page_to_scrape)+'/page/'+str(pageNum)+"/"
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
        text = BeautifulSoup(sub_page.read())
        text.prettify()
        
        #Get Title
        postTitle = re.sub("â",'"',re.sub("â",'"',re.sub("â","'",clean_html(str(text.find("h1","title"))))))

        #Get Date

        postDate = str(text.find("postdate",'span')) # not sure about this line

        # Get Categories
        postCategories = []
        categoryHeader = text.findAll("span","postcat")
        linkHeads = BeautifulSoup(str(categoryHeader)).findAll("a")
        for cat in linkHeads:
            postCategories.append(clean_html(str(cat)))
    
        # Get Author
        postAuthor = clean_html(str(text.find("span","postauthor")))

        # Get Comments # TODO: FIX THIS
        #commentHeader = text("a")

        #NumComments = re.search("[0-9]+? comment",clean_html(str(commentHeader)))
        #NumComments = NumComments.group(0)
        #postNumComments = int(re.search("[0-9]+?",NumComments).group(0))
        #postNumber = postCounter

        # Get Images
        textDiv = text.find("div","p")
        textSearch = BeautifulSoup(str(textDiv))
        postImgCount = len(textSearch.findAll("img")) - 1
        
        # Get Word Count
        cleanText = clean_html(str(textDiv))
        words = cleanText.split()
        postWordCount = len(words)

        # Get Video Count
        #postVidCount = 0
        #for frame in textSearch.findAll("iframe"):
        #    if re.search("youtube",frame["src"]) != None:
        #        postVidCount += 1
                
        # Write To CSV
        #csvwriter.writerow([postNumber, postNumComments, postTitle, postDate, postAuthor, postCategories, postImgCount, postWordCount, postVidCount])
        csvwriter.writerow([postCounter, postTitle, postDate, postAuthor, postCategories, postImgCount, postWordCount])

        postCounter += 1
    


readFile.close()

