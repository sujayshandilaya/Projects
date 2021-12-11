setwd("C:/Users/Sujay Shandilaya/Desktop/Fall-21/BA with R/data files")

corolla_df <- read.csv("ToyotaCorolla.csv", header=TRUE, stringsAsFactors = TRUE)
head(corolla_df)
summary(corolla_df)
names(corolla_df)


class(corolla_df$Fuel_Type)
levels(corolla_df$Fuel_Type)

class(corolla_df$Color)
levels(corolla_df$Color)

#To print histogram of no of cars per KM.
hist(corolla_df$KM, xlab = "KM") 
 
#To print boxplot of fueltype and weight of car.
boxplot(corolla_df$Weight ~ corolla_df$Fuel_Type, xlab = "Fuel_Type", ylab = "Weight")

#To Print scatter plof mfg_year and price
plot(corolla_df$Price ~ corolla_df$Mfg_Year, xlab = "Mfg_Year", ylab = "Price")

#To Print scatter plot of KM driven and price
plot(corolla_df$Price ~ corolla_df$KM, xlab = "KM", ylab = "Price")


# Use model.matrix() to convert all categorical variables in the data frame into
# a set of dummy variables. We must then turn the resulting data matrix back into
# a data frame for further work
xtotal <- model.matrix(~ 0 + Fuel_Type + Color, data = corolla_df)

xtotal <- as.data.frame(xtotal)
t(t(names(xtotal))) 
head(xtotal)


xtotal <- xtotal[, -12] 
xtotal <- xtotal[, -3]
head(xtotal)

corolla_df <- cbind(corolla_df[, -c(8, 11)], xtotal)
t(t(names(corolla_df)))
set.seed(1) 
## partitioning into training (50%), validation (30%), test (20%)
# randomly sample 50% of the row IDs for training
train.rows <- sample(rownames(corolla_df), dim(corolla_df)[1]*0.5)
# randomly sample 30% of the row IDs for validation (setdiff used to draw records not in training set)
valid.rows <- sample(setdiff(rownames(corolla_df), train.rows), dim(corolla_df)[1]*0.3)
test.rows <- setdiff(rownames(corolla_df), union(train.rows, valid.rows))
train.data <- corolla_df[train.rows, ]
valid.data <- corolla_df[valid.rows, ]
test.data <- corolla_df[test.rows, ]
dim(train.data)
dim(valid.data)
dim(test.data)




