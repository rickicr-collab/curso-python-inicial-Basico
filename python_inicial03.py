#Criar um script em python que mostra a soma entre dois numeros

def sum ( num1 , num2 ): # usando a função soma para realizar a soma entre duas variaveis 
  return num1 + num2

print( "Desafio 03" )
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

print("O resultado da Soma é: %d " %sum (num1 , num2))