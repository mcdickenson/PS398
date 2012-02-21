# -*- coding: cp1252 -*-
import urllib2, urllib, datetime, re, string, os, csv, sys, os, time
import nltk
from cPAMIE import PAMIE
from BeautifulSoup import BeautifulSoup
import cookielib

# Flesch-Kincaid Grade level analysis of text.
# Borrowed From Ed Cranford at http://www.slumberheart.com/things/flesch_kincaid.py
import nltk
from nltk.corpus import cmudict
from re import match

cmu = cmudict.dict()
def syllable_count(word):
	reduced = reduce(word)
	if (not len(reduced)) or (not reduced in cmu):
		return 0
	return len([x for x in list(''.join(list(cmu[reduced])[-1])) if match(r'\d', x)])

def reduce(word):
	return ''.join([x for x in word.lower() if match(r'\w', x)])

def grade_level(text):
	sentences = nltk.tokenize.sent_tokenize(text)
	totalwords = 0
	totalsyllables = 0
	totalsentences = len(sentences)
	for sentence in sentences:
		words = nltk.tokenize.word_tokenize(sentence)
		words = [reduce(word) for word in words]
		words = [word for word in words if word != '']
		totalwords += len(words)
		syllables = [syllable_count(word) for word in words]
		totalsyllables += sum(syllables)
	totalwords = float(totalwords)
	return ( # Flesh-Kincaid Grade Level formula. Thanks, Wikipedia!
			0.39 * (totalwords / totalsentences)
			+ 11.8 * (totalsyllables / totalwords)
			- 15.59 )

# Start Actual Data Processing


# Define Number of Pages to be Scanned
startpage = 1
endPage = 100

# Define column headers
Headers = ["Post Number", "Tweets", "Likes", "Comments", "Title", "Date", "Author", "Categories", "Graphics", "Length", "Videos", "Grade Level"]

# Open output file

nameFile = "MonkeyCageData-"+str(startpage)+"-"+str(endPage)+".csv"
readFile = open(nameFile,"wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(Headers)

# Generate IE Client
ie = PAMIE()

# Initialize Post Counting
postCount = ((startpage-1)*10) + 1

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
        postTitle = re.sub("�",'"',re.sub("“",'"',re.sub("’","'",util.clean_html(str(soup.find("h1","entry-title"))))))

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
