a = c(1, 2, -3, -4) # Сформировать вектор а из набора чисел 1,2,-3 и -4 
b <- rep(1, 4) 
seq(0,6,2)->c #от 0 до 6 с шагом 2
d=2:5 #вектор с координатами 2,3,4,5
a;b;c;d
a[2]<-10
x<-array(2,dim=c(1,10));x
s<-as.vector(x);s
S<-matrix(0,nrow=10,ncol=10)
Q<-cbind(rep(1,3),1:3,c(1,-2,0))
P<-rbind(seq(-1,1,1),rep(2,3),4:6)
S;Q;P
x<-array(2,dim=c(3,5));x
s<-as.matrix(x);s
Data1<-read.table("clipboard",h=FALSE,dec=",",sep="\t")
W1<-as.matrix.data.frame(Data1)
W1
A<-W1[,1:3]
B<-W1[,4]
A
B
write.table(B,"/home/nikita/git/FA/2 Курс/Глущенко/R/clipboard",quote=FALSE,col.names = FALSE,row.names = FALSE,sep="\t",dec=",")
#Задание 1
a <- rep(3, 50);a 
#Задание 2
b =1:100;b 
#Задание 3
help(matrix)
S<-matrix(1:16,nrow=4,ncol=4,byrow = FALSE)
S
S<-matrix(1:16,nrow=4,ncol=4,byrow = TRUE)
S
#Задание 4.1
Data<-read.table("/home/nikita/git/FA/2 Курс/Глущенко/R/1.xlsx",h=FALSE,dec=",",sep="\t")
W1<-c(Data);W1
#Задание 4.2
Data<-read.table("/home/nikita/git/FA/2 Курс/Глущенко/R/2.xlsx",h=FALSE,dec=",",sep="\t")
W2<-c(Data);W2
#Задание 4.3
Data<-read.table("/home/nikita/git/FA/2 Курс/Глущенко/R/zadanie4_3.xlsx",h=FALSE,dec=",",sep="\t")
W<-as.matrix.data.frame(Data)
W
Data<-read.table("/home/nikita/git/FA/2 Курс/Глущенко/R/zadanie4_3_2.xlsx",h=FALSE,dec=",",sep="\t")
W<-as.matrix.data.frame(Data)
W
#Задание 5
S<-matrix(nrow=10,ncol=10)
for (i in 1:10)
  for (j in 1:10)
    S[i,j]<-i+j
S
#Задание 6
B<-matrix(1,nrow=40,ncol=40)
write.table(B,"/home/nikita/git/FA/2 Курс/Глущенко/R/zadanie5.xlsx",quote=FALSE,col.names = FALSE,row.names = FALSE,sep="\t",dec=",")

