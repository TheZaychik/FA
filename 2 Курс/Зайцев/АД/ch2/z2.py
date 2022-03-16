from scipy.stats import chi2

sr_v = 400
n = 28
s0_2 = 16.34
y = 0.98
z1 = (1 + y) / 2
z2 = (1 - y) / 2
ppf1 = chi2.ppf(z2, n)
ppf2 = chi2.ppf(z1, n)
left = n * s0_2 / ppf2
right = n * s0_2 / ppf1

print(z1)
print(z2)
print(ppf1)
print(ppf2)
print(left)
print(right)
