setwd("C:/Users/Sujay Shandilaya/Desktop/Fall-21/BA with R/data files")

movies_df <- read.csv("Movies2016.csv", header=TRUE, stringsAsFactors = FALSE)
t(t(movies_df))

#histogram for opening gross sales
hist(movies_df$Opening.Gross.Sales....millions., xlab = "Opening Gross Sales ($ millions)", xlim=c(0,200), ylim=c(0,60), main="Opening Gross sales")

#histogram for total gross sales
hist(movies_df$Total.Gross.Sales....millions., xlab = "Total Gross Sales ($ millions)", xlim=c(0,600), ylim=c(0,50), main="Total Gross sales")

#histogram for total no of theaters
num_theater<-movies_df$Number.of.Theaters

theater<-str_remove(num_theater, ',')

theater_int<-as.integer(theater)

hist(theater_int, xlab = "Total Number of Theaters", ylim=c(0,50), main="Number of Theaters")

class(movies_df$Weeks.in.Release)

##histogram for weeeks in release
hist(movies_df$Weeks.in.Release, xlab = " Number of Weks in release", xlim=c(0,60), ylim=c(0,50), main="Number of Weeks in Release")

#scatter plot for total gross sales vs opening gross sales
plot(movies_df$Total.Gross.Sales....millions. ~ movies_df$Opening.Gross.Sales....millions., xlab = "Opening Gross sales", ylab = "Total Gross Sales")


#scatter plot for total gross sales vs total no of theatres
plot(movies_df$Total.Gross.Sales....millions. ~ theater_int, xlab = "Total no of theaters", ylab = "Total Gross Sales")


#scatter plot for total gross sales vs no of weeks
plot(movies_df$Total.Gross.Sales....millions. ~ movies_df$Weeks.in.Release, xlab = "Number of weeks in release", ylab = "Total Gross Sales")


