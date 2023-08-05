 # print() --> sua funçao é exibir texto na tela (console),e nela pode ser colados variaveis , numeros e textos
'''
print("óla")
print("tudo bem?")
print("que dia é hoje?")

# Meu segundo código 
print(2+2)

'''

'''
Este programa imprime os textos "ola" e "tudo bem?" seguido de 
2 + 2.
print("tudo bem?")
'''

# DATA TYPES ( TIPOS DE DADOS ) : text and numbers
'''
STRING - text(texto)
(STR)

NUMBERS - Integer= Inteiro( 1 , 2 ,3 ...) , qualquer número que não tenha fração o python entende como número unteiro
          float = Fração ( 3.5, 5.6, 7.1)

BOOLEAN TYPE : True our false 
(BOOL)        
'''

# VARIABLES

'''
Variaveis são um containner que são usados para armazenar dados 

x = 2 (interger)

 A = 'ola' (string)

y = 3.5 (float)
'''

'''
x = 2
A = 10
y = 20

print(x)

print(A)

print(y)
'''

# modificando os tipos de Dados
'''
x = str(3) # A VARIAVEL (x) DE NUMERO INTERIRO , PASSOU A SER UMA VARIAVEL STRING
A = int(4) # A VARIAVEL (A) continua sendo uma vaeriavel de numero intero
y = float(5) # A VARIAVEL (y) passou a ser uma fração 

print(x+x)
print(A+A)
print(y+y)

print(type(x))
'''


# Fernando tem 22 anos de idade e mora em campos dos goytacazes 

#nome = "marlucia"
#idade = 15
#idade = str(idade)
#cidade = 'campos dos goytacazes'
#distração = 'dormir'

#print(' o ' + nome +  " tem "  + idade + " anos de idade e mora em " + cidade + '.')

'''
nome = input('qual é o seu nome?')
idade = input('quantos anos voce tem?')
cidade = input("aonde voce mora?")
distração = input('o que gosta de fazer no seu tempo livre?')

print(' A '+ nome +' tem '+ idade +' anos de idade e mora em '+ cidade + ' e é mandona ' + '.')
'''



#calculando a idade com input 

'''
ano_nascimento = input('em que ano voce nasceu')
idade = 2022 - int(ano_nascimento)
print(idade)
'''

# slice : consite em obter uma sub-lista contendo os elementos de uma posição inicial até uma posição final de uma lista

'''
fruta = "Abacate"
#index   0123456

9print(fruta[0:7])

'''
'''
valor = 1800.45
valor = str(valor)
#index  0123456

print(valor[0:])
'''

# formated strings
'''
nome = 'lucas'
sobrenome = 'silva'
idade = str (22)
cidade = 'campos dos goytacazes'
cursando = "Analise e desenvolvimento de sistemas"
faculdade = 'Estacio de sa'
local = str (28)
profissão = 'Analista de sistemas'
aprendendo = 'python'

print(f'{nome} {sobrenome} tem {idade} de idade e mora em {cidade} ,e atualmente esta cursando {cursando} na {faculdade} , que fica na {local} e esta aprendendo {aprendendo} , e atualmente trabalha como {profissão}')
'''

# Metodos para strings : lower(letra minuscula), upper(letra maiuscula), capitalize(pega a primeira letra e transforma ela em maiuscula) , find (mostra a posição da letra ou aonde inicia uma palavra), replace (ele troca um dado antigo por outro)
'''
mensagem = 'eu estou amando estudar python'
# index     0123456789
print(mensagem.strip())

'''

# OPERAÇÕES MATEMATICA COM PYTHON (REVISÃO)
# MULTIPLICAÇÃO E DIVISÃO 
# ADIÇÃO E SUBTRAÇÃO
# PARENTESES
# ESPONENCIAS
'''
calculo = 2 + 2 * 3

print(calculo)

'''

# OPERADPRES DE COMPARAÇÃO 

#operadores = 200 == 200
#operadores1 = 20 != 10
#operadores2 = 300 > 500
#operador3 = 30 < 40
#operador4 = 100 >= 90
#operador5 = 200 <= 200

#print(operador5)
#print(operador4)
#print(operador3)
#print(operadores2)
#print(operadores1)
#print(operadores)

'''
# == Equal 
# != Not Equal
# > Greater than 
# < Less than
# >= Greater than or equal To 
# <= Less than or equal To
'''

# operadores de atribuição ( é uma forma que tem de se realizar calculos matematicos com um codigo um pouco mais simples )

'''
x = 200
# x = x + 100
x += 100

print(x)
'''








