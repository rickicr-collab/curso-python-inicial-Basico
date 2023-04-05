# - - - - - - - - - - - - - - - - - - - - - - - - -
#cores no terminal
#codigo principal para formatação da cor \033[style;texto;background m

#style [0 - none, 1 - bold(negrito), 4 - underline(sublinhado), 7 - negativo
#cordetexto [30 - branco, 31 - vermelho, 32 - verde, 33 - amarelo, 34 - azul, 35 - margenta , 36 - ciano , 37 - cinza]
#cordefundo [40 - branco, 41 - vermelho, 42 - verde, 43 - amarelo, 44 - azul, 45 - margenta, 45 - ciano, 47 - cinza]
# \033[m - gera o fundo preto padrão do terminal  
# \033[7;30m - gera um fundo branco com cor preta com o algarismo 7 representando a função negativa de formatação de texto
# \033[m - no final da string há uma especie de limitação da função background a apenas a string formatada
# ao atribuir formatação para variaveir declaradas com chaves em print as variaveis serão formatadas no terminal ao realizar o print exemplo \033[34;44m{} nesse caso os valores nessas chaves serão formatados de acordo os dados fornecidos pelo programador 
#primeira forma de utilização 
print('\033[33;43m Ola mundo!\033[m')
#2 forma de utilização com variaveis e executando formatação no print
a = 3
b = 5
print('os valores das variaveis são \033[33m{}\033[34m{}\033[m'.format(a, b) )

#3 format de utilização é utilizando a função format apricando os códigos de formatação usando a função
nome = 'ricardo'.capitalize()
print('Muito prazer em te conhecer,{}{}{} !!!!'.format('\033[35m', nome,'\033[m'))