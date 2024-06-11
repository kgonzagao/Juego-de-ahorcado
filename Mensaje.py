# Creamos la clase Mensaje, para que pueda recibir por parametros
# el color que deseamos por pantalla y el mensaje a mostrar

class Mensaje():
    def __init__(self,pColor,pMensaje):
        self.color=pColor
        self.mensaje=pMensaje

    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color,self.mensaje)


    def inicializar_palabra_oculta(palabra):
        return "_" * len(palabra)

    def mostrar_palabra_oculta(palabra, letras_adivinadas):
        resultado = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                resultado += letra
            else:
                resultado += "_"
        return resultado
