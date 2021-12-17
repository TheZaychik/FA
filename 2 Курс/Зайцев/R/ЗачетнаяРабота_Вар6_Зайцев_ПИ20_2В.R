# Зайцев Н.В. Зачетная работа | Вариант 6
# Задание 1
z <- sample(1:25, 1)
x <- sample(1:25, 1)
y <- sample(1:25, 1)
z
x
y
s <- (z * sqrt(x) - y^2 * x^(1 / 3)) / ((x + 0.5)^(1 / 5))
s

b <- cos(tan(1 / z)^2)
b

# Задание 2
a <- 2.5
b <- 1.3
c <- 1.5
d <- 2.3
x <- 0
y <- 0
if ((a * b) >= (c * d)) {
  x <- sqrt(a * b)
} else if ((a * b) < (c * d)) {
  x <- (c * d)^(1 / 3)
}
if (x < 1) {
  y <- a + c * x
} else if ((1 <= x) && (x < 3)) {
  y <- b + d / x
} else if (x >= 3) {
  y <- с - a * x
}
x
y

#Задание 3
for (k in 1 : 20) {
  print((sqrt(k) + 2) / (k^2 + 1))
}

# Задание 4
boxes <- c('Коробка 1', 'Коробка 2', 'Коробка 3', 
           'Коробка 4', 'Коробка 5', 'Коробка 6')
prices <- c(100, 50, 250, 250, 100, 300)
max_price <- max(prices)
max_price
for (i in 1 : length(prices)) {
  if (max_price - prices[i] == 50){
    print(boxes[i])
    print(prices[i])
  }
}

# Задание 5
# Выражение 2 из Задания 1: b <- cos(tan(1 / z)^2)
rng <- c(1, 2, 3, 4, 5)
get_graph <- function(rng) {
  b <- c()
  for (i in 1 : length(rng)){
    b <- append(b, cos(tan(1 / rng[i])^2))
  }
  plot(rng, b, type = 'l')
}
get_graph(rng)



