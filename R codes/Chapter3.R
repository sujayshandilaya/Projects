setwd("C:/Users/Sujay Shandilaya/Desktop/Fall-21/BA with R/data files")

rm_df <- read.csv("RidingMowers.csv", header=TRUE, stringsAsFactors = TRUE)

#to plot a scatter plot between lot size and income. Also color Code the same on the basis of ownership
plot(rm_df$Income ~ rm_df$Lot_Size, xlab = "Lot_Size", ylab = "Income", col=c("red","green")[rm_df$Ownership])
legend(x="topright", legend = levels(rm_df$Ownership), col=c("red", "green"), pch=1)

library(ggplot2)

laptop_df <- read.csv("LaptopSalesJanuary2008.csv", header=TRUE, stringsAsFactors = TRUE)

head(laptop_df)

#plot the bargraph for store and its average price
avg_store<- aggregate(laptop_df$Retail.Price ~ laptop_df$Store.Postcode, data = laptop_df, mean)

ggplot(avg_store)+geom_col(aes(x=`laptop_df$Store.Postcode`,y=`laptop_df$Retail.Price`))+theme(axis.text.x = element_text(angle = 90)) + coord_cartesian(ylim=c(475, 500))

#plot the boxplot for retail price for each store side by side
boxplot(laptop_df$Retail.Price ~ laptop_df$Store.Postcode, xlab = "Store", ylab = "Price")
