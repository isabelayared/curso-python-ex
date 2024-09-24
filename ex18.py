print("Formando um triângulo")
x=float(input("entre com a primeira medida em cm:"))
y=float(input("entre com a segunda medida em cm:"))
z=float(input("entre com a terceira medida em cm:"))
print(x,y,z)
if (x + y > z) and (x + z > y) and (y + z > x):
    if x == y == z:
        print("É um triângulo equilátero.")
    elif (x == y) or (x == z) or (y == z):
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Não é possível formar um triângulo com essas medidas.")
