from random import randrange
import re

def leer_texto():
    with open("Palabras.txt", encoding="UTF-8") as archivo:
        texto=archivo.read()
        expresion_regular= r'[,.]'
        texto_sin_caracteres_especial = re.sub(expresion_regular,'',texto)
        lista = texto_sin_caracteres_especial.strip().split()
    return lista

def palabra():
    lista_palabras=leer_texto()
    numero_posicion = randrange(0,len(lista_palabras))
    repuesta=(lista_palabras[numero_posicion],numero_posicion)
    return repuesta

def mostrar_ahorcado(intentos):
    dibujo = [
        '''
           _______
          |/      |
          |      
          |    
          |      
          |    
        __|________
        |         |__
        |___________|
        ''',
        '''
           _______
          |/      |
          |     (o_o)
          |    
          |      
          |    
        __|________
        |         |__
        |___________|
        ''',
        '''
           _______
          |/      |
          |     (o_o)
          |       |
          |       |
          |    
        __|________
        |         |__
        |___________|
        ''',
        '''
           _______
          |/      |
          |     (o_o)
          |      \|
          |       |
          |    
        __|________
        |         |__
        |___________|
        ''',
        '''
           _______
          |/      |
          |     (o_o)
          |      \|/
          |       |
          |    
        __|________
        |         |__
        |___________|
        ''',
        '''
           _______
          |/      |
          |     (o_o)
          |      \|/
          |       |
          |      / 
        __|________
        |         |__
        |___________|
        ''',
        '''
           _______
          |/      |
          |     (x_x)
          |      \|/
          |       |
          |      / \\
        __|________
        |         |__
        |___________|
        '''
    ]
    return dibujo[intentos]