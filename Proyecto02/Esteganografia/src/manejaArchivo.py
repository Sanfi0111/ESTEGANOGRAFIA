import numpy as np
from PIL import Image 
import sys, os
sys.path.insert(0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class manejaArchivo:
    
    """
        Lee un archivo .txt y regresa la cadena que tiene adentro.
        Parámetros:
        nombreArchivo : El nombre del archivo que se leerá
    """
    def leeArhivo(self, nombreArchivo):
        f =  open(nombreArchivo, "r")
        mensaje = f.read()
        return mensaje
    """
        Dada una cadena mensaje, se crea un archivo nombreArchivo.txt con la cadena en él
        Parámetros:
        nombreArchivo: El nombre que tendrá el archivo que se crea
        mensaje: El mensaje que tendrá el archivo
    """
    def escribeArchivo(self, nombreArchivo, mensaje):
        file = open(nombreArchivo, "w")
        file.write(mensaje)
        file.close()
