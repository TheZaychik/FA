# Зайцев Н.В ПИ20-2в Практическая работа 4
# Задание 1
a <- rep(3, 50)
a
# Задание 2
b <- 1:100
b
# Задание 3
help(matrix)
S<-matrix(1:16, nrow=4, ncol=4, byrow = FALSE)
S
S<-matrix(1:16, nrow=4, ncol=4, byrow = TRUE)
S
# Задание 4
# Задание 4-1
Data<-read.table("~/git/FA/2 Курс/Зайцев/R/Семинары/ПР4/1.xlsx",h=FALSE,dec=",",sep="\t")
W1<-c(Data)
W1
# Задание 4-2
Data<-read.table("~/git/FA/2 Курс/Зайцев/R/Семинары/ПР4/2.xlsx",h=FALSE,dec=",",sep="\t")
W2<-c(Data)
W2
# Задание 4-3
Data<-read.table("~/git/FA/2 Курс/Зайцев/R/Семинары/ПР4/3.xlsx",h=FALSE,dec=",",sep="\t")
W<-as.matrix.data.frame(Data)
W
Data<-read.table("~/git/FA/2 Курс/Зайцев/R/Семинары/ПР4/4.xlsx",h=FALSE,dec=",",sep="\t")
W<-as.matrix.data.frame(Data)
W
S<-matrix(nrow=10,ncol=10)
for (i in 1:10)
  for (j in 1:10)
    S[i,j]<-i+j
S
# Задание 6
B<-matrix(1,nrow=40,ncol=40)
write.table(B,"~/git/FA/2 Курс/Зайцев/R/Семинары/ПР4/5.xlsx",quote=FALSE,col.names = FALSE,row.names = FALSE,sep="\t",dec=",")
