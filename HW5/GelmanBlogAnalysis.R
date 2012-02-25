### Analysis of Andrew Gelman's Blog
### Data collected by Matt Dickenson
### R analysis by Matt Dickenson (mcdickenson@gmail.com)

setwd('/Users/mcdickenson/github/PS398/HW5/')
gelman <- read.csv('GelmanBlogScrapeFull.csv', header=T)
head(gelman)
plot(gelman$Length, gelman$Comments,xlim=c(0,4000),ylim=c(0,30))