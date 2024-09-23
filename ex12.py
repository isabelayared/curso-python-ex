qnt_km = float(input("digite a quantidade em Km percorridos com o carro:"))
qnt_dias = int(input("digite a quantidade de dias o qual o carro foi alugado: "))
pagar = (qnt_km*0.15) + (qnt_dias*60)
print("O preço a pagar é R$", pagar)
