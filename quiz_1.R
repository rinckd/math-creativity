library(dplyr)
library(readr)
library(tidyr)
library(plyr) # This is a neat library
library(readxl)

pollution <- read_csv("data/daily_SPEC_2014.csv.bz2")

names(pollution)
question1 <- pollution %>%
  filter(`State Name` == "Wisconsin") %>%
  filter(`Parameter Name` == "Bromine PM2.5 LC" ) 
smaller_table <- select(question1, `Parameter Name`, `Arithmetic Mean` )
answer1 <- mean(smaller_table$`Arithmetic Mean`, na.rm=TRUE)

question2 <- ddply(pollution, .(`Parameter Name`), summarize,  TotalMean=mean(`Arithmetic Mean`, na.rm=TRUE))
arrange(question2, desc(`TotalMean`))

question3 <- pollution %>%
  filter(`Parameter Name` == "Sulfate PM2.5 LC") %>%
  select(`State Code`, `County Code`, `Site Num`, `Arithmetic Mean`)
  
question3b <- ddply(question3, .(`State Code`, `County Code`, `Site Num`), summarize, TotalMean=mean(`Arithmetic Mean`, na.rm=TRUE))
arrange(question3b, desc(`TotalMean`))

question4 <- pollution %>%
  filter(`Parameter Name` == "EC PM2.5 LC TOR" ) %>%
  select(`State Name`, `Arithmetic Mean`)
question4b <- ddply(question4, .(`State Name`), summarize, TotalMean=mean(`Arithmetic Mean`, na.rm=TRUE))


question5 <- pollution %>%
  filter(`Parameter Name` == "OC PM2.5 LC TOR") %>%
  filter(`Longitude` < -100) %>%
  select(`Longitude`, `Arithmetic Mean`)
median(question5$`Arithmetic Mean`, na.rm=TRUE)

library(readxl)
sites <- read_excel("data/aqs_sites.xlsx", sheet="aqs_sites")
question6 <- sites %>%
  filter(`Land Use` == "RESIDENTIAL") %>%
  filter(`Location Setting` == "SUBURBAN")

question7 <- pollution %>%
  filter(`Parameter Name` == "EC PM2.5 LC TOR" ) %>%
  select(`State Code`, `County Code`, `Site Number`, `Arithmetic Mean`)
question7b <- ddply(question7, .(`State Code`, `County Code`, `Site Num`), summarize, TotalMean=mean(`Arithmetic Mean`, na.rm=TRUE))

question7d <- sites %>%
  filter(`Land Use` == "RESIDENTIAL") %>%
  filter(`Location Setting` == "SUBURBAN") %>%
  filter(`Longitude` >= -100)

question7e <- intersect(question7d, question7b)
for(i in 1:length(question7b)) {
  questionTemp <- question7d %>%
    filter(`State Code` == as.character(question7b[i]$`State Code`)) %>%
    filter(`County Code` == as.character(question7b[i]$`County Code`)) %>%
    filter(`Site Number` == as.character(question7b[i]$`Site Number`))
  
  print(questionTemp)
    # next(x[i] < 5) # Just for conceptualizing my question.
  #print(question7b[i])
}

