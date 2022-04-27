from scipy.stats import chi2
m=100
n=30
S1=18.54
a=0.05
S0=16
z=1-a
chi2Nabl=(n*S1)/S0
chi2Cr=chi2.ppf(z,n)
print("Задача 1 - " + str(chi2Nabl) + " "+str(chi2Cr) + " Принимаем H0")
m=400
n=28
S1=16.34
a=0.01
S0=14
z=1-a
chi2Nabl=(n*S1)/S0
chi2Cr=chi2.ppf(z,n)
print("Задача 2 - " + str(chi2Nabl) + " "+str(chi2Cr) + " Принимаем H0")