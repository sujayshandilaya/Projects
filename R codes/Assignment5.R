#Association 
install.packages("arules")
install.packages("arulesViz")
library(arules)
library(arulesViz)

course_df <- read.csv("Coursetopics.csv")


course.df <- as.matrix(course_df) 


course.trans <- as(course.df, "transactions") # converts binary into list format

rules <- apriori(course.trans, parameter = list(minlen=2, supp = 0.01, conf = 0.5, target="rules"))

inspect(sort(rules, by = "lift"))

plot(rules)

# Clustering

pharma_df <- read.csv("Pharmaceuticals.csv")
View(pharma_df)



row.names(pharma_df) <- pharma_df[,2]
pharma_df <- pharma_df[,-2]
View(pharma_df)

pharma.df <- pharma_df[,-c(1, 11, 12, 13)]
View(pharma.df)


pharma.df.norm <- sapply(pharma.df, scale) #Normalizing all columns
summary(pharma.df.norm)

row.names(pharma.df.norm) <- row.names(pharma.df) 

d.norm <- dist(pharma.df.norm, method = "euclidean") # Calculating Euclidean Distance
d.norm


hc.ward <- hclust(d.norm, method = "ward.D")
plot(hc.ward)


clusters <- cutree(hc.ward, k = 2) #To create 2 clusters
clusters

aggregate(pharma.df.norm, by = list(clusters = clusters), mean)


#Interpretation

library(dplyr)
pharma_new_df <- read.csv("Pharmaceuticals.csv")

pharma_new.df <- mutate(pharma_new_df, Cluster = clusters)
pharma_new.df <- pharma_new.df[order(pharma_new.df$Cluster),]
View(pharma_new.df)

MedRecom <- as.factor(pharma_new.df$Median_Recommendation)
Location <- as.factor(pharma_new.df$Location)
Exchange <- as.factor(pharma_new.df$Exchange)
Cluster <- pharma_new.df$Cluster

count_type<- table(Cluster, MedRecom)
count_type
count_country <- table(Cluster, Location)
count_country
count_exchange <- table(Cluster, Exchange)
count_exchange

barplot(count_type, main = "Median Recommendation Comparison", 
        xlab = "Types", col = c("Yellow", "Green"), legend = rownames(count_type), las = 2) 

barplot(count_country, main = "Location Comparison", 
        xlab = "Country", col = c("Yellow", "Green"), legend = rownames(count_country), las = 2)

barplot(count_exchange, main = "Exchange Comparison", 
        xlab = "Exchange Type", col = c("Yellow", "Green"), legend = rownames(count_exchange), las = 2)


