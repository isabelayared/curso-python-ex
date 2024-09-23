n = float(input('Digite uma distância em metros:'))
km = n/1000
hm = n/100
dam = n/10
dm = n * 10
cm = n * 100
mm = n * 1000
print('A distância de', n, 'm, corresponde a:')
print('\n {}Km \n {}Hm \n {}Dam \n {}Dm \n {}Cm \n {}Mm'.format(km,hm,dam,dm,cm,mm))
