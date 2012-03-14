### Analysis of Blog Data
### Data collected by Anton Strezhnev and Matt Dickenson
### R analysis by Matt Dickenson (mcdickenson at gmail.com)
library(foreign)
setwd('/Users/mcdickenson/github/PS398/Monkey Cage/')
monkey1 <- read.dta('finalMonkeyCageData.dta')
setwd('/Users/mcdickenson/github/PS398/HW5/')
gelman <- read.csv('GelmanBlogScrapeFull.csv', header=T)
freak <- read.csv('FreakonomicsDataClean.csv', header=T)
behavior <- read.csv('ModeledBehaviorData-1-30.csv')

### Data Inspection and Cleanup
## Gelman
head(gelman)
plot(gelman$Length, gelman$Comments,xlim=c(0,4000),ylim=c(0,30))
gelman$Date <- as.character(gelman$Date)
gDateSplit <- strsplit(gelman$Date, ', ')
gDateSplit[[1]]
gelman$newdate <- c()
gelman$time <- c()
for(i in c(1:length(gDateSplit))){
  gelman[i, 'newdate'] <- gDateSplit[[i]][1]
  gelman[i, 'time'] <- gDateSplit[[i]][2]
}
head(gelman)
?as.Date
gelman$newdate <- as.Date(gelman$newdate, '%d %B %Y')
gelman$newdate
gelman$sincelast <- c()
for(i in c(1:nrow(gelman)-1)) {
  gelman[i, 'sincelast'] <- gelman[i, 'newdate'] - gelman[i+1, 'newdate']
}
gelman$sincelast # days since last post

gelman$weekdaynum <- format(gelman$newdate, "%w")
gelman$weekdaynum[1:6]
gelman$weekday01 <- as.numeric(0< gelman$weekdaynum & gelman$weekdaynum<6)
gelman$weekday01[1:20]
gelman$weekdaynum[1:20]

## Monkey Cage
head(monkey1)
# reworking date variable
strsplit(monkey1$date[1:2], '/')
temp_date <- matrix(unlist(strsplit(monkey1$date, '/')), nrow=length(monkey1$date), byrow=T)
head(temp_date)
monkey1$year <- temp_date[,3]
monkey1$day <- temp_date[,2]
monkey1$month <- temp_date[,1]
head(monkey1)
monkey1$newdate <- as.Date(monkey1$date, "%m/%d/%Y")
head(monkey1)
monkey1$weekday <- weekdays(monkey1$newdate)
monkey1$weekday[1]
monkey1$weekdaynum <- format(monkey1$newdate, "%w")
monkey1$weekdaynum[1:6]
monkey1$weekday01 <- as.numeric(0< monkey1$weekdaynum & monkey1$weekdaynum<6)
monkey1$weekday01[1:20]
monkey1$weekdaynum[1:20]

monkey1$sincelast <- c()
for(i in c(1:nrow(monkey1)-1)) {
  monkey1[i, 'sincelast'] <- monkey1[i, 'newdate'] - monkey1[i+1, 'newdate']
}
monkey1$sincelast
head(monkey1)

# Freakonomics
head(freak)
freak$Date <- as.character(freak$Date)
freak$Comments <- as.numeric(freak$Comments)
freak$Graphics <- as.numeric(freak$Graphics)
freak$Length <- as.numeric(freak$Length)
dateSplit <- strsplit(freak$Date, "\t")
head(dateSplit)
dateSplit[[1]][2]
x <- strsplit(dateSplit[[1]][2], " | ")
x
x[[1]][3]
x[[1]][4]
print(str(c(x[[1]][3], ' ', x[[1]][4])))
freak$Time <- c()
freak$pm <- c()
length(dateSplit)
for(i in c(1:length(dateSplit))) {
  dateTime <- strsplit(dateSplit[[i]][2], " | ")
  freak[i, "Date"] <- dateTime[[1]][1]
  freak[i, "Time"] <- dateTime[[1]][3]
  if(dateTime[[1]][4] == 'pm'){
    freak[i, 'pm'] <- 1
  }
  else {
    freak[i, 'pm'] <- 0  
    }
  
}
freak$Author <- as.character(freak$Author)
authorSplit <- strsplit(freak$Author, ' \n')
head(authorSplit)
head(freak)
for(i in c(1:length(authorSplit))) {
  freak[i, 'Author'] <- authorSplit[[i]][1]
}
head(freak)
freak$newdate <- as.Date(freak$Date, '%m/%d/%Y')
freak$sincelast <- c()
for(i in c(1:nrow(freak)-1)) {
  freak[i, 'sincelast'] <- freak[i, 'newdate'] - freak[i+1, 'newdate']
}
freak$sincelast

# weekday vs weekend
freak$weekdaynum <- format(freak$newdate, "%w")
freak$weekdaynum[1:6]
freak$weekday01 <- as.numeric(0< freak$weekdaynum & freak$weekdaynum<6)
freak$weekday01[1:20]
freak$weekdaynum[1:20]
# appears to be all-weekday

# Modeled Behavior
head(behavior)
behavior$Comments <- as.numeric(behavior$Comments)
behavior$Graphics <- as.numeric(behavior$Graphics)
behavior$Length <- as.numeric(behavior$Length)

behavior$fullDate <- paste(behavior$Day, behavior$Month, behavior$Year, sep="/")
behavior$fullDate
behavior$newdate <- as.Date(behavior$fullDate, '%d/%B/%Y')
behavior$sincelast <- c()
for(i in c(1:nrow(behavior)-1)) {
  behavior[i, 'sincelast'] <- behavior[i, 'newdate'] - behavior[i+1, 'newdate']
}
behavior$sincelast
head(behavior)

# weekend/weekday
behavior$weekdaynum <- format(behavior$newdate, "%w")
behavior$weekdaynum[1:6]
behavior$weekday01 <- as.numeric(0< behavior$weekdaynum & behavior$weekdaynum<6)
behavior$weekday01[1:20]
behavior$weekdaynum[1:20]

### making names consistent between mine and Anton's data
head(monkey1)
head(gelman)
colnames(monkey1)[9] <- "Comments"
colnames(monkey1)[12] <- "Graphics"
colnames(monkey1)[13] <- "Length"
head(monkey1)

### Variables of interest
# varname    # datasets   # what it is
# tweets     # monkey1    # count of tweets
# likes      # monkey1    # count of likes
# bin_tweet  # monkey1    # more tweets than likes (also bin_like)
# Comments   # all        # count of comments
# Graphics   # all        # count of images in post
# Length     # all        # word count
# newdate    # all        # R-formatted date
# weekday01  # all        # 1 if weekday, 0 if weekend
# sincelast  # all        # days since previous post

### Potential add'l variables:
# dummies for author (already in monkey1)
# dummies for category of post (already in monkey1)

### Descriptive stats
## Comments
par(mfrow=c(2,2))
plot(density(monkey1$Comments),main="Monkey Cage", xlab=expression(paste('N=860 ',mu==2.4,' ',sigma==2.4)))
plot(density(gelman$Comments, na.rm=T), main="Andrew Gelman", xlab=expression(paste('N=4215 ',mu==2.6,' ',sigma==2.8)))
plot(density(freak$Comments), main="Freakonomics", xlab=expression(paste('N=1289 ',mu==53.5,' ',sigma==34.7)))
plot(density(behavior$Comments), main="Modeled Behavior", xlab=expression(paste('N=1200 ',mu==6.4,' ',sigma==7.5)))
mean(monkey1$Comments) # 2.36
sd(monkey1$Comments) # 2.44
mean(gelman$Comments,na.rm=T) # 2.6
sd(gelman$Comments, na.rm=T) # 2.75
mean(freak$Comments) # 53.5
sd(freak$Comments)  # 34.7
mean(behavior$Comments) # 6.4
sd(behavior$Comments) # 7.45
## all of them seem to more or less fit a poisson distribution
## ie not too much under/overdispersion

## Length of post
four_densities = function(Variable_Vector, Name_Vector, Object_Lengths) {
  par(mfrow=c(2,2))
  for(i in c(1:length(Variable_Vector))) {
    object_to_plot <- Variable_Vector[1:Object_Lengths[i],i]
    mu_var = round(mean(object_to_plot, na.rm=T), digits=1)
    sig_var = round(sd(object_to_plot, na.rm=T), digits=1)
    plot(density(object_to_plot, na.rm=T), 
         main=Name_Vector[i], 
         xlab=bquote(paste(N==.(Object_Lengths[i]),' ', mu==.(mu_var),' ', sigma==.(sig_var)))
         )
         #xlab=substitute(expression(paste('N=', j, ' ', mu==k, ' ', sigma==l)), list(j=Object_Lengths[i], k=mu_var, l=sig_var)))
  }
}
# http://tolstoy.newcastle.edu.au/R/help/04/01/0967.html
post_lengths <- cbind(monkey1$Length, gelman$Length, freak$Length, behavior$Length)
blog_names <- c("Monkey Cage", "Andrew Gelman", "Freakonomics", "Modeled Behavior")
object_lengths <- c(860, 4215, 1289, 1200)
four_densities(post_lengths, blog_names, object_lengths)


post_intervals <- cbind(monkey1$sincelast, gelman$sincelast,freak$sincelast,behavior$sincelast)
four_densities(post_intervals, blog_names, object_lengths)

post_images <- cbind(monkey1$Graphics, gelman$Graphics, freak$Graphics, behavior$Graphics)
four_densities(post_images, blog_names, object_lengths)

### Subsetting to a common time interval
monkey1$newdate[860] # may 2011
gelman$newdate[635] # jan 31 2011
freak$newdate[1289] # jan 31 2011
behavior$newdate[1170] # jan 31 2011

# using '1' to indicate 1 year back
gelman1 <- gelman[1:635,]
freak1 <- freak
behavior1 <- behavior[1:1170,]

## redo plots
object_lengths1 <- c(860, 635, 1289, 1170)
post_comments1 <- cbind(monkey1$Comments, gelman1$Comments, freak1$Comments, behavior1$Comments)
#png(filename='PostCommentDens1.png', width=450, height=450,res=300)
four_densities(post_comments1, blog_names, object_lengths1)


post_lengths1 <- cbind(monkey1$Length, gelman1$Length, freak1$Length, behavior1$Length)
four_densities(post_lengths1, blog_names, object_lengths1)


post_intervals1 <- cbind(monkey1$sincelast, gelman1$sincelast,freak1$sincelast,behavior1$sincelast)
four_densities(post_intervals1, blog_names, object_lengths1)

post_images1 <- cbind(monkey1$Graphics, gelman1$Graphics, freak1$Graphics, behavior1$Graphics)
four_densities(post_images1, blog_names, object_lengths1)

### Getting pageview data
monkeyviews <- read.csv("/Users/mcdickenson/github/PS398/Monkey Cage/MCpageviews.csv", header=T)
head(monkeyviews)
# TODO: match up titles in monkey1 with titles in monkeyviews
# delete all older posts in monkeyviews than oldest post in monkey1
min(monkey1$newdate)
monkeyviews$Year <- as.character(monkeyviews$Year)
monkeyviews$Year <- as.numeric(monkeyviews$Year)
min(monkeyviews$Year, na.rm=T)
monkeyviews$Month <- as.character(monkeyviews$Month)
monkeyviews$Month <- as.numeric(monkeyviews$Month)
max(monkeyviews$Month, na.rm=T)
monkeyviews <- subset(monkeyviews, (Year==2011 & Month>=5) | (Year==2012))
head(monkeyviews)
monkeyviews$Day <- as.character(monkeyviews$Day)
monkeyviews$Day <- as.numeric(monkeyviews$Day)
mean(monkeyviews$Day, na.rm=T)
head(monkeyviews)
max(monkeyviews$Day, na.rm=T)
x <- sort(monkeyviews$Day)
x
monkeyviews <- subset(monkeyviews, (Day <= 31))
nrow(monkeyviews) # 444
monkeyviews$date <- c()
monkeyviews$date <- paste(monkeyviews$Day,monkeyviews$Month,monkeyviews$Year, sep='/')
head(monkeyviews)
monkeyviews$newdate <- as.Date(monkeyviews$date, '%d/%m/%Y')

monkeyviews$Visits <- as.character(monkeyviews$Visits)
monkeyviews$Visits <- as.numeric(monkeyviews$Visits)
monkeyviews$Pages.Visit <- as.character(monkeyviews$Pages.Visit)
monkeyviews$Pages.Visit <- as.numeric(monkeyviews$Pages.Visit)
monkeyviews$X..New.Visits <- as.character(monkeyviews$X..New.Visits)
monkeyviews$X..New.Visits <- as.numeric(monkeyviews$X..New.Visits)

### time to add pageview data to main data matrix
nrow(monkey1) # 860
monkey1$Visits <- rep(NA, 860)
monkey1$Pages <- rep(NA, 860)
monkey1$TimeOn <- rep(NA, 860)
monkey1$PercentNew <- rep(NA, 860)
monkey1$Top2000 <- rep(0, 860)
head(monkey1)

str(monkey1$title[1])
monkey1$newdate[1] == monkeyviews$newdate[1]
# cleaning up some unicode titles by visual inspection
monkey1$title[44] <- "Justice Stevens"
monkey1$title[61] <- "guy says Santorum's tax plan doesn't add up"
monkey1$title[101] <- ""
monkey1$title[102] <- "Moral Hazard in Authoritarian Repression and the Fate of Dictators"
monkey1$title[109] <- "statistically adrift?"
monkey1$title[145] <- "the 2012 US Presidential Elections"
monkey1$title[155] <- "Really Big Data Edition"
monkey1$title[177] <- "*"
monkey1$title[224] <- ""
monkey1$title[226] <- "nerdfight"
monkey1$title[250] <- ""
monkey1$title[249] <- ""
monkey1$title[257] <- ""
monkey1$title[263] <- "Technocratic Government!"
monkey1$title[274] <- "What does the Empirical Evidence Have to Say?"
monkey1$title[278] <- ""
monkey1$title[287] <- "than Republicans?"
monkey1$title[385] <- ""
monkey1$title[400] <- ""
monkey1$title[402]<- ""
monkey1$title[429]<- ""
monkey1$title[434] <- "Question"
monkey1$title[438]<- ""
monkey1$title[445]
monkey1$title[488] <- "with Ezra Klein"
monkey1$title[494] <- "Politician"
monkey1$title[499]<- ""
monkey1$title[511]<- ""
monkey1$title[517]<- ""
monkey1$title[561]<- ""
monkey1$title[596]<- ""
monkey1$title[649]<- ""
monkey1$title[655] <- "in International Relations Scholarship?"
monkey1$title[651]<- ""
monkey1$title[652] <- ""
monkey1$title[687]<- ""
monkey1$title[700] <- "Huh??"
monkey1$title[708] <- "I'd like to see a graph of relative change in death rates, with age on the x-axis"
monkey1$title[709]<- ""
monkey1$title[715]<- ""
monkey1$title[730] <- "that point in social scientists' papers where they pivot from a well-founded but narrow claim to a broad conclusion that is unsupported by theory or data"
monkey1$title[735]<- ""
monkey1$title[759] <- "a course for political science graduate students"
monkey1$title[758] <- ""
monkey1$title[773] <- "of a University of Illinois sociology professor"
monkey1$title[779]<- ""
monkey1$title[798]<- ""
monkey1$title[832]<- ""
monkey1$title[834]<- ""
monkey1$title[853]<- ""
monkeyviews$Title[117] <- "Iran's Dangerous Bluster Over The Strait of Hormuz"
monkeyviews$Title <- as.character(monkeyviews$Title)
monkeyviews$Title[132] <- "Why Aren't there Irb's For The Development Industry"
monkeyviews$Avg.Time.On <- as.character(monkeyviews$Avg.Time.On)
monkeyviews$Avg.Time.On[27]
x <- strsplit(monkeyviews$Avg.Time.On[27], ':')
as.integer(x[[1]][3])
monkey1$title <- as.character(monkey1$title)
substr(monkeyviews$Title[9], 1, 10)
substr(monkey1$title[2], 1, 10)
for(i in c(1:nrow(monkey1))) {
  print(i)
  for(j in c(1:nrow(monkeyviews))) {
    print(j)
    if(monkey1$newdate[i] == monkeyviews$newdate[j]) {
      if(substr(monkey1$title[i], 1, 10)==substr(monkeyviews$Title[j], 1, 10)) {
        monkey1$Visits[i] <- monkeyviews$Visits[j]
        monkey1$Pages[i] <- monkeyviews$Pages.Visit[j]
        timesplit <- strsplit(monkeyviews$Avg.Time.On[j], ':')
        seconds <- as.integer(timesplit[[1]][3])
        minutes <- as.integer(timesplit[[1]][2])
        monkey1$TimeOn[i] <- minutes*60 + seconds
        monkey1$Top2000[i] <- 1
      }
    }
  }
}

head(monkeyviews)
head(monkey1)
mean(monkey1$Top2000, na.rm=T) #27 percent of posts in monkey1 are in top 2000
mean(monkey1$TimeOn, na.rm=T) # mean reading time is 78.9 seconds
median(monkey1$TimeOn, na.rm=T) # 31.5


### Let's do some plotting
plot(density(monkey1$Visits, na.rm=T))
#par(mfrow=c(1,1))
fancy_density = function(Variable, Name, Color) {
  mu_var = round(mean(Variable, na.rm=T), digits=1)
  sig_var = round(sd(Variable, na.rm=T), digits=1)
  plot(density(Variable, na.rm=T), 
         main=Name, 
         xlab=bquote(paste(N==234,' ', mu==.(mu_var),' ', sigma==.(sig_var)))
         )
  polygon(density(Variable, na.rm=T), col=Color)
}
fancy_density(monkey1$Visits, "Visits")
# overdispersed poisson

plot(density(monkey1$TimeOn, na.rm=T))
fancy_density(monkey1$TimeOn, "Time On Page (Seconds)")
# overdispersed poisson
quantile(monkey1$TimeOn, .90, na.rm=T)

### Modeling
head(monkey1)
pageviews1.out<-glm(Visits~tweets+likes+Comments, data=monkey1,family="quasipoisson")
summary(pageviews1.out)
pageviews2.out<-glm(Visits~Comments, data=monkey1,family="quasipoisson")
summary(pageviews2.out)
#pageviews2.out<-glm()
cor(monkey1$Visits, monkey1$Comments, use="pairwise.complete.obs")

## scenario: 10 tweets/likes/comments, others held at 0
# dv: probability of being in top 2000 posts
top2k <- glm(Top2000 ~ tweets + likes + Comments, data = monkey1)
summary(top2k)
min(monkey1$Visits, na.rm=T) # 20 

# distribution of IV's
top2ktweets <- monkey1$tweets[monkey1$Top2000==1]
fancy_density(top2ktweets, "Tweets")
top2klikes <- monkey1$likes[monkey1$Top2000==1]
fancy_density(top2klikes, "Likes")
top2kcomments <- monkey1$Comments[monkey1$Top2000==1]
min(monkey1$Comments)
fancy_density(top2kcomments, "Comments")

# TODO: add color polygons
par(mfrow=c(2,2))
fancy_density(monkey1$Visits, "Page Views", 'grey')
fancy_density(top2ktweets, "Tweets", 'blue')
fancy_density(top2klikes, "Likes", 'red')
fancy_density(top2kcomments, "Comments", 'green')

# in scenarios, raise from 0 to mean
median(top2ktweets) # 8
median(top2klikes) # 7
median(top2kcomments) # 2
mean(monkey1$tweets) # 8.36
mean(monkey1$likes) # 6.67
mean(monkey1$Comments) # 2.35

scen0 <- matrix(c(0, 0, 0, 0), nrow=1)
scenT <- matrix(c(1, 8, 0, 0), nrow=1)
scenL <- matrix(c(1, 0, 7, 0), nrow=1)
scenC <- matrix(c(1, 0, 0, 2), nrow=1)
library(MASS)
library(stats)
top2k$coefficients[2]
top2k$vcov <- vcov(top2k)
top2k$vcov
top2k$vcov[2,2]

par(mfrow=c(1,1))
# set up matrix for predicted probabilities
pHatTop2k <- matrix(NA, nrow=1000, ncol=4)

# introduce uncertainty for coefficient on tweets
pTweetBetas <- mvrnorm(1000, mu=top2k$coefficients[2], Sigma=top2k$vcov[2,2])
pTweetBetas <-cbind(rep(top2k$coefficients[1],1000), pTweetBetas, rep(top2k$coefficients[3]), rep(top2k$coefficients[4]))
pTweetBetas <- matrix(pTweetBetas, nrow=1000, ncol=4)
head(pTweetBetas)
for (i in c(1:1000)) {
  pHatTop2k[i,1] <- (1/(1 + exp(-(pTweetBetas[i,] %*% t(scen0)))))
}
plot(density(pHatTop2k[,1])) # perfect uncertainty

for (i in c(1:1000)) {
  pHatTop2k[i,2] <- (1/(1 + exp(-(pTweetBetas[i,] %*% t(scenT)))))
}
plot(density(pHatTop2k[,2]))

pLikeBetas <- mvrnorm(1000, mu=top2k$coefficients[3], Sigma=top2k$vcov[3,3])
pLikeBetas <-cbind(rep(top2k$coefficients[1],1000), rep(top2k$coefficients[2]), pLikeBetas, rep(top2k$coefficients[4]))
pLikeBetas <- matrix(pLikeBetas, nrow=1000, ncol=4)
for (i in c(1:1000)) {
  pHatTop2k[i,3] <- (1/(1 + exp(-(pLikeBetas[i,] %*% t(scenL)))))
}
plot(density(pHatTop2k[,3]))

pCommentBetas <- mvrnorm(1000, mu=top2k$coefficients[4], Sigma=top2k$vcov[4,4])
pCommentBetas <- cbind(rep(top2k$coefficients[1],1000), rep(top2k$coefficients[2]), rep(top2k$coefficients[3]), pCommentBetas)
pCommentBetas <- matrix(pCommentBetas, nrow=1000, ncol=4)
for (i in c(1:1000)) {
  pHatTop2k[i,4] <- (1/(1 + exp(-(pCommentBetas[i,] %*% t(scenC)))))
}
plot(density(pHatTop2k[,4]))

plot(density(pHatTop2k[,2]), main="Pr(Page Views>20)", xlab="Overall probability=.27", ylim=c(0,200), col='blue', lwd=3)
polygon(density(pHatTop2k[,2]), col=rgb(0,0,255,100,maxColorValue=255), border=NULL)
polygon(density(pHatTop2k[,4]), col=rgb(0,255,0,100,maxColorValue=255), border=NULL)
lines(density(pHatTop2k[,4]), col='green', lwd=3)
polygon(density(pHatTop2k[,3]), col=rgb(255,0,0,100,maxColorValue=255), border=NULL)
lines(density(pHatTop2k[,3]), col='red', lwd=3)
 
### 3.7.12 analysis