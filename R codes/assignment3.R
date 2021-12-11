library(caret)
library(e1071)
library(ggplot2)

setwd("C:/Users/Sujay Shandilaya/Desktop/Fall-21/BA with R/assignments/Assignment 3")

#5.1 a)
set_df <- read.csv("prospensity.csv", header=TRUE, stringsAsFactors = TRUE)
set_df$Actual <- as.factor(set_df$Actual)

# Cutoff = 0.25
confusionMatrix(as.factor(ifelse(set_df$Propensity_of_1>0.25, '1', '0')), set_df$Actual)
# Cutoff = 0.5
confusionMatrix(as.factor(ifelse(set_df$Propensity_of_1>0.5, '1', '0')), set_df$Actual)
# Cutoff = 0.75
confusionMatrix(as.factor(ifelse(set_df$Propensity_of_1>0.75, '1', '0')), set_df$Actual)

#5.1 b)


set_df$Actual <- as.numeric(set_df$Actual)

set_df$Propensity_of_1 <- as.numeric(set_df$Propensity_of_1)

library(gains)
gain <- gains(set_df$Actual, set_df$Propensity_of_1,)
barplot(gain$mean.resp / mean(set_df$Actual), names.arg = gain$depth, xlab = "Percentile",
        ylab = "Mean Response", main = "Decile-wise lift chart")

# 6.1 

boston_df <- read.csv("BostonHousing.csv", header=TRUE, stringsAsFactors = TRUE)


summary(boston_df)
model <- lm(formula = MEDV ~ CRIM + CHAS + RM, data = boston_df)

predict(model,data.frame("CRIM" = 0.1,"RM" = 6, "CHAS" = 0))

corrr <- cor(boston_df[, c('CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','LSTAT')])

library(DescTools)

FindCorr(corrr, cutoff = .75, verbose = FALSE)

boston.df <- boston_df[ -c(3,5,10,14) ]

# Data Partitioning
set.seed(1234)
#Partitioning into training (60%) and validation (40%)
train.rows <- sample(row.names(boston.df), dim(boston.df)[1]*0.6) 
# collect all the columns with training rows ID in to training set.
train.data <- boston.df[train.rows,] 
# assign row IDs that are not already in the training set, into validation
valid.rows <- setdiff(rownames(boston.df), train.rows)
valid.data <- boston.df[valid.rows,] 

boston.lm <- lm(MEDV ~ ., data = train.data)

library(forecast)

#forward
boston.forward <- step(boston.lm , direction = "forward")
summary(boston.forward)

# use predict() to make predictions on a new set.
boston.forward.pred <- predict(boston.forward, valid.data)


#backward
boston.backward <- step(boston.lm , direction = "backward")
summary(boston.backward) 

# use predict() to make predictions on a new set.
boston.backward.pred <- predict(boston.backward, valid.data)

#both
boston.both <- step(boston.lm , direction = "both")
summary(boston.both)
# use predict() to make predictions on a new set.
boston.both.pred <- predict(boston.both, valid.data)

# use accuracy() to compute common accuracy measures.
accuracy(boston.forward.pred, valid.data$MEDV)
accuracy(boston.backward.pred, valid.data$MEDV)
accuracy(boston.both.pred, valid.data$MEDV)


actual = valid.data$MEDV
#forward Decile Chart
gain1 = gains(actual,boston.forward.pred,group = 10)
plot(c(0, gain1$cume.pct.of.total*sum(actual))~c(0, gain1$cume.obs), type = "l", xlab = "#Cases", ylab = "Cumulative MEDV", main = "Lift Chart for Forwards")
segments(0, 0, nrow(valid.data), sum(actual), lty = "dashed", col = "red", lwd = 2)

#backward Decile Chart
gain1 = gains(actual,boston.backward.pred,group = 10)
plot(c(0, gain1$cume.pct.of.total*sum(actual))~c(0, gain1$cume.obs), type = "l", xlab = "#Cases", ylab = "Cumulative MEDV", main = "Lift Chart for backwards")
segments(0, 0, nrow(valid.data), sum(actual), lty = "dashed", col = "red", lwd = 2)

#both Decile Chart
gain1 = gains(actual,boston.both.pred,group = 10)
plot(c(0, gain1$cume.pct.of.total*sum(actual))~c(0, gain1$cume.obs), type = "l", xlab = "#Cases", ylab = "Cumulative MEDV", main = "Lift Chart for both")
segments(0, 0, nrow(valid.data), sum(actual), lty = "dashed", col = "red", lwd = 2)

#10.1

bank.df <- read.csv("banks.csv")

logit.reg <- glm(Financial.Condition ~ TotLns.Lses.Assets + TotExp.Assets, data = bank.df, family = "binomial")
options(scipen=999)
summary(logit.reg)
coeff_odds_df <- data.frame(summary(logit.reg)$coefficients, odds = exp(coef(logit.reg)))
round(coeff_odds_df, 5)

reg_predict<-predict(logit.reg,data.frame("TotExp.Assets"=0.11,"TotLns.Lses.Assets"=0.6)) # predicted value
reg_predict
#the odds
exp(reg_predict)
#the probability
prob<- exp(reg_predict)/(1+exp(reg_predict))

prob

exp(8.371)


#10.3

riding.df <- read.csv("RidingMowers.csv")

Total_Households <- nrow(riding.df) 
ownership_df <- subset(riding.df, Ownership=="Owner")
no_of_owners <- nrow(ownership_df) 
Percentage_of_owners <- (no_of_owners / Total_Households)*100
Percentage_of_owners



set.seed(1234)

train.index <- sample(c(1:dim(riding.df)[1]), dim(riding.df)[1]*0.6)
riding.df$Ownership <- as.factor(riding.df$Ownership)

train.df <- riding.df[train.index, ]
valid.df <- riding.df[-train.index, ]
logit.reg <- glm(Ownership ~ ., data = train.df, family = "binomial")
options(scipen=999)
summary(logit.reg)

#to plot a scatter plot between lot size and income. Also color Code the same on the basis of ownership
plot(riding.df$Income ~ riding.df$Lot_Size, xlab = "Lot_Size", ylab = "Income", col=c("red","green")[riding.df$Ownership])
legend(x="topright", legend = levels(riding.df$Ownership), col=c("red", "green"), pch=1)

library(caret)


riding.df$X <- NULL
riding.df$Outcome<-ifelse(riding.df$Ownership=="Owner",1,0)
# Converting the new variable into factor
riding.df$Outcome<-as.factor(as.character(riding.df$Outcome))
str(riding.df)
riding.df$Ownership <- NULL

#Implementing the Logistic Regression Model
riding.df_log<-glm(Outcome~.,data = riding.df, family = "binomial")
summary(riding.df)

riding.df_pred<-predict(riding.df_log, type = "response")
round(riding.df_pred,5)

confusionMatrix(as.factor(ifelse(riding.df_pred>0.5, "1", "0")), as.factor(riding.df$Outcome))

predict_val<-predict(riding.df_log,data.frame("Income"=60,"Lot_Size"=20))
predict_val  
o <- exp(predict_val)

o

p <- o/(1+o)
p
