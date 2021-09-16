# Зайцев Н.В ПИ20-2в Практическая работа 2
# Задание 1 
round(log((2^-3 + (sin(factorial(7) + choose(32,11))^3) / (sqrt(1 + atan(1 / 1 + 0.2435)))), 48.23), 5)
# Задание 2
round(cos((1 / sqrt(0.3532)^1/3) - ((((cosh(12) / sinh(12))^3) * exp(-1/4.8)) / sqrt(abs(log((256/1809.43), 13.76)) + atan(7^-3))))^-1, 3)
# Задание 3
cars
sum(cars[,2]) * 0.3048 / length(cars[,2])
# Задание 4
# install.packages("ggplot2")
# install.packages("dplyr")
library("ggplot2")
library("dplyr")
glimpse(diamonds, 10)
# кол-во алмазов
length(diamonds[["carat"]])
# средний вес алмазов (в каратах)
mean(diamonds[["carat"]])
# Задание 5
sin(0.01)
cos(0.01)
