### Graphing times of 3 sort algorithms
### Generated for POLS 398 by sorter_times.py
### Fall 2012, Matt Dickenson, Duke University

times <- read.csv("/Users/mcdickenson/github/PS398/HW3/times.csv", header = F)
head(times)
colnames(times) <- c("N", "Selection", "Bubble", "Quick")
head(times)
plot(times$N, times$Bubble, type="l", ylab="Milliseconds", xlab="Length of Sorted List", col="blue",yaxt='n')
axis(2,las=2, labels = c("0","5","10", "15", "20"), at = c(0.000, 0.005, 0.010, 0.015, 0.020))
lines(times$N, times$Selection)
lines(times$N, times$Quick, col="red")
text(250, 0.020, labels="Bubble", pos=2, col="blue")
text(250, 0.006, labels="Selection", pos=2)
text(250, 0.003, labels="Quick", pos=2, col="red")