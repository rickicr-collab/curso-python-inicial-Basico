# manipulando textos -----------------------------------------------------

frase = 'Curso em video python'
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print(frase.upper())
print(frase.lower())
print(frase.find('deo'))
print(frase.find('android'))
print(frase.count('o'))
print(frase.split())
print(''.join(frase))
print(frase[::2])
print(frase.upper().count('O'))
print('Curso' in frase)
print('android' in frase)

#print.len(frases) - mostra quantos caracteres possui a string contando do valor 0 da esquerca pra direita 
#print(frase[9]) - programa imprimi o caractere que mostra na posição nove que no caso seria 'v'
#print(frase[9:13]) - programa imprimi os valores com intervalos iniciando da posição 9 até a posição 13 que seria 'vide' no entanto a posição 13 é ignorada e vai até a posição 12 sempre considerar um posição a menos no fatiamento de string
#print(frase[9:21:2]) - programa realiza o fatiamento da posição inicial 9 até a posição 21 com intervalos de 2 em dois o restante dos caracteres é ignorado resultando: 'VdoPto'.
#print(frase[:5]) - progrma irá realizar o fatiamento da posição inicial 0 pois não foi informado inicalmente o incio então ele irá inciar automaticamente da posição 0 resultando: 'Curso'
#print(frase[15:]) - programa irá realizar o fatiamento da posição inicial 15 até o final que seria: 'Python'
#print(frase[9::3]) - programa realiza o fatiamento da posição inicial 9 até o final realizando intervalo de 3 algarismos que como resultado ficaria :'VePh'

## atributos de fatiamento Analise##

#print.len(frase) - função de analise que mostra o comprimento de uma cadeia de caracteres que na frase acima seria - 21 caracteres 
#print(frase.count('o')) - ele informa quantos caracteres 'o' exestem na frase que seria no casco fa frase informada - 3
#print(frase.count('o',0,13)) - ele informa quantos caracteres 'o' existem na frase com intervalo inicial 0 a intervalo 13 que seria 12 afinal o 13 é ignorado nas linguagens de programação que teria resultado - 1
#print(frase.find(deo)) - ele mostra quantas vezes ele encontrou o caractere 'deo' na frase mostrando sua posição que seria - 11
#print(frase.find('android')) - quando coloca um string que não existe na frase do conteudo da variavel ele retorna o valor na tela de -1
# 'curso' in frase - ele pergunta na frase existe a string curso  se ao verificiar existe a string ele retorna TRUE mais não existir ele retorna FALSE 

## atributos de fatiamento Transfomação ##

#print(frase.replace('Python','Android')) - realiza a substituiçao da string anterior pela nova string , embora android tenha uma variavel a mais na frase a função faz a realocação na frase para que posssa ser feita a substituição da string.
#print(frase.upper()) - função que ajusta na frase o aumento dos caracteres minusculos transformando todos em caracteres maiusculos 
#print(frase.lower()) - função que ajusta na frase a diminuição dos caracteres maiusculos transformando todos os caracteres minusculos
#print(frase.capitalize()) - função que que transforma o primeiro caractere em maiusculo e todos o outros caracteres em minusculos 
#print(frase.title()) - função que transforma os primeiros caracteres de todas as palavras na string em maiusculos e os outros caracteres em minusculos 
#print(frase.strip()) - função que remove os espacos desnecessarios de inicio e fim de frase quando houver desconsiderando o espaço entre as frases 
#print(frase.rstrip()) - função que remove os espacos desnecessarios do lado direito
#print(frase.lstrip()) - função que remove os espacos desnecessarios do lado esquerdo 
#print(frase.split()) - função que cria uma divisão nos espacos existentes entre as strings 
