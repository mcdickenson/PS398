### Cleanup Monkey Cage Pageviews
import csv

# Setup input and output files
Headers = ["Landing Page","Visits","Pages/Visit","Avg Time On", "% New Visits", "Bounce Rate", "Year", "Month", "Day", "Title"]
nameOutput = "MCpageviews.csv"
outputFile = open(nameOutput,"ab")
csvwriter = csv.writer(outputFile)
csvwriter.writerow(Headers)
nameInput = "MonkeyCageTop2K.csv"
inputFile = open(nameInput,"rU")
csvreader = csv.reader(inputFile)

for row in csvreader:
    print row
    if row[0] == 'Landing Page' or row[0] == '/':
        pass
    else:
        landing = row[0]
        visits = row[1]
        pgpervisit = row[2]
        avgtime = row[3]
        percentnew = row[4]
        bounces = row[5]
        cleanpage = landing.lstrip('/blog') # remove leading characters
        cleanpage = cleanpage.rstrip('.html') # remove trailing characters
        cleanpage = cleanpage.split('/')
        print ("Clean page: ", cleanpage) 
        year = cleanpage[0]
        try:
            month = cleanpage[1]
            if len(cleanpage) == 3:
                day = 'NA'
                title = str(cleanpage[2])
            elif len(cleanpage) >= 4:
                day = cleanpage[2]
                title = cleanpage[3]   
            print ("Title: ", title)
            if '-' in title:
                title = title.split('-')
            else: 
                title = title.split('_')
            newtitle = ''
            for word in title:
                word = word.capitalize()
                newtitle = newtitle + str(word) + ' '
            newtitle = newtitle.rstrip(' ')
        except: 
            month, day, newtitle = 'NA', 'NA', 'NA'
        csvwriter.writerow([landing, visits, pgpervisit, avgtime, percentnew, bounces, year, month, day, newtitle])

inputFile.close()
outputFile.close()
