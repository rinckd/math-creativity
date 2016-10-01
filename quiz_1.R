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
question7b <- ddply(question7, .(`State Code`, `County Code`, `Site Number`), summarize, TotalMean=mean(`Arithmetic Mean`, na.rm=TRUE))
question7b$`State Code` = as.numeric(as.character(question7b$`State Code`))
question7b$`County Code` = as.numeric(as.character(question7b$`County Code`))
question7b$`Site Num` = as.numeric(as.character(question7b$`Site Num`))
question7d <- sites %>%
  filter(`Land Use` == "RESIDENTIAL") %>%
  filter(`Location Setting` == "SUBURBAN") %>%
  filter(`Longitude` >= -100)
questionTemp <- question7d %>%
  filter(`State Code` %in% question7b$`State Code`) %>%
  filter(`County Code` %in% question7b$`County Code`) %>%
  filter(`Site Number` %in% question7b$`Site Num`)
question7e <- question7b %>%
  filter(`State Code` %in% questionTemp$`State Code`) %>%
  filter(`County Code` %in% questionTemp$`County Code`) %>%
  filter(`Site Num` %in% questionTemp$`Site Number`)
question7f <- ddply(question7e, .(), summarize, TotalMean=mean(`TotalMean`, na.rm=TRUE))

 
 #Amongst monitoring sites that are labeled as COMMERCIAL for "Land Use", which month
question8 <- sites %>%
  filter(`Land Use` == "COMMERCIAL")
questionTemp <- pollution %>%
  filter(`State Code` %in% question8$`State Code`) %>%
  filter(`County Code` %in% question8$`County Code`) %>%
  filter(`Site Num` %in% question8$`Site Number`) %>%
  filter(`Parameter Name` == "Sulfate PM2.5 LC") %>%
  arrange(`Arithmetic Mean`)
head(questionTemp)

questionblah <- sites %>%
  filter(`Land Use` == "RESIDENTIAL") %>%
  filter(`Location Setting` == "SUBURBAN") %>%
  filter(`Longitude` >= -100)
questionblah2 <- sites %>%
  filter(`Land Use` == "RESIDENTIAL")
questionblah2 <- questionblah2 %>%
  filter(`Location Setting` == "SUBURBAN")
questionblah2 <- questionblah2 %>%
  filter(`Longitude` >= -100)
