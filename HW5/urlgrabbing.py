#First install BeautifulSoup: pip install BeautifulSoup
import urllib2
from BeautifulSoup import BeautifulSoup

#Open a webpage
webpage = urllib2.urlopen('http://yspr.wordpress.com') # comparable to open() in csvstuff.py
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
  
#Crawl the next 3 links?
