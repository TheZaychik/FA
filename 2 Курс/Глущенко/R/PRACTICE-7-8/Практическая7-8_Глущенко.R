## Функция
"%+%" <- function(...){
  paste0(...)
}
check_id <- function(path) {

setwd(path)
dat <- read.csv("avocado_new.csv")
View(dat)
names <- c("id")
files <- list.files()

vecfile<-c()
vectype<-c()
for (f in files) {
  dat <- read.csv(f)
  
  print(vecfile)
  print(vectype)
  if(toString(names[names %in% names(dat)])=="id"){
    vecfile<-append(vecfile,c(f))
    vectype<-append(vectype,c(1))
  }
  else{
    vecfile<-append(vecfile,c(f))
    vectype<-append(vectype,c(0))
  }
  
  filename<-vecfile
  type<-vectype
  datout <- cbind.data.frame(filename, type)
  
  View(datout)
}

}
setwd("/home/nikita")
a<-getwd()
path<-a%+%"/git/FA/2 Курс/Глущенко/R/PRACTICE-7-8/"
check_id(path)
#2
InsectSprays
write.csv(InsectSprays, "InsectSprays.csv")
test1 <- read.csv("InsectSprays.c3sv")
#3
setwd("/home/nikita/git/FA/2 Курс/Глущенко/R/Practice7-8")
data123 <- read.table("data.txt", sep = "")
View(data123)
prices <- read.table("prices.txt", sep = "\n",header = FALSE)
View(prices)
#2.1
v1 <- c(1, 2.5, "organic")
v2 <- c(2, 1.5, "organic")
v3 <- c(3, 0.9, "conventional") 
test<-(cbind.data.frame(v1, v2,v3))
test
#2.2
trans.test<-t(test)
trans.test
#2.3
colnames(trans.test)<-append()
