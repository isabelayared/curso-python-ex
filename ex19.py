#Caixa Eletrônico
total=int(input("Valor a ser sacado:"))
if total <=0:
 print("Valor inválido")
if total ==3:
  print("Valor não pode ser sacado, há somente cédulas de 2,5,10,20,50 e 100 reias")
else:
  notas100 = total // 100
  total = total % 100

  notas50 = total // 50
  total = total % 50

  notas20 = total // 20
  total = total % 20

  notas10 = total // 10
  total = total % 10

  notas5 = total // 5
  total = total % 5

  notas2 = total // 2
  total = total % 2
  print(f"Cédulas de 100 reias: {notas100}")
  print(f"Cédulas de 50 reias: {notas50}")
  print(f"Cédulas de 20 reais: {notas20}")
  print(f"Cédulas de 10 reais: {notas10}")
  print(f"Cédulas de 5 reais: {notas5}")
  print(f"Cédulas de 2 reais: {notas2}")
if total > 0:
  print(f"Valor restante que não pode ser sacado: {total} real(is)")
