# SIPRI Data Cleanup
# Final Project Draft
# Spring 2012, Duke University
# Matt Dickenson 

# clear workspace
rm(list=ls())

# load packages
library(foreign)

# read Sipri Suppliers txt file
sipsup <- read.delim2('/Users/mcdickenson/Data/SIPRI/Trade-Register-1950-2011-Suppliers.txt', 
                      header = TRUE, sep = "\t", quote="", dec=",",
                      fill = TRUE, comment.char="", blank.lines.skip=T,
                      row.names=NULL)

head(sipsup)
colnames(sipsup) <- c('countries','Supplier',"NumOrdered","WeaponType","WeaponDesc","YearOrdered","YearDelivered","NumDelivered","Comments")
head(sipsup)

sipsup <- sipsup[-c(1:4),]
head(sipsup)

colnames(sipsup) <- c('Supplier',"NumOrdered","WeaponType","WeaponDesc","YearOrdered","YearDelivered","NumDelivered","Comments")
head(sipsup)
row.names(sipsup) <- c(1:nrow(sipsup))
sipsup2 <- cbind(sipsup$Supplier, matrix(NA, ncol=1, nrow=nrow(sipsup)), sipsup[,c(2:9)])
head(sipsup2)

colnames(sipsup2) <- c('Supplier','Receiver',"NumOrdered","WeaponType","WeaponDesc","YearOrdered","YearDelivered","NumDelivered","Comments")
head(sipsup2)

class(sipsup2[,1])
sipsup2[,1] <- as.character(sipsup2[,1])
temp <- sipsup2[2,1]
nchar(temp)
checkText <- substr(temp,1,3)
checkText=="R: "
keepText <- substr(temp,4,nchar(temp))
keepText

dim(sipsup2)

for(i in c(1:nrow(sipsup2))){
  temp <- sipsup2[i,1]
  checkText <- substr(temp,1,3)
  if(checkText == "R: "){
    keepText <- substr(temp,4,nchar(temp))
    sipsup2[i-1,2] <- keepText
    sipsup2[i-1,3:10] <- sipsup2[i,3:10]
  }
}

# PROBLEM: "R: " only shows up for the first recipient
# SOLUTION: have a true/false item about whether to carry up
# when it reaches a "R: " it is set to true, when it reaches a blank it is set to false

head(sipsup2)
sipsup2[1:100,1:3]
not.want <- which(is.na(sipsup2[,2]))
