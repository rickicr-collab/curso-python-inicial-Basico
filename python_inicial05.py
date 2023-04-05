#script com valores flutuantes reais 

n = float(input('Digite um numero'))
print(n);

#Operações Aritmericas 

#Exemplos 001

#5+3*2==11
#3*5+4**2==31
#3*(5+4)**2==243

#exemplo 002
#opçoes do format na função print usando operaçoes aritmericas 

n1 = int(input('Digite um numero: '))#função input com classe primitiva já inserida antecipadamente na primeira variavel
n2 = int(input('Digite outro numero: '))#função input com classe primitiva já inserida antecipadamente na segunda variavel
print('A soma vale: {}'.format(n1+n2))#imprimi o valor da soma vas varriaveis n1 e n2
print('A Subtração: {}'.format(n1-n2))#imprimi o valor da subtração dos variaveis n1 e n2
print('A Multiplicação: {}'.format(n1*n2))#imprimi o valor da subtração dos variaveis  n1 e n2
print('A Divisão: {}'.format(n1/n2))#imprimi o valor da divisão dos variaveis n1 e n2
print('Divisão inteira é : {}'.format(n1//n2))#imprimi o valor da divisão inteira das variaveis n1 e n2
print('A potenciação é : {}'.format(n1**n2))#imprimi o valor da potenciação de n1 e n2

#{:.3f} - modifica pra numeros flotoantes possuirem 3 algarismo no maximo
# end=' ' - função que não impede a quebra de linha na função print
# \n - função de quebra linha nos comentario do print
# end ' >>> ' outra opção para a função end não quebrar a linha e continuar os print posteriores 

#exemplo 003 função format do print usando string como valores 
nome = input('digite seu nome: ')
print('Prazer! , em te conhecer {:=^15}!'. format(nome))#formatação centralizando o nome em 15 espaços com caractere =
print('Prazer! , em conhecer {:>15}!'. format(nome))#formatação com 15 espaços para a direita na função print
print('Prazer! , em conhecer {:<15}!'. format(nome))#formatação com 15 espaços para a esquerda na função print
print('Prazer! , em conhecer {:^15}!'. format(nome))#formatação com 15 espaços e nome centralizado na função print