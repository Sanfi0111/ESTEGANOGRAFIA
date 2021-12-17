import numpy as np
from PIL import Image 
import sys,os
sys.path.insert(0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import manejaArchivo

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
        return mensaje[:-11]
    

    """
        Método principal de la clase, realiza preguntas al usuario sobre qué quiere ocupar
    """
    def ocultaDevela(self):
        manejador = manejaArchivo.manejaArchivo()
        print("Bienvenido. Ingresa la letra correspondiente a lo que quieres realizar")
        print("Puedes probar con las imagenes que ya vienen incluidas, es decir, para develar puedes ocupar el archivo 'mensaje.txt' y la imagen 'macacos.jpg'.")
        print("Para develar puedes ocupar la imagen 'macacoEncrip.png'")
        print("h: ocultar mensaje en una imagen")
        print("u: Descrifrar mensaje de una iamgen")
        func = input()
        if func == 'h':
            print("Introduce el nombre del archivo (con extensión .txt) donde se encuentra el mensaje a ocultar")
            archivo = input()
            mensaje = manejador.leeArhivo(archivo)
            print("Introduce el nombre de la imagen con todo y formato (es decir, jpg, png, dependiendo de la imagen")
            imagen = input()
            print("Introduce el nombre que quieres que tenga la imagen con la terminación .png")
            imagenOculta = input()
            print("Ocultando...")
            self.Oculta(imagen, mensaje, imagenOculta)
            print("La imagen con el mensaje oculto se encuentra en esta carpeta con el nombre ",imagenOculta)

        elif func == 'u':
            print("Introduce el nombre de la imagen que se tiene que descrifrar con todo y formato (es decir, jpg, png, dependiendo de la imagen)")
            imagen = input()
            print("Introduce el nombre que quieras que tenga el archivo .txt donde se escribirá el mensaje develado")
            archivo = input()
            print("Develando...")
            mensaje = self.Devela(imagen)
            manejador.escribeArchivo(archivo,mensaje)
            print("Archivo generado de manera exitosa. Revisa el archivo ",archivo," , ahí se encuentra el mensaje develado")


        else:
            print("Entrada inválida")