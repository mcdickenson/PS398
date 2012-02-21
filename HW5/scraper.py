"""Homework 4: Data Structures
Computational Frameworks, POLS 398
Spring 2012, Duke University
Matt Dickenson """
# /Users/mcdickenson/github/PS398/HW5/

# Load libraries
import urllib2
from BeautifulSoup import BeautifulSoup

# Optional: get user input 
page_to_scrape = raw_input("Enter the URL to scrape > ")
#page_to_scrape = 

#Open a webpage
webpage = urllib2.urlopen(page_to_scrape) # comparable to open() in csvstuff.py
#Parse it
soup = BeautifulSoup(webpage.read())
soup.prettify()

#Print out the target destinations for the links
print "Links\n********************"
for link in soup('a'):
    print str(link['href']) # prints the href attribute of the 'a' linkes in soup
  
print "Headers\n********************"
for header in soup(['h1', 'h2', 'h3']):
    print "{0}: {1}".format(header.name, header.string) # object.name gives you the 'h1', 'h2', or 'h3'; in our example above it would be 'a'


# How many pages do we want?
startpage = 1
endPage = 172 # check Gelman's max page count manually

# What info do we want? 
Headers = ["Post Number", "Tweets", "Likes", "Comments", "Title", "Date", "Author", "Categories", "Graphics", "Length", "Videos"]

# Open output file

nameFile = "GelmanData-"+str(startpage)+"-"+str(endPage)+".csv"
readFile = open(nameFile,"wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(Headers)

postCounter = 1

# Loop through every page
for i in range(endPage-(startpage-1)):
    pageNum = i + startpage

    # Navigate to the page
    ie.navigate("http://www.themonkeycage.org/page/"+str(pageNum)+"/")
    time.sleep(1)
    initialText = ie.pageGetText()
    soupA = BeautifulSoup(initialText)
    
    # Extract posts on a page
    headers = soupA.findAll("h2","entry-title")
    
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
        ie.navigate(postPage)
        time.sleep(1)
        text = ie.pageGetText()
        soup = BeautifulSoup(text)

        #Get Title
        postTitle = re.sub("â",'"',re.sub("â",'"',re.sub("â","'",util.clean_html(str(soup.find("h1","entry-title"))))))

        #Get Date

        postDate = str(soup.find("abbr", "published")["title"])

        # Get Categories
        postCategories = []
        categoryHeader = soup.findAll("p","headline_meta")[1]
        linkHeads = BeautifulSoup(str(categoryHeader)).findAll("a")
        for cat in linkHeads:
            postCategories.append(util.clean_html(str(cat)))
    
        # Get Author
        postAuthor = util.clean_html(str(soup.find("span","author vcard fn")))
        # Get Comments
        commentHeader = soup.findAll("p","headline_meta")[0]
        NumComments = re.search("[0-9]+? comment",util.clean_html(str(commentHeader))).group(0)
        postNumComments = int(re.search("[0-9]+?",NumComments).group(0))
        postNumber = postCount

        # Get Images
        textDiv = soup.find("div","format_text entry-content")
        textSearch = BeautifulSoup(str(textDiv))
        postImgCount = len(textSearch.findAll("img")) - 1
        
        # Get Word Count
        cleanText = util.clean_html(str(textDiv))
        words = cleanText.split()
        postWordCount = len(words)

        # Get Grade Level
        postGradeLevel = grade_level(cleanText)

        # Get Video Count
        postVidCount = 0
        for frame in textSearch.findAll("iframe"):
            if re.search("youtube",frame["src"]) != None:
                postVidCount += 1
                
        # Download Text
        minFile = open(str(postNumber)+".txt","wb")
        minFile.write(cleanText)
        minFile.close()

        postCount += 1
        # Get Twitter and Facebook Counts
        for iframe in soup.findAll('iframe'):
            #Twitter Button
            try:
                if iframe["title"] == "Twitter Tweet Button":
                   ie.navigate(str(iframe["src"]))
                   time.sleep(1)
                   tweetText = ie.pageGetText()
                   try:
                       tweet = re.search("This page has been shared [0-9]+? times",tweetText).group(0)

                       tweetCount = int(re.search("[0-9]+",tweet).group(0))
                       
                   except:
                       tweetCount = 0
                       
            except:
                pass
            #Facebook Button
            try:
                if re.search("facebook",str(iframe)) != None and iframe["scrollbars"] == "no" :
                   ie.navigate(str(iframe["src"]))
                   time.sleep(1)
                   fbText = ie.pageGetText()
                   fbSoup = BeautifulSoup(fbText)
                   
                   widgetVals = fbSoup.findAll("div","connect_widget_button_count_count")
                   likeCount = int(util.clean_html(str(widgetVals[1])))
                   
            except:
                pass

        # Write To CSV
        csvwriter.writerow([postNumber, tweetCount, likeCount, postNumComments, postTitle, postDate, postAuthor, postCategories, postImgCount, postWordCount, postVidCount, postGradeLevel])
        
readFile.close()
