# install.packages('ggplot2', dep=TRUE)

library(dataset)

library(lattice)
state <- data.frame(state.x77, region=state.region)
xyplot(life.exp ~ income | region, data=state, layout=c(4,1))

library(ggplot2)
data(mpg)
qplot(displ, hwy, data=mpg)