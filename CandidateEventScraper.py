"""Campaign Trail Events
Washington Post
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/

# Which libraries do we need? 
import urllib2, re, time, csv
from nltk.util import clean_html
from BeautifulSoup import BeautifulSoup


# Which site do we want to scrape? 
page_to_scrape = 'http://projects.washingtonpost.com/2008-presidential-candidates/tracker/dates/'

# Which years we want?
startPage = 2007
endPage = 2008

# What info do we want? 
Headers = ["Date", "Person",  "Time", "EventType", "City", "State"]

# Open output file
nameFile = "CampaignTrail-"+str(startPage)+"-"+str(endPage)+".csv"
writeFile = open(nameFile,"wb")
csvwriter = csv.writer(writeFile)
csvwriter.writerow(Headers)

# Get all dates with events
mainpage = urllib2.urlopen(page_to_scrape)
mainsoup = BeautifulSoup(mainpage)
mainsoup.prettify()

eventPages = mainsoup.findAll("li","first")
events = []
for page in eventPages:
    url = re.search('href=".*?"',str(page.find("a")))
    #print url
    if str(url) != 'None':
        url = url.group(0)
        url = url.lstrip("href=")
        url = url.rstrip('"')
        url = url.lstrip('"')
        #print url
        events.append(url)

eventTotal = len(events)
eventCounter = 1
# Loop through events
for date in events:
    # Navigate to single post
    datePage = 'http://projects.washingtonpost.com' + str(date)
    try:
        date_page = urllib2.urlopen(datePage)
        time.sleep(1)
        text = BeautifulSoup(date_page)
        text.prettify()

        # Get Date
        eventDate = clean_html(str(text.find('h1'))) 
        eventDate = eventDate[10:]
        #print eventDate

        # Get Candidate Event Lists
        textDiv = text.findAll("div","ctEvent")
        #print textDiv[0]

        for divider in textDiv:

            # Get Candidate Name
            candidateName = clean_html(str(divider.find("h4")))
            eventList = divider.findAll("li")

            for event in eventList:
                # Get Event Time
                eventTime = clean_html(str(event.find("b")))

                # Get Type and State
                details = event.findAll("a")
                eventType = clean_html(str(details[0]))
                eventState = clean_html(str(details[1]))

                # Get City
                details2 = str(event)
                details2 = details2.split(',')[1]
                eventCity = details2.split(' in ')[1]
      
                # Write To CSV
                csvwriter.writerow([eventDate, candidateName, eventTime, eventType, eventCity, eventState])
    
        # Progress Bar
        print "Currently on page %s of %s" % (eventCounter, eventTotal)
        eventCounter += 1
    except: print "Page Skipped." 
    
writeFile.close()


