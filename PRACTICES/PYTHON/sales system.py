
# sistema de venda de carro 
# criação das variaveis necessárias
#variáveis globais global cpf, rg, salario, senha, numero_de_vendas, total_gasto
 #variável local login 

    
def cadastro_cliente (**cliente): # Area de cadastramento
    nome = str(input('Qual seu nome ? '))
    Email = str(input('Digite seu e-mail'))
    CPF = int(input('Insira seu número de CPF:'))
    RG = int(input('insira seu número de RG:'))
    cliente = {'nome':nome,'email':Email ,'cpf':CPF,'rg':RG }
    return cliente
 
def logar (cliente):
    email= input("digite o seu EMAIL")
    if email == cliente['email']:
        return True
    else :
        print ('Usuario ou Senha Incorretos')

def verificar_login (senha):
    if senha == '1234567890' :
        print ('Bem Vindo ap sistema')
    else:
        print ("Senha incorreta")
'''
def atendente(): # Area de Atendimento

    print("Bem-Vindo ao Sistema")

    usuario = input("Digite seu e-mail:")
    senha = int(input('digite sua senha:'))
    while usuario == '<EMAIL>':
        continue 
    else:
        print('usuario não encontrado!')
    if senha == '<PASSWORD>':
        return True
    else:
        print('senha incorreta!')
'''

def sistema_compra(**carro): # area de vendas

    valor_total=0.0
    for i in range (1 , len(carro)):
        preco = float((carro[i]['preço']))
        quantidade =int ((carro[i]['quantidade'])) 
        valor_total += preco * quantidade
        print ('O valor a ser pago é {}'.format(valor_total))

def estoque(**carro):
    lista=[marca , modelo , cor , ano ]
    marca = ['ford', 'fiat' , 'Mercedes' , 'Ferrari']
    modelo=['ka', 'k4' , 'k5' , 'k6']
    cor=['azul','vermelho', 'preta' , 'cinza' ]
    ano=[2019]
    for i in range (len(lista) ):
        print(f'{marca} {modelo} {cor} {ano}'.format(*lista [i]))
        print('Obrigado por compra em nosso site !')

''''
atendente()
'''
cadastro_cliente('nome' , 'email' , 'cpf' , 'rg')
logar('email')
verificar_login('1234567890')
sistema_compra('preço' , 'quantidade' , 'valor_total' )
estoque()







