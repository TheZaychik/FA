# Зайцев Н.В ПИ20-2в Практическая работа 1
# Задание 1 
67^3 - 112^2
log(125)
log(81, 3)
# Задание 2
flights_d <- c(140, 150, 100, 90, 230, 240, 165)
flights_a <- c(65, 145, 80, 87, 220, 268, 216)
# 2.1
flights_d[3]
# 2.2
flights_d[2] - flights_a[2] 
# 2.4
sum(flights_d)
# 2.5 
for (i in 1:length(flights_a)) {
  if (flights_a[i] < 220){
    print(i)
  }
}
# Задание 3
pos <- c(4.765, 3.230, 1.256, 1.780, 2.583, 2.781, 3.945, 2.345)
# 3.1 
max(pos)
min(pos)
# 3.2
pos.round <- round(pos, 2)
pos.round
# 3.3
pos.g <- c()
for (i in 1:length(pos)) {
  pos.g <- c(pos.g, pos[i] * 1000)
}
pos.g
# Задание 4
milk <- c(89.5, 50.5, 31.5, 21.0, 22.1, 27.4)
# 4.1
sum <- 0
for (i in 1:length(milk)) {
  sum <- sum + milk[i]
}
s_arf <- sum / length(milk)
s_arf
# 4.2
E = 0
for (i in 1:length(milk)) {
  E <- E + (milk[i] - s_arf)^2
}
s <- (E/length(milk) - 1)^2
s
# Задание 5
euro
# 5.1
help("euro")
# 5.2
euro['FIM'] * 100
euro['BEF'] * 50
# 5.3
max <- -999999
for (i in 1:length(euro)) {
  if (euro[i] > max){
    max <- euro[i]
  }
}
max
# Задание 6
# 6.1
country <- c(rep("France", 5), rep("Italy", 5), rep("Spain", 5))
country
# 6.2
year <- c(seq(2000,2004), seq(2000,2004), seq(2000,2004))
year















