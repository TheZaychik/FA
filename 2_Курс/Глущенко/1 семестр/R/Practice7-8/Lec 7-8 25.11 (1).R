# формат файлов csv
"user1,26,F"
"user2,32,M"
# загрузка файлов формата csv
read.csv("avocado.csv")
read.csv(file.choose())
\t
dat <- read.csv("avocado.csv")
View(dat)
# загрузка файла с разделителем  ;
dat2 <- read.csv("avocado2.csv", sep = ";")
# функция  read.csv2 считывает файлы с разделителем ; без sep
dat2 <- read.csv2("avocado2.csv")
dat3 <- read.csv("avocado3.csv", sep = ";")
str(dat3)
dat3 <- read.csv2("avocado3.csv", sep = ";")
str(dat3)
dat3 <- read.csv("avocado3.csv", sep = ";", dec = ",", stringsAsFactors = FALSE)
read.csv("test.csv", encoding = "Windows-1251")
#### txt
dat_cars <- read.table("cars.txt", sep = "")
View(dat_cars)
dat_cars2 <- read.table("cars2.txt", header = TRUE)

dat_cars3 <- read.table("cars3.txt")
View(dat_cars3)
? read.table
##### xls, xlsx
library(readxl)
read_excel()

ex <- read_excel("test.xlsx", sheet = "Prices")
View(ex)
help("read_excel")

### запись файлов
mtcars
write.csv(mtcars, "mtcars.csv")
test1 <- read.csv("mtcars.csv")
View(test1)
test2 <- write.csv2(mtcars, "mtcars2.csv")
View(test2)

write.table(mtcars, "mtcars.txt")
WriteXLS(mtcars, "mtcars.xlsx")
WriteXLS(c("mtcars", "cars"), "cars.xlsx")
### Задача
getwd()
setwd("/Users/svetlana/S/test")
files <- list.files()
for (f in files) {
  dat <- read.csv(f)
  cat (f, dim(dat), "\n")
}

## Функция

 check <- function(name, sheet) {
   ex_dat <- read_excel(name, sheet = sheet)
   if (ncol(ex_dat) == nrow(ex_dat)) {
     res <- TRUE
     
   } else {
     res <- FALSE
   }
   res
 }
check ("test.xlsx", 2) 
 
### Работа с датафрейм
dat <- cbind.data.frame(a = c(4,6,7), b = c(0,1,0))
View(dat)

data()
mtcars

class(mtcars)

AirPassengers
class(AirPassengers)
plot(AirPassengers)
diff(AirPassengers, differences = 1)

HairEyeColor
class(HairEyeColor)
dim(HairEyeColor)
margin.table(HairEyeColor, 1)
margin.table(HairEyeColor, 2)
margin.table(HairEyeColor, 3)

## частоты в долях

prop.table(HairEyeColor)
prop.table(HairEyeColor)*100

##  базовые операции с дф

mycars <- mtcars
mycars

mycars[3,2]
mycars[3,2] <- 6
mycars
mycars[2, ]
mycars[ ,3]
mycars[2:4]
mycars[ ,2:3]

mycars[c(2,5,8), ]
mycars[ ,c(2,4)]
mycars["Mazda RX4", "cyl"]

mycars["Mazda RX4", c("cyl", "hp")]

t(mycars)
class(t(mycars))
mycars2 <- as.data.frame(t(mycars))
mycars
##

avo <- read.csv("avocado_new.csv")
str(avo)
summary(avo) # описательная статистика для каждого столбца

head(avo)
head(avo, 10)
tail(avo)

avo <- na.omit(avo)
summary(avo)

head(rownames(avo))

colnames(avo) <- tolower(avo)
View(avo)
avo <- read.csv("avocado_new.csv")
avo$Total.Volume
avo$log.volume <- log(avo$Total.Volume)
str(avo)
avo <- avo[, -c(15)]
str(avo)
organic <- avo[avo$type == "organic",]
avo2 <- avo[avo$type == "organic",3:4]
head(avo2)
avo3 <- avo[avo$type == "organic",c(2,4)]
head(avo3)
avo4 <- avo[avo$type == "organic",-c(2,4)]
head(avo4)
avo5 <- avo[avo$AveragePrice >1 & avo$AveragePrice < 1.5, ]
head(avo5)
avo6 <- avo[avo$AveragePrice < 1.5 & avo$type == "organic", ]
head(avo6)
