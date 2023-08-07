# quero criar uma programa que saiba quem eu sou ( idade , aonde mora, o que gosto de fazer , o que eu estudo , aonde é a minha faculdade ), {quero que calcule a minha idade}.
'''
nome = input('Olá! tudo bem , sou sua assistente pessoal , voce poderia me informa seu nome por gentileza ?')
idade = input('qual a sua idade senhor? ops! , senhor não , jovem eu quis dizer!')
altura = input('qual sua altura')
casa =  input('voce pode me informa aonde voce mora ?')
lazer = input('o que voce gosta de fazer no seu tempo livre ?')
curso = input('voce esta cursando o que ?')
local = input(' aonde fica o local do seu curso?')

print(f'{nome} você tem {idade} anos e sua altura é de {altura} , e vc mora em {casa} , no seu tempo livre voce gosta {lazer} e esta cursando {curso}, que fica na {local}')
'''

'''
idade = int(input('Qual a sua idade? '))
ano_nascimento = int(input('Qual o ano de seu nascimento? '))
ano_atual = int(input('Qual o ano atual? '))

idade_atual = ano_atual - ano_nascimento

print(f'{idade} {ano_nascimento} {ano_atual}')
'''

# controle de fluxo  ( estrutura condicional ternaria ) if (se) , else (outro) , elif ()
# sistema medidor de velocidade 

 
'''
velocidade = 100

if velocidade > 200:                        
    print('acima da velocidade permitida!')  
    multa = (velocidade - 120) * 7

    print(multa)

elif velocidade < 70 :                           
    print('por favor dirigir acima de 80km/h')
    print('voce esta em uma via!') 

else :                        # else (outro)
    print('velocidade ok!')       
'''

'''
idade = 18

if idade < 18 :
    print('voce não pode entrar na festa por ser menor de idade')

else :
    print('pode entrar por favor!')    
'''



# quero montar um programa aaonde eu trabalho em um banco , eu vou aprovar um finaciamento de um carro .
# criterios : a pessoa tem que ter uma renda acima de 5mil R$ e tem que ter o nome limpo 

# operador logico ( and , or , not ) ---> boolean type 
'''
renda = True
nome = True

if renda and nome :
    print(f'financiamento aprovado')

else :
    print(f'seu financiamento foi negado')
'''

# multiplos operadores de comparação 
# ( and , or , >= , <= ) ---> podemos colocar varios multiplos operadores de comparação 
# criar um site aonde o produto custa entre 20 R$ a 40 R$ 
'''
# valor = 20 
valor = int(input('Qual o valor do produto? '))

 #if 20<=valor > 40:
if valor >= 20 and valor <= 40 :
    print(f'o valor do produto custa {valor} R$')
    

else :
    print(f'sua compra foi negada')
'''

# for loop utilizando numeros 
# ranger() ---> sua função é retonar um conjunto de numeros sequencias , que podem ser definidos de acordo com os parametros utilizados pela função.
# por padrão , o intervalo por ela começa pelo zero e é incrementadoum a um até atingir o pondo de parada. 

'''
for c in range(0, 20000):
    print(c)
'''

# for loop utilizando strings
'''
palavra = "espetacular"

for letra in palavra:
    print(f'{letra} esta dentro da palava {palavra}' )
'''

# for loop com if else
# criar um sistema aonde uma loja online quer enviar um e-mmail para seus clientes dizendo que sua compra foi enviada com sucesso
# enviar um e-mail com os detalhes da compra online (maximo 3 tentativas) para compra confirmadas.
'''
compra = True
dados_compra = 'compra no valor de R$10.50 e entrega confirmada'

for enviar in range(3):
    if compra :
        print(dados_compra)
        print('Os detalhes da compra foram enviados para o seu e-mail')
        print('obrigador por comprar em nosso site , volte sempre!')
        break
else: 
     print('falha na compra')
     print('tente novamente mais tarde')
'''
# sistema de confirmação de uma loja online     
'''
compra = False
email = input('digite o seu e-mail para confirmação da compra')
dados = 'compra no valor de 150.00'

for enviar in range(3):
    if compra:
        print(f'{dados} Os detalhes da compra foi enviado para o {email}')
        print('Obrigado por comprar em nosso site . Volte Sempre!')
        #envio do email aqui
        break
else:
    print('Falha na compra')    
    print (input(f'digite o seu email Para mais informaçoes '))
    print('A compra não pode ser efetuada porque o site esta fora do ar')
    print ('Tente Novamente Mais Tarde.') 
'''

# for loop - Nested loops (Outer loop) --> loop de fora , (Inner loop) --> loop de dentro.
'''
for numero1 in range(5): # quando a variavel (numero1) completa o seu primeiro loop 
    print(numero1)          
    for numero2 in range(5): #  A variavel (numero2) da cinco voltas sequidas 
        print( numero1,numero2)


for numero1 in range(1,11):
    print('Produto' + str(numero1))
    for numero2 in range(11):
        print(numero1,numero2)
'''

# for loop - Separando Strings
# Modificardor de FANTASTICO para F A N T A S T I C O 
'''
nome = input('digite seu nome')

for Letra in nome : 
    print(f' {Letra} ' , end='')
'''
'''
nome = input('digite o seu nome por favor !')

for letra in nome:
    print(f' {letra}' , end='')
'''    

# for loop - criando um retangulo
'''
linha = 7
coluna =7
simbolo = "*"

for linha in range(7):  # Outer loop (loop de fora)
    for coluna in range(7):  # Inner loop (loop de dentro)
        print(f'{simbolo}' , end='')
    print() # esse print esta relacionado ao loop de fora 
'''
# while loops 
# Excelente para loops dependendo de sua condição 
# Criar uma promoção para um produto no valor de R$100.

'''
valor = 100 # o produto ele vale R$100
dia = 0 
while valor > 20: # enquanto o valor for maior que R$20 ele vai imprimir a condição que foi desiguinada a ele 
    dia = dia + 1
    print(f'No dia {dia} o produto foi vendido por {valor} R$')
    valor = valor - 5
'''

# Operador ternario

##idade = int(input('Informe sua idade para votar'))
'''
if idade >= 16: 
    print('Voce pode votar')
else:
    print('Voce nao pode votar')
'''
#resultado = 'voto permitido' if idade >= 16 else 'voto não permitido'

#print(resultado)

# diferença entre for loop e while loop 
# if e else ( É para um condição de verdadeiro ou falso e ele não fica girando) 
# for loop (É quando voce sabe a quantidade de vezes que uma condição seja executada)
# while loop é quando voce não sabe quantas vezes uma determinada condição seja executada , voce espera atingir um resultado 

# Publicar um produto com comissão de 10% se for acima de R$20 
'''
preco_produto = float(input('qual o valor do seu produto em R$ '))

while preco_produto > 20: 
    valor = (preco_produto * 0.10) + preco_produto
    print(f'o valo do produto é de {valor}R$')
    break
'''

# Quero criar uma promoção de um produto na qual esse produto tem o valor (x)
# E a cada venda desse produto é gerado uma comissão 10% desse produto 
'''
preço_produto = int(input('qual o valor do seu produto ?'))


if preço_produto >= 100: 
    valor = (preço_produto * 0.10) + preço_produto
    print(f'o valor da sua compra foi de R${valor} ,')
    print(f'voce ganhou {preço_produto * 0.60} de comissão por venda')
    break 
'''

# funções ( function ) como funciona uma função?
# def soma(): #funçãos são definidas pela palavra reservada
# DRY - don`t repeat yourself (função foi feita pra vc não ficar se repetindo)
'''
def boas_vindas():
    print("Bom dia")
    print("Boa tarde")
    print("boa noite")
    return "Fim"

print(boas_vindas())
'''

# criando função de soma
'''
def soma():
    valor1 = 100
    valor2 = 350
    resultado= valor1+valor2
    if resultado ==  450 :
        print ("resultado igual ao esperado!")
        return True
    else:
        print ('errou!')
        return False
    
def somar():
    valor1 = 200
    valor2 = 350
    resultado= valor1+valor2
    if resultado < 450:
        print ("resultado igual ao esperado!")
        return True
    else:
        print ('errou!')
        return False

soma()
somar()
'''
# indice de massa corporal (IMC)

def calculadoraImc():
    altura = float(input('Digite sua Altura em metros'))
    peso = float(input("digite o seu peso"))
    imc= peso/(altura**2)

   
    if imc <= 15 and 18.5:
        return f"Abaxo do peso , Seu imc é de : {imc}"
    elif imc >= 18.6 and 24.9 :
        return f"Peso normal, seu imc é de : {imc}"
    elif imc >= 25 and 29.9:
        return f"Acima do Peso, seu imc é de : {imc}"
    elif imc >= 30 and 39.9:
        return f"Obesidade grau I, seu imc é de : {imc}"
    elif imc >= 40 :
        return f"Obesidade grau II ou grau III, seu imc é de : {imc}"
    else :
        return f"valor invalido!" 


print(calculadoraImc())
    














