pollution <- read.csv("../avgpm25.csv", colClasses=c("numeric", "character", "factor", "numeric", "numeric"))

## Five Number Summary
summary(pollution$pm25)

par(mfrow=c(1, 3))

## Histogram
hist(pollution$pm25, col="green", breaks=100)

## rug underneath histogram
rug(pollution$pm25)

## Boxplot
boxplot(pollution$pm25, col="blue")

## overlaying horizontal abline
abline(h = 12)

## Barplot
barplot(table(pollution$region), col = "wheat", main="Number of Counties in Each Region")