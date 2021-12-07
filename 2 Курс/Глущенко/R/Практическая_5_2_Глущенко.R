mycars<-mtcars

View(mycars)
hist(mycars$hp, main = "Число лошадиных сил", col = "green", 
     xlab = "Число сил",ylab="Количество подобных машин",breaks = 20,border="navy")
abline(v=mean(mycars$hp),col="red",lty=2,lwd=2)
abline(v=median(mycars$hp),col="blue",lty=4,lwd=2)
