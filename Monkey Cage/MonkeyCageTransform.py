import csv, os, sys

infile = "MonkeyCageData.csv"
openinfile = open(infile, "rb")

csvread = csv.reader(openinfile)

arrayOne = []
authorArray = []
topicArray = []

for line in csvread:
    if line[0] != "Post Number":
        arrayOne.append(line)
        author = line[6]
        if author not in authorArray:
            authorArray.append(author)
        
        categories = line[7]
        categories = categories.strip("[]")
        topics = categories.split(", ")
        for k in topics:
            item = k.strip("'")
            if item not in topicArray:
                topicArray.append(item)



HeaderArray = ["Post Num","Tweets","Likes","bin_Tweet","bin_Like","diff_Tweets_Likes","prop_Tweet","prop_Like","Comments","Title","Date","Graphics","Length","Videos","Grade Level"]

for m in authorArray:
    HeaderArray.append(m)

for k in topicArray:
    HeaderArray.append(k)

arrayTwo = []

for line in arrayOne:
    arrayEntry = []
    arrayEntry.append(line[0])
    arrayEntry.append(line[1])
    arrayEntry.append(line[2])
    if int(line[1]) > int(line[2]):
        arrayEntry.append("1")
        arrayEntry.append("0")
    elif int(line[1]) > int(line[2]):
        arrayEntry.append("0")
        arrayEntry.append("1")
    else:
        arrayEntry.append("0")
        arrayEntry.append("1")
        
    arrayEntry.append(int(line[1])-int(line[2]))
    if (int(line[1]) + int(line[2])) != 0:
        arrayEntry.append(float(line[1])/(int(line[1]) + int(line[2])))
        arrayEntry.append(float(line[2])/(int(line[1]) + int(line[2])))
    else:
        arrayEntry.append(".")
        arrayEntry.append(".")
    arrayEntry.append(line[3])
    arrayEntry.append(line[4])
    arrayEntry.append(line[5])
    arrayEntry.append(line[8])
    arrayEntry.append(line[9])
    arrayEntry.append(line[10])
    arrayEntry.append(line[11])
    author = line[6]
    for p in authorArray:
        if p == author:
            arrayEntry.append("1")
        else:
            arrayEntry.append("0")
    topics = line[7].strip("[]")
    topic = topics.split(", ")
    for o in range(len(topic)):
        topic[o] = topic[o].strip("'")
        
    for h in topicArray:
        if h in topic:
            arrayEntry.append("1")
        else:
            arrayEntry.append("0")

    arrayTwo.append(arrayEntry)

outfile = "MonkeyCageFinal.csv"
openoutfile = open(outfile,"wb")
csvwrite = csv.writer(openoutfile)

csvwrite.writerow(HeaderArray)
csvwrite.writerows(arrayTwo)

openoutfile.close()
openinfile.close()
