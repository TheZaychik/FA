#Глущенко Никита. ПИ20-2в. Вариант №3
#Задание 1
x<-2
y<-2
z<-exp(x)-sin(x)^2
cat("При x=2,y=2, z = ", z)
a<-(1+y)*((x+(y/(x^2+4)))/(exp(-x-2)+1))
cat("При x=2,y=2, a = ", a)
#Задание 2
a<-1.2
b<-3.1
x<-sqrt(a^2+b^2)
cat("X = ", x)
zadanie2.1<-function(a,b,x){
  if (x<2){
    c<-a*x+b
  }
  else if (x>=2) {
    c<-a+b*x
  }
  return(c)
}
c<-zadanie2.1(a,b,x)
cat("C = ", c)
zadanie2<-function(a,b,x,c){
  if (x<=a){
    y<-x-c
  }
  else if (a<x && x<=b) {
    y<-x+c
  }
  else if (x>b){
    y<-x/c
  }
  return(y)
}
y=zadanie2(a,b,x,c)
cat("Y = ", y)
#Задание 3
zadanie3<-function(){
  S<-0
  for(i in 1:10){
    S<-S+1/sqrt(i)
  }
  return(S)
}
S<-zadanie3()
cat("S = ", S)
#Задание 4
KolVoAbiturientov<-matrix(c(12,345,67,78,98,9,67,45,32,334), nrow=10,ncol=1)
KolVoAbiturientov
maxabitur<-which(KolVoAbiturientov[,1]==max(KolVoAbiturientov[,1]))
cat("Год с самым большим количеством абитуриентов: ", maxabitur)
#Решение через обычный вектор
vectorAbitur<-c(12,345,67,78,98,9,67,45,32,334)
matforvector<-which(vectorAbitur==max(vectorAbitur))
cat("Год с самым большим количеством абитуриентов через вектор: ", matforvector)
#Задание 5
functionForFirstExercize <-function(x) {exp(x)-sin(x)^2} 
x <- seq(-10, 10, 0.05)
plot(x,functionForFirstExercize(x), type = "l")
abline(h = 0, v = 0, col = "gray50")
#График по второй функции
y<-2
functionForSecondExercize <-function(x) {(1+y)*(x+((y/(x^2+4))))/(exp(-x-2)+1)} 
x <- seq(-10, 10, 0.05)
plot(x,functionForSecondExercize(x), type = "l")
abline(h = 0, v = 0, col = "gray50")

