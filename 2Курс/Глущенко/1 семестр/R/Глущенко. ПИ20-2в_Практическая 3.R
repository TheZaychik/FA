n<-2
n
typeof(n)
n<-as.integer(n)
n
typeof(n)
Flag<-TRUE
Flag
typeof(Flag)
A<-(2>3)
A
typeof(A)
n<-2L
n
typeof(n)
n<-2.0
n
typeof(n)
n<-log(2)
n
typeof(n)
z<--3+4i
z
typeof(z)
z^2 #степень качественной части
Re(z) #Вещ. часть
Im(z) #Мнимая часть
Arg(z)
Mod(z)
a<-c(2,-3,3,-3,1)
polyroot(a)
symbol<-"A"
symbol
typeof(symbol)
paste(symbol,"B",sep="")
Cases <-c("A","B","B","A","FULL","A","B","A1","A1")
Cases
Case_Factor<-factor(Cases)
Case_Factor
plot(Case_Factor)
str(Case_Factor)
Case_Factor_Order<-ordered(Case_Factor,levels=c("Full","B","A","A1"))
Case_Factor_Order
Case_Factor_Order[4]
Case_Factor_Order[5]
Case_Factor_Order[4]<Case_Factor_Order[5]
S<-c(0,1,2,3,4,5,6,7,8,9)
S
S[2]
Q<-S[-3];Q
V<-S[3:5];V
W<-S[S>7];W
names(S)<-c("number 1", "number 2")
S
S["number 1"]
S<-c(number1=0,number2=1)
S
typeof(S)
is.vector(S)
str(S)
M<-array(data="A",dim=c(3,4));M
M[3,4]<-2;M
dimnames(M)<-list(NULL, c("One","Two","Three","Four"));M
M[2,"Three"]
dim(M)<-c(6,2);M
ФИО<-c("Билан","Буянтогтох","Гаджиев")
КНИЖКА<-c(151416,153305,152613)
A1<-c(20,11,3)
A2<-c(20,11,2)
ЗАЧЕТ<-c(60,50,0)
ИТОГ<-c(100,72,5)
ОЦЕНКА<-c("зачтено","зачтено","не зачтено")
Exam<-data.frame(Name=ФИО,N=КНИЖКА,ATT1=A1,ATT2=A2,Z=ЗАЧЕТ,ALL=ИТОГ,Rez=ОЦЕНКА)
Exam
Exam$Name
Exam[1,]
Exam[1,1]
Exam$Name[1]
Exam[2,6]
Exam$ALL[2]
library("dplyr")
H<-dplyr::filter(Exam,Rez=="зачтено");H
H<-dplyr::select(Exam,Name,ALL,Rez);H
H<-dplyr::mutate(Exam,Attestation=ATT1+ATT2)
H
dplyr::glimpse(H)
n.v<-"04.06-3-3611"
year<-"2016/2017"
n.s<-3
name.g<-"H3-1"
subject<-"Мат.Стат."
professor<-"Загадаев Сергей Алексеевич"
vedomost<-list(n.ved=n.v,year=year,n.sem=n.s,groop=name.g,subject=subject,professor=professor,exam=Exam)
vedomost
glimpse(vedomost)
vedomost[[1]]
vedomost$exam
vedomost$exam$ALL[1]
vedomost$exam[1,6]
vedomost[[7]][1,6]
#Задания
#1 a)
a<-c(25,6,1)
polyroot(a)
#1 b)
a<-c(25,8,1)
polyroot(a)
#1 c)
a<-c(-81,0,0,0,1)
polyroot(a)
#1 d)
a<-c(3+4i,-(3+4i),-1,1)
polyroot(a)
#1 e)
a<-c(3,-3+4i,-(1+4i),1)
polyroot(a)
#Задание 2 a)
z<-(2+1i)^4;
z<-z/(3-4i);z
Re(z) #Вещ. часть
Im(z) #Мнимая часть
#Задание 2 b)
z<-(3-5i)*(2+5i)
z<-z/(3+4i);z
Re(z) #Вещ. часть
Im(z) #Мнимая часть
#Задание 3
setka<-c("","Доходы, трлн.рублей","в % к ввп","Нефтегазовые, трлн.руб","в % ко всем доходам")
y2014<-c("оценка",14.07,19.9,7.5,51.9)
y2015<-c("проект бюджета",15.08,19.5,7.7,51.2)
y2016<-c("проект бюджета",15.8,19.0,7.8,50.8)
y2017<-c("проект бюджета",16.5,18.4,8.34,49.6)
budget<-data.frame(setka=setka,year_2014=y2014,year_2015=y2015,year_2016=y2016,year_2017=y2017)
budget
#Чтобы можно было удобно считать
setka1<-c("Доходы, трлн.рублей","в % к ввп","Нефтегазовые, трлн.руб","в % ко всем доходам")
y20141<-c(14.07,19.9,7.5,51.9)
y20151<-c(15.08,19.5,7.7,51.2)
y20161<-c(15.8,19.0,7.8,50.8)
y20171<-c(16.5,18.4,8.34,49.6)
budget1<-data.frame(setka=setka1,оценка2014=y20141,проект2015=y20151,проект2016=y20161,проект2017=y20171)
budget1
#Задание 4
vid="Административнй штраф"
date="-"
summa=15550
tabl<-data.frame(вид_платежа=vid,дата=date, сумма=summa);tabl
pol.pla<-"УФК по МО"
inn="7702300872"
kpp="770201001"
bank="Отделение №1 МГТУ Банка России"
chet="40101810600000010102"
bik="044583001"
kbk="18811630020016000140"
okato="4621800000000"
fio="Иван Иванович Иванов"
adres="Москва, Красная площадь 1"
kvitanzia<-list(получатель=pol.pla,ИНН=inn,КПП=kpp,Банк=bank,счет=chet,БИК=bik,КБК=kbk,ОКАТО=okato,ФИО=fio,адрес=adres,ФИО_адрес=tabl)
kvitanzia
