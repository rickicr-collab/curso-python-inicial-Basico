#----------Calculando valores metricos---------------------#
#calcular valores metricos 
a = float(input('Qual a altura da parede: '))
l = float(input('Qual a largura da parede:'))
m = a*l#calculando o valor do metro quadrado realizando a operação multiplicando a altura vezes a largura 
t = (a*l)/2#aqui mostra a operação para se obter a quantidade de litros de tinta para realizar a pintura 
print('Você vai precisar de:{} litros de tinta'.format(t))

#opção 02
larg = float(input('Digite a Largura da parede: '))#atribuimos o variavel largura sobre propriedade input sobre classe primitiva flutuante
alt = float(input('digite a altura da parede: '))#atribuimos a variavel altura sobre propriedade input sobre classe primitiva flutuante 
area = larg * alt#aqui declaramos a variavel area realizando o calculo referente a variavel largura multiplicando pela variavel altura 
print('Sua parede tem as dimensoes de {:.2f} x {:.2f} sua area será {:.2f}m²'.format(larg, alt, area))
tinta = area/2#aqui declaramos a variavel tinta sobe operação usando a variavel area dividindo por 2 referente aos metros quadrados de tinta buscados 
print('para pintar essa parede, você precisa de: {:.2f}litros de tinta'.format(tinta))
