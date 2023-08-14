
# criar um sistema de emprestimo bancario 
'''
import random
from time import sleep
valor = int(input('Digite o valor do emprestimo: ')) # entrada de dados
print(f'{valor}*10')
sleep (1.5)    # tempo para a mensagem aparecer
if 6 <= valor < 39 :
    print(f"o seu saldo é de {valor} e voce pode fazer um parcelamento de ate 12 vezes")
    print ('-=-'*8 )
    for c in range(1,4):
        num =random.randint(-7,-1)+c
        if valor >num and valor<=(num+1)*12:
            print(f'{c}° Parcela - {num}')
            break
        else:
            print('valor invalido')
'''
