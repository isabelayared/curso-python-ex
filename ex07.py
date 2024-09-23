n = float(input('Quanto dinheiro quer converter para dólar?'))
dolar = round(n/5.44,2)
print('Com R${}, você pode comprar US${}'.format(n,dolar))
