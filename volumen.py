import math
pi = math.pi
def radio():
     rad = int (input('text radio'))
     altura = int(input(' text altura '))
     return rad, altura

def cono():
    radios, alturas = radio()
    area = pi * radios**2 * alturas /3
    print('el área es', area)

def cilindro():
    radios, alturas = radio()
    area = pi * radios**2 * alturas
    print('el área del cilindro es ', area)

def esfera():
    radios, alturas = radio()
    area = pi *radios**3 * 4 /3
    print('el área es ', area)
   
def run ():
    # calcular el volúmen
  
    print('que deseas calcular?')
    print('1 ==> cono')
    print('2 ==> cilindro')
    print('3 ==> esfera')
    opciones = int (input(' '))
    if( opciones == 1 ):
        cono()
    elif(opciones ==2):
        cilindro()
    elif(opciones ==3):
        esfera()
    elif(opciones != 3):
        print("check!")
    


if __name__ == '__main__':
    run()