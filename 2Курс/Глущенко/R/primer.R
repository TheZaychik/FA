x<-1
y<-1
z<-1
r<-x/(1+(x**2)/2*y)
r
b<-x*(tan(z)+exp(x+3))
b
zadanie2<-function(x,y){
if (x*y<=20){
  z<-tan((5*x+y*x)/(21-x))
  print(z)
}
else if (x<0) {
  z<-3 
  print(z)
}
else{
  z<-1
  print(z)
}
  
  a<-z^2-15.9*z
  print(a)
}
zadanie2(x,y)
##3
zadanie3<-function(sum,proc){
  i<-0
  while(sum<=20000){
    sum<-sum*(1+proc)
    i<-i+1
    print(sum)
  }
  print(i)
}
zadanie3(1000,0.06)
#4
a<-c(5, -50, 9, -10, 3, -2)
zadanie4<-function(){
  e<-0
  b<-length(a)
for (i in 1:b){
  if (a[i] < 0){
    e<-e+1
    print(e[i])
  }
}
  
  print(e)
}
zadanie4()
min(a)
##5
S<-matrix(1:16,nrow=4,ncol=4,byrow = FALSE)
S
zadanie5<-function(){
  sum<-c(0,0,0,0)
  for (i in 1:4){
    sum[i]<-sum(S[,i])
  }
  
  print(sum)
  which(sum==max(sum))
}
zadanie5()
#Создать пользовательскую функцию 2*x^2-3*x+5 и построить ее график на интервале (-5; 5). 
f <-function(x) {2*x^2-3*x+5} 
x <- seq(-5, 5, 0.05)
plot(x,f(x), type = "l")
abline(h = 0, v = 0, col = "gray50")
###
a<-1.2
b<-3.1
x<-sqrt(a^2+b^2)
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
y
#1
x<-2
y<-2
z<-exp(x)-sin(x)**2
z
a<-(1+y)*(x+((y/(x^2+4)))/(exp(-1*x-2)+1))
a
#4
S<-matrix(c(12,345,67,78,98,9,67,45,32,334,56,12,32,45,67,88), nrow=4,ncol=4,byrow = FALSE)
S
zadanie5<-function(){
  sum<-c(0,0,0,0)
  for (i in 1:4){
    sum[i]<-sum(S[,i])
  }
  
  print(sum)
  which(sum==max(sum))
}
zadanie5()
balls<-c(12,25,34,31,30,9)
newballs<-c()
srarifm<-sum(balls)/6
zadanie1<-function(balls){
  for (i in 1:length(balls)){
  if (balls[i]>srarifm){
    newballs<-append(newballs,balls[i])
    }
  }
  return(newballs)
}
newballs<-zadanie1(balls)
newballs
for(i in 0.2:5){
  print(i)
}
