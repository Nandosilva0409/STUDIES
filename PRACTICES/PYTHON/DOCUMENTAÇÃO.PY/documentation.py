
# criar um sistema robotico 
import numpy as np 
    # biblioteca para operações matemáticas
    #com vetores e matrizes
from math import sin, cos
    
def create_robot(name):
        #criar uma lista vazia de 3 posições
        positions = []
        def move():
            x1=positions[0] + (cos((x2+90)*np.
                                pi/180))*lenght
            y1=(positions[1]+sin(((y2-45) *
                                np.pi)/180))*(lenght*0.7)#distancia do centro da roda com o chassi
            z1=-(positions[2]-sin((((z2)-60)*)
                                np.pi / 180))*(lenght*0.7)#distancia do centro da roda com a base
            return [x1 , y1 , z1 ]
        def turnleft ():
            global x2
            if ((x2 - 90)>(-180)):
                print("Turn left")
                x2 -= 10
            else:
                print ("Error")
def turnright () :
        global x2
        if (((x2)+90)<(-180)):
            print('turn right')
            x2 += 10
        else:
             print ('error')
def showposition() :
        print(f'The position is {positions}')
        # criação dos atributos das variáveis globais
        lenght = float(input('\nEnter the length of the wheels: '))
        x2 = int(float(input("\nEnter the initial angle in degrees for X axis")
                    ))
        % (-180),int(float(input("\nEnter the final angle in degrees for")
                        "X axis")))
        y2 = int(float(input("\nEnter the initial angle in degrees for Y")
                'axis')))%  180,(int(float(input("\nEnter")
                                            "\nthe final angle in degrees"
                                            '\nfor Y axis')))%   180
        z2 = int(float(input("\nEnter the initial angle in degrees for Z")
                'axis')))%(180),(int(float(input("\nEnter\nthe")
                                            "final angle in degrees \nfor Z")))%    180
    #atribuição aos valores na lista
        positions=[x2,y2,z2]

showposition()


