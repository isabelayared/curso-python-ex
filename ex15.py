n=int(input("entre com um número entre 0 e 15:"))
print(n)
d1=n%2
quoc=n//2
d2=quoc%2
quoc=quoc//2
d3=quoc%2
quoc=quoc//2
d4=quoc%2
b=d4*10**3+d3*10**2+d2*10**1+d1*10**0
print(n, "em binário é", b)
