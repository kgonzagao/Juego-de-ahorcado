from GeneradorPalabras import palabra,mostrar_ahorcado
from Mensaje import Mensaje

mensaje_bienvenida = '''
¡Bienvenido al Juego del Ahorcado!

El objetivo del juego es adivinar la palabra oculta.
Tienes un número limitado de intentos para adivinar cada letra de la palabra.
Cada vez que falles una letra, se dibujará una parte del ahorcado.

¡Buena suerte y que empiece la diversión!
'''
color_mensaje = 35
print(Mensaje(color_mensaje,mensaje_bienvenida))
print(Mensaje(33,mostrar_ahorcado(0)))

adivinar,posicion=palabra()
print(Mensaje(36,f'La Palabra adivinar tiene: {len(adivinar)} letras'))

def obtener_max_intentos(tamaño_palabra):
    if tamaño_palabra <= 5:
        return 4  
    elif tamaño_palabra <= 6:
        return 5  
    elif tamaño_palabra <= 8:
        return 6 
    else:
        return 7


palabra_oculta = Mensaje.inicializar_palabra_oculta(adivinar)
print(adivinar)
intentos=obtener_max_intentos(len(adivinar))

def mostrar_letra_en_palabra(palabra, caracter):
    palabra_mostrada = ""
    for letra in palabra:
        if letra == caracter:
            palabra_mostrada += letra
        else:
            palabra_mostrada += "_"
    return palabra_mostrada

while True:
    print(f"Intentos: {intentos} Palabra: {palabra_oculta}") 
    palabra_adivinada=input(Mensaje(34,"Ingresa la palabra: ")).lower()
    if len(palabra_adivinada) > len(adivinar):
        print(Mensaje(31,"Error.. la palabra ingresada es larga a la que debes de adivinar"))
    else:
        palabra_oculta = mostrar_letra_en_palabra(adivinar, palabra_adivinada)
        if adivinar.lower() == palabra_adivinada:
            print(Mensaje(32,f"Felicidades ganaste !! era la palabra: {adivinar}"))
            break
        else:
            if intentos > 1:
                intentos -=1
                print(Mensaje(33,mostrar_ahorcado(-(intentos+1))))
            else:
                print(Mensaje(31,f"Perdista la palabra para era: {adivinar}"))
                print(Mensaje(31,mostrar_ahorcado(-intentos)))
                break