### Analysis of Monkey Cage popularity data
### Data collected by ANTON STREZHNEV
### R analysis by MATT DICKENSON (mcdickenson@gmail.com)

library(foreign)
setwd('/Users/mcdickenson/github/PS398/Monkey Cage/')
# setwd('get your own')
monkey1 <- read.dta('finalMonkeyCageData.dta')

head(monkey1)

# visual exploration
plot(density(monkey1$tweets))
plot(density(monkey1$likes))
plot(density(monkey1$prop_tweet, na.rm=T))
plot(density(monkey1$prop_like, na.rm=T))

plot(monkey1$tweets, col='blue')
points(monkey1$likes, col='red')
points(monkey1$comments)

plot(monkey1$tweets, col=monkey1$has_graphics+1)
plot(monkey1$likes, col=monkey1$has_graphics+1) # better predictor

plot(monkey1$date, monkey1$tweets)

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

# back to plotting 
plot(monkey1$newdate, monkey1$tweets, col='blue')
points(monkey1$newdate, monkey1$likes, col='red')

# is day of the week relevant?

day_abbr_list <- c("Sun","Mon","Tue","Wed","Thu","Fri","Sat")

par(mfrow=c(3,1))

plot(monkey1$weekdaynum, monkey1$tweets, col='blue', xaxt='n',xlab='',ylab="Tweets (blue) and Likes (red)")
axis(1,labels=day_abbr_list, at=c(0,1,2,3,4,5,6))
points(monkey1$weekdaynum, monkey1$likes, col='red')


boxplot(monkey1$tweets ~ monkey1$weekdaynum, xaxt='n',xlab='',ylab="Tweets",col='blue')
axis(1,labels=day_abbr_list, at=c(1,2,3,4,5,6,7))
# M,W,R

boxplot(monkey1$likes ~ monkey1$weekdaynum, xaxt='n',xlab='',ylab="Likes",col='red')
axis(1,labels=day_abbr_list, at=c(1,2,3,4,5,6,7))
# M,W,F

boxplot(monkey1$comments ~ monkey1$weekdaynum,xlab='',xaxt='n',ylab="Comments",col='green')
axis(1,labels=day_abbr_list, at=c(1,2,3,4,5,6,7))
# M,W,S

# weekday vs. weekend
par(mfrow=c(1,1))
boxplot(monkey1$tweets ~ monkey1$weekday01,xlab='',, xaxt='n', ylab="Tweets",col='blue')
axis(1,labels=c("Weekend","Weekday"), at=c(1,2))

boxplot(monkey1$likes ~ monkey1$weekday01,xlab='',, xaxt='n', ylab="Likes",col='red')
axis(1,labels=c("Weekend","Weekday"), at=c(1,2))

boxplot(monkey1$comments ~ monkey1$weekday01,xlab='',, xaxt='n', ylab="Comments",col='green')
axis(1,labels=c("Weekend","Weekday"), at=c(1,2))

# model exploration
head(monkey1)
?glm
predTweets <- glm(bin_tweet ~ length + gradelevel + johnsides + andrewgelman + weekday01, data=monkey1)
summary(predTweets)
predTweets <- binreg(c(monkey1$length, monkey1$gradelevel, monkey1$johnsides,monkey1$andrewgelman,monkey1$weekday01), monkey1$bin_tweet)
predTweets

predLikes <- glm(bin_like ~ length + gradelevel + johnsides + andrewgelman + weekday01, data=monkey1)
summary(predLikes)

monkey1$comment01 <- as.numeric(monkey1$comment > 0) 
predComments <- glm(comment01 ~ length + gradelevel + johnsides + andrewgelman + weekday01, data=monkey1)
summary(predComments)

# six scenarios: John Sides, Andrew Gelman, everyone else; weekend/not
pHatTweet <- matrix(NA, nrow=1000, ncol=6)
pHatLike <- matrix(NA, nrow=1000, ncol=6)
pHatComment <- matrix(NA, nrow=1000, ncol=6)
scen1 <- matrix(c(1, mean(monkey1$length), mean(monkey1$gradelevel), 1, 0, 0),nrow=1) # sides, weekend
head(scen1)
scen2 <- matrix(c(1, mean(monkey1$length), mean(monkey1$gradelevel), 0, 1, 0), nrow=1) # gelman, weekend
head(scen2)
scen3 <- matrix(c(1, mean(monkey1$length), mean(monkey1$gradelevel), 0, 0, 0), nrow=1) # avg weekend

# weekdays
scen4 <- matrix(c(1, mean(monkey1$length), mean(monkey1$gradelevel), 1, 0, 1), nrow=1) # sides, weekday
scen5 <- matrix(c(1, mean(monkey1$length), mean(monkey1$gradelevel), 0, 1, 1), nrow=1) # gelman, weekday
scen6 <- matrix(c(1, mean(monkey1$length), mean(monkey1$gradelevel), 0, 0, 1), nrow=1) # avg weekday

#scenarios <- cbind(rep(scen1,1000), rep(scen2,1000), rep(scen3,1000), rep(scen6,1000), rep(scen7,1000), rep(scen8,1000))
#head(scenarios)
#nrow(scenarios)
library(MASS)
predTweets$coefficients
predTweets$coefficients[1]
predTweets$coefficients[4]
predTweets$coefficients[5]
library(stats)
predTweets$vcov <- vcov(predTweets)
predTweets$vcov[4,4]
pTweetBetas <- mvrnorm(1000, mu=predTweets$coefficients[4], Sigma=predTweets$vcov[4,4])
pTweetBetas <-cbind(rep(predTweets$coefficients[1],1000),rep(predTweets$coefficients[2],1000),rep(predTweets$coefficients[3],1000), pTweetBetas, rep(0,1000), rep(0,1000))
pTweetBetas <- matrix(pTweetBetas, nrow=1000, ncol=6)
for (i in c(1:1000)) {
  pHatTweet[i,1] <- (1/(1 + exp(-(pTweetBetas[i,] %*% t(scen1)))))
}
# plot of probability that a post by John Sides gets tweeted more than liked
plot(density(pHatTweet[,1]), main="Pr(#Tweets>#Likes|Author=JS)")

head(pHatTweet)
dim(scen1)
dim(pTweetBetas)
pTweetBetas[1,]
pTweetBetas[1,] %*% t(scen1)
t(scen1)

predTweets$coefficients[5] 
predTweets$vcov[5,5]
pTweetBetas2 <- mvrnorm(1000, mu=predTweets$coefficients[5], Sigma=predTweets$vcov[5,5])
head(pTweetBetas2)
pTweetBetas2 <-cbind(rep(predTweets$coefficients[1],1000),rep(predTweets$coefficients[2],1000),rep(predTweets$coefficients[3],1000), rep(0,1000), pTweetBetas2, rep(0,1000))
pTweetBetas2 <- matrix(pTweetBetas, nrow=1000, ncol=6)

for (i in c(1:1000)) {
  pHatTweet[i,2] <- (1/(1 + exp(-(pTweetBetas2[i,] %*% t(scen2)))))
}
dim(t(scen2))
plot(density(pHatTweet[,2]))
lines(density(pHatTweet[,1]))

plot(density(pHatTweet[,1]))
lines(density(pHatTweet[,2]))


pTweetBetas3 <-cbind(rep(predTweets$coefficients[1],1000),rep(predTweets$coefficients[2],1000),rep(predTweets$coefficients[3],1000), rep(0,1000), rep(0,1000), rep(0,1000))
pTweetBetas3 <- matrix(pTweetBetas, nrow=1000, ncol=6)

for (i in c(1:1000)) {
  pHatTweet[i,3] <- (1/(1 + exp(-(pTweetBetas3[i,] %*% t(scen3)))))
}
plot(density(pHatTweet[,3]))

min(monkey1$newdate)

# weekday scenarios

pTweetBetas4 <- mvrnorm(1000, mu=predTweets$coefficients[4], Sigma=predTweets$vcov[4,4])
pTweetBetas4 <-cbind(rep(predTweets$coefficients[1],1000),rep(predTweets$coefficients[2],1000),rep(predTweets$coefficients[3],1000), pTweetBetas4, rep(0,1000), rep(1,1000))
pTweetBetas4 <- matrix(pTweetBetas, nrow=1000, ncol=6)
for (i in c(1:1000)) {
  pHatTweet[i,4] <- (1/(1 + exp(-(pTweetBetas4[i,] %*% t(scen4)))))
}
plot(density(pHatTweet[,4]))
lines(density(pHatTweet[,1])) # no difference


pTweetBetas5 <- mvrnorm(1000, mu=predTweets$coefficients[5], Sigma=predTweets$vcov[5,5])
pTweetBetas5 <-cbind(rep(predTweets$coefficients[1],1000),rep(predTweets$coefficients[2],1000),rep(predTweets$coefficients[3],1000), rep(0,1000), pTweetBetas5, rep(1,1000))
pTweetBetas5 <- matrix(pTweetBetas, nrow=1000, ncol=6)

for (i in c(1:1000)) {
  pHatTweet[i,5] <- (1/(1 + exp(-(pTweetBetas5[i,] %*% t(scen2)))))
}
plot(density(pHatTweet[,5]))
lines(density(pHatTweet[,2]))

# the weekday/weekend comparisons are uninteresting


### 2-20-12
# John was kind enough to send me Google Analytics data on top 2k posts
# library(foreign)
# setwd()
top2k <- read.csv("MonkeyCageTop2K.csv", header=T)
head(top2k)
head(monkey1)
plot(top2k$Visits)

# getting month and year
# reworking date variable
temp <- strsplit(as.character(top2k$Landing.Page), '/')
temp
top2k$year <- NA
top2k$month <- NA
top2k$date <- NA
for (i in c(1:nrow(top2k))) {
  top2k$year[i] <- temp[[i]][2]
  top2k$month[i] <- temp[[i]][3]
}
temp[[5]][2]
temp[[5]][3]
head(top2k)
top2k$date <- paste(top2k$year, ".", top2k$month, sep="")
head(top2k)
top2k$date <- as.numeric(top2k$date)
head(top2k)
nrow(top2k)

# # trouble below...
# top2k$dateMY <- paste(top2k$month, "/", top2k$year, sep="")
# top2k$dateMY[2:1997]
# top2k$date
# as.Date(top2k$dateMY[2], format="%m/%Y")
# top2k$newdate <- as.Date(as.character(top2k$date), format="%Y.%m")
# class(top2k$dateMY)
# head(top2k)
# top2k$year
# 
# for (i in c(1:nrow(top2k))) {
#   if ((top2k$year[i] != 'blog') & (top2k$year[i] != NA) & (top2k$year[i] != 'ugavi.jpg')) {
#     top2k$newdate[i] <- as.Date(as.character(top2k$date[i]), format="%Y.%m")
#   }
# }
# 
# 
# plot(top2k$date, top2k$Visits)

# more trouble...
top2k$day <- c()
for (i in c(1:nrow(top2k))) {
    top2k$year[i] <- temp[[i]][3]
    top2k$month[i] <- temp[[i]][4]
    top2k$day[i] <- temp[[i]][5]

}

