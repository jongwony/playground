library(datasets)

hist(airquality$Ozone)  ## Draw a new plot

with(airquality, plot(Wind, Ozone))
title(main="Ozone and Wind in New York City")   # Add a title
with(subset(airquality, Month==5), points(Wind, Ozone, col="blue"))
legend("topright", pch=1, col=c("blue", "red"), legend=c("May", "Other Months"))

airquality <- transform(airquality, Month=factor(Month))
boxplot(Ozone ~ Month, airquality, xlab = "Month", ylab = "Ozone (ppb)")

## example points
example(points)

x <- rnorm(100)
y <- rnorm(100)
plot(x, y, pch=20
title("Scatterplot")
text(-2, -2, "Label")
legend("topleft", legend ="Data", pch=20)

fit <- lm(y ~ x)
abline(fit, lwd=3, col="blue")

y <- x + rnorm(100)
g <- gl(2, 50, labels=c("Male", "Female"))
str(g)

points(x[g=="Male"], y[g=="Male"], col="green")