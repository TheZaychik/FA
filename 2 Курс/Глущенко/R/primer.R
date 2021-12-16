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
