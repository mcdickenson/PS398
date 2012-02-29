# -*- coding: cp1252 -*-
"""Homework 5: Blog Scraping
Computational Frameworks, POLS 398
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/HW5/

# Which libraries do we need? 
import urllib2, urllib, datetime, re, csv, time
#from nltk import util
import nltk
from nltk import util
from nltk.util import clean_html
from BeautifulSoup import BeautifulSoup


# Which site do we want to scrape? 
# Optional: get user input 
# page_to_scrape = raw_input("Enter the URL to scrape > ")
# expected input: http://www.thisIsASite.com/
page_to_scrape = 'http://www.modeledbehavior.com/'

# How many pages do we want?
startPage = 1
endPage = 30 # 30 is enough to go back 1 year

# What info do we want? 
Headers = ["Post Number", "Title", "Weekday", "Date", "Month", "Day", "Year", "Author", "Categories", "Graphics", "Length","Comments", "Tweets"]


# Open output file

nameFile = "ModeledBehaviorData-"+str(startPage)+"-"+str(endPage)+".csv"
readFile = open(nameFile,"wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(Headers)

postCounter = 1

# Loop through pages
for i in range(endPage - (startPage-1)):
    pageNum = i + startPage

    #Open the webpage
    current_page = str(page_to_scrape)+'/page/'+str(pageNum)+"/"
    time.sleep(1)
    webpage = urllib2.urlopen(current_page) 

    #Parse it
    soup = BeautifulSoup(webpage.read())
    soup.prettify()
        
    # Extract posts on a page
    headers = soup.findAll("h2")
    
    posts = []
    for entry in headers[0:40]:
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
        # postTitle = re.sub("â",'"',re.sub("â",'"',re.sub("â","'",clean_html(str(text.find("h3"))))))
        postTitle = clean_html(str(text.find('h1','post-title'))) 

        #Get Date
        metadata = clean_html(str(text.find('p','post-metadata')))
        metadata = metadata.partition(' ~ ')
        postWeekday = metadata[0]
        metaPartition = metadata[2].partition(' in ')
        postDate = metaPartition[0]
        postDatePartition = postDate.split(' ')
        postMonth = postDatePartition[0]
        postDay = postDatePartition[1].rstrip(',sthrnd')
        postYear = postDatePartition[2]

        # Get Categories
        #postCategories = []
        #categoryHeader = text.findAll("a","category tag")
        #linkHeads = BeautifulSoup(str(categoryHeader)).findAll("a")
        #for cat in linkHeads:
        #    postCategories.append(clean_html(str(cat)))
        metaPartition2 = metaPartition[2]
        metaPartition2 = metaPartition2.rpartition(' | by ')
        postCategories = metaPartition2[0]
    
        # Get Author
        #postAuthor = clean_html(str(text.find("li","postmeta-author")))
        #postAuthor = clean_html(str(text.find("a","author")))
        postAuthor = metaPartition2[2]

        # Get Comments
        #postNumComments = re.sub("â",'"',re.sub("â",'"',re.sub("â","'",clean_html(str(text.find("h3"))))))
        commentDiv = text.find("h2", "comments-title")
        postNumComments = clean_html(str(commentDiv))
        postNumComments = postNumComments.rpartition(" comment")[0]
        
        
        # Get Images
        textDiv = text.find("div", "post-content")
        textSearch = BeautifulSoup(str(textDiv))
        postImgCount = len(textSearch.findAll("img"))

        # Get Tweet count
        tweetDiv = text.find("div", "widget widget_twitter")
        tweetSearch = BeautifulSoup(str(tweetDiv))
        postTweetCount = len(tweetSearch.findAll("li"))
        
        # Get Word Count
        postText = clean_html(str(textDiv))
        words = postText.split()
        postWordCount = len(words)
                
        # Write To CSV
        csvwriter.writerow([postCounter, postTitle, postWeekday, postDate, postMonth, postDay, postYear, postAuthor, postCategories, postImgCount, postWordCount, postNumComments, postTweetCount])

        # Progress Bar
        print "Currently on post %d, page %d. Total of %d posts, %d pages." % (postCounter, pageNum, 40*(endPage-startPage+1), (endPage-startPage+1))
        postCounter += 1
    
readFile.close()

