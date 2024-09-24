n= int(input("Digite um número de 0 a 10(base decimal): "))

binario=""
temp = n
while temp>0:
  resto = temp % 2
  binario = str(resto) + binario
  temp = temp // 2
print("O número", n, "em base 2 é:", binario)
octal = ""
temp = n
while temp > 0:
    resto = temp % 8
    octal = str(resto) + octal
    temp //= 8
print("O número", n, "em base 8 é:", octal)
