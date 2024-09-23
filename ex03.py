# +	Adição	Realiza a soma de ambos operandos.
# -	Subtração	Realiza a subtração de ambos operandos.
# *	Multiplicação	Realiza a multiplicação de ambos operandos.
# /	Divisão	Realiza a Divisão de ambos operandos.
# //	Divisão inteira	Realiza a divisão entre operandos e a parte decimal de ambos operandos.
# %	Módulo	Retorna o resto da divisão de ambos operandos.
# **	Exponenciação	Retorna o resultado da elevação da potência pelo outro.


# ==	Igual a	Verifica se um valor é igual ao outro
# !=	Diferente de	Verifica se um valor é diferente ao outro
# >	Maior que	Verifica se um valor é maior que outro
# >=	Maior ou igual	Verifica se um valor é maior ou igual ao outro
# <	Menor que	Verifica se um valor é menor que outro
# <=	Menor ou igual	Verifica se um valor é menor ou igual ao outro


# =	x = 1
# +=	x = x + 1
# -=	x = x - 1
# *=	x = x * 1
# /=	x = x / 1
# %=	x = x % 1


# and	Retorna True se ambas as afirmações forem verdadeiras
# or	Retorna True se uma das afirmações for verdadeira
# not	retorna Falso se o resultado for verdadeiro

# is	Retorna True se ambas as variáveis são o mesmo objeto
# is not	Retorna True se ambas as variáveis não forem o mesmo objeto

# in	Retorna True caso o valor seja encontrado na sequência
# not in	Retorna True caso o valor não seja encontrado na sequência

n = int(input('Digite um número:'))
a = n - 1
s = n + 1
d = n * 2
t = n * 3
r = n ** (1/2)
print('Analisando {}: \n seu antecessor é {}\n seu sucessor é {}\n seu dobro é {}\n seu triplo é {} \n sua raiz quadrada é {}.'.format(n, a, s,d,t,r))

