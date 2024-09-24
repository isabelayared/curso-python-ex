Dnasc=int(input("entre com o dia de nascimento:"))
print(Dnasc)
Mnasc=int(input("entre com o mes de nascimento:"))
print(Mnasc)
Anasc=int(input("entre com o ano de nascimento:"))
print(Anasc)
Datu=int(input("entre com o dia atual:"))
print(Datu)
Mnatual=int(input("entre com o mes atual:"))
print(Mnatual)
Aatual=int(input("entre com o ano atual:"))
print(Aatual)
Adif=Aatual-Anasc
if Mnatual<Mnasc or (Mnatual==Mnasc and Datu<Dnasc):
    Adif=Adif-1
if Adif>=18:
 print("pode")
else:
 print("não pode")
