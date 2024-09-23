largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))
area = largura * altura
litros = round(area/15,2)
print('Sua parede tem dimensão de {}x{} e sua área é de {} metros quadrados'.format(largura,altura,area))
print('Para pintar essa parede, você precisará de {} litros de tinta'.format(litros))
