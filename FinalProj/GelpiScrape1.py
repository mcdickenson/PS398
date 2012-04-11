"""Chris Gelpi Web Scrape
Final Project Draft
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/FinalProj

# Which libraries do we need? 
import urllib2, urllib, datetime, re, string, time, csv
from xml.sax.saxutils import unescape
import nltk
from nltk import util
from nltk.util import clean_html
import cookielib
from twill import get_browser
from BeautifulSoup import BeautifulSoup


# Which site/page do we want to scrape? 
page_to_scrape = 'http://duke.edu/~gelpi/309SPCCoreSpring11.htm'

# What is the name of this course (for output file)?
course_name = 'SPCcore'

# What info do we want? 
Headers = ["Author","Year","Title","Journal/Publisher", "SearchString"]

# Open output file
nameFile = "CampaignTrail-"+str(course_name)+".csv"
writeFile = open(nameFile,"wb")
csvwriter = csv.writer(writeFile)
csvwriter.writerow(Headers)

# Get HTML of main page
mainpage = urllib2.urlopen(page_to_scrape)
mainsoup = BeautifulSoup(mainpage)
mainsoup.prettify()
#print mainsoup

# Citations are identified by <p> tags with the following style:

# Search for citations
paragraphs = mainsoup.findAll("p",'MsoNormal')
print len(paragraphs)

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



# Loop thru actual citations, get info
for cite in citations:
    # Clean cite of HTML tags and '&quot'
    cite2 = clean_html(str(cite))
    cite3 = cite2.replace('&quot;', '') # TODO: use this as information
    cite3 = cite3.split('.')
    #print cite3
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

        # Create string to be searched in Google Scholar
        toSearch = authorName + ' ' + pubYear + ' ' + workTitle

        # Write to CSV
        csvwriter.writerow([authorName, pubYear, workTitle, journPub, toSearch])

        # Update progress
        numSuccessful += 1
        numChecked = numErrors + numSuccessful
        print "Completed %s of %s. %s successful, %s failures." % (numChecked, numTotal, numSuccessful, numErrors)

    except:
        numErrors += 1
        numChecked = numErrors + numSuccessful
        print "Completed %s of %s. %s successful, %s failures." % (numChecked, numTotal, numSuccessful, numErrors)
