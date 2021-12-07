f <-function(x) {(x-3)^2} 
f(5)
x <- seq(-5, 8, 0.05)
plot(x,f(x), type = "l")
abline(h = 0, v = 0, col = "gray50")
# Задание 1 - график (-2,2) sign(x)
f1 <-function(x) {sign(x)} 
x <- seq(-2, 2, 0.05)
plot(x,f1(x), type = "l")
abline(h = 0, v = 0, col = "gray50")

# Задание 2 -Подготовить 10 разных графиков с различными вариантами оформления. Использовать все изученные параметры. В качестве наборов данных использовать различные математические функции. Подобрать функции интересные с точки зрения графического представления. На одном графике размещать несколько функций. 
# 1-3
abline(h = 0, v = 0, col = "gray50")

x<-seq(-10,10,0.2)
plot(x, (x^2)/x, type = "l", xlab = "x", ylab = "f(x)")
lines(x, (x^2)/x, col = "red")
lines(x, sign(x), col = "blue")
lines(x, x^3, col = "green")

abline(h = 0, v = 0, col = "gray50")
legend(-10,10, c("(x^2)/x","sign(x)", "x^3"), lwd = c(1,1), 
       col = c("red", "blue","green"), cex = 0.8)
# 4-6

x<-seq(-5,5,0.2)
f4<-function(a,b,c){(a*(x^2)+b*x+c)}
plot(x, 10/x, type = "l", xlab = "x", ylab = "f(x)",col = "red")
lines(x, -3*x, col = "blue")
lines(x, f4(10,2,-1), col = "green")
abline(h = 0, v = 0, col = "gray50")
legend(-5,50, c("парабола","прямая", "гипербола"), lwd = c(1,1), 
       col = c("green", "blue","red"), cex = 0.8)
# 7- 10

x<-seq(-10,10,0.2)
plot(x, cos(x), type = "l", xlab = "x", ylab = "f(x)",col = "red")
lines(x, exp(x), col = "blue")
lines(x,sqrt(x), col = "green")
lines(x,log10(x), col = "orange")
abline(h = 0, v = 0, col = "gray50")
legend(-10,1, c("ln(x)","показательная", "y=sqrt(x)","cos(x)"), lwd = c(1,1), 
       col = c("orange", "blue","green","red"), cex = 0.8)

