# Зайцев Н.В ПИ20-2в Практическая работа 5
# Задание 1
x<-seq(-10,10,0.2)
plot(x, x^2, type = "l", xlab = "x", ylab = "f(x)")
lines(x, x^2, col = "red")
lines(x, x^3, col = "green")
legend(-10,25, c("x^2", "x^3"), lwd = c(1,1), 
       col = c("red", "green"), cex = 0.8)

dev.copy(jpeg, "graph.jpeg")
x<-seq(-10,10,0.2)
plot(x, x^2, type = "l", xlab = "x", ylab = "f(x)")
lines(x, x^2, col = "red")
lines(x, x^3, col = "green")
legend(-10,25, c("x^2", "x^3"), lwd = c(1,1), 
       col = c("red", "green"), cex = 0.8)
dev.off()
