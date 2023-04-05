#-----------calculando o aumento de valor com 15% usando porcentagem----------------#
#opção 01
salário = float(input('Digite seu salario do funcionário aqui?: R$'))#definindo variavel salario com classe primitiva flutuante com propriedade input 
aumento = salário + (salário * 15 / 100)#calculanndo o valor do aumento de valor com 15% no salario a ser inserido no terminal 
print('O funcionario com salario R${}, com aumento de 15% possuirá salario de: R${}'.format(salário, aumento))
#---------------------------------------------------------------------------------