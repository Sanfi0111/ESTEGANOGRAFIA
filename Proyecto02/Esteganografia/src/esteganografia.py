import numpy as np
from PIL import Image 
"""
    Clase que se encarga de ocultar un mensaje en una imagen o develar el mensaje oculto de una imagen
"""
class Esteganografia:
    """"
        Método que se encarga de encriptar un mensaje en una imagen.
        Pametros:
        imagen : La imagen en la que se quiere ocultar un mensaje
        mensaje : El mensaje que se quiere ocultar
        imagenOculta : El nombre de la imagen que que tendrá el mensaje oculto
        """
    def Oculta(self,imagen, mensaje, imagenOculta):
        img = Image.open(imagen, 'r')
        width, height = img.size
        array = np.array(list(img.getdata()))
        if img.mode == 'RGB':
            n = 3
        elif img.mode == 'RGBA':
            n = 4
        totalPixeles = array.size//n
        mensaje += "$3ncripTAd0"
        mensajeBinario = ''.join([format(ord(i), "08b") for i in mensaje])
        pixelNecesario = len(mensajeBinario)
        if pixelNecesario > totalPixeles:
            print("Error, imagen demasiado pequeña para el mensaje a ocultar")
        else:
            index=0
            for p in range(totalPixeles):
                for q in range(0, 3):
                    if index < pixelNecesario:
                        array[p][q] = int(bin(array[p][q])[2:9] + mensajeBinario[index], 2)
                        index += 1
            array=array.reshape(height, width, n)
            imagenEcriptada = Image.fromarray(array.astype('uint8'), img.mode)
            imagenEcriptada.save(imagenOculta)
            print("Mensaje ocultado de forma exitosa")
    """
        Método que se encarga de develar el mensaje de una imagen, funciona al revés que Oculta.
        Parámetros:
        imagen : La imagen que contiene un mensaje oculto

    """
    def Devela(self,imagen):
        img = Image.open(imagen, 'r')
        array = np.array(list(img.getdata()))
        if img.mode == 'RGB':
            n = 3
        elif img.mode == 'RGBA':
            n = 4
        totalPixeles = array.size//n
        bitsOcultos = ""
        for p in range(totalPixeles):
            for q in range(0, 3):
                bitsOcultos += (bin(array[p][q])[2:][-1])
        bitsOcultos = [bitsOcultos[i:i+8] for i in range(0, len(bitsOcultos), 8)]
        mensaje = ""
        for i in range(len(bitsOcultos)):
            if mensaje[-11:] == "$3ncripTAd0":
                print("Entre a $3ncripTAd0, sale el programa")
                break
            else:
                mensaje += chr(int(bitsOcultos[i], 2))
        if "$3ncripTAd0" in mensaje:
            print("El mensaje Oculto es:", mensaje[:-11])
        else:
            print("No se encontró un mensaje oculto")
        return mensaje[:-5]
    

    """
        Método principal de la clase, realiza preguntas al usuario sobre qué quiere ocupar
    """
    def ocultaDevela(self):
        print("Bienvenido. Ingresa la letra correspondiente a lo que quieres realizar")
        print("h: ocultar mensaje en una imagen")
        print("u: Descrifrar mensaje de una iamgen")
        func = input()
        if func == 'h':
            print("Introduce el nombre de la imagen con todo y formato (es decir, jpg, png, dependiendo de la imagen")
            imagen = input()
            print("Introduce el mensaje a ocultar ")
            mensaje = input()
            print("Introduce el nombre que quieres que tenga la imagen con la terminación .png")
            imagenOculta = input()
            print("Ocultando...")
            self.Oculta(imagen, mensaje, imagenOculta)

        elif func == 'u':
            print("Introduce el nombre de la imagen que se tiene que descrifrar con todo y formato (es decir, jpg, png, dependiendo de la imagen)")
            imagen = input()
            print("Develando...")
            self.Devela(imagen)

        else:
            print("Entrada inválida")