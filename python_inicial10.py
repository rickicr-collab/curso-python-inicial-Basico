#------------------Calculando aluguel de carros------------------#
Dias = int(input('quantos dias alugados? '))
km = float(input('quantos km rodados? '))
preço = (Dias*60) + (km*0.15)
print('O total a se pagar R$:{:.2f}'.format(preço))
#----------------------------------------------------------------