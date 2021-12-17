import numpy as np
from PIL import Image 
import sys, os
sys.path.insert(0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class manejaArchivo:
    
    def leeArhivo(self, nombreArchivo):
        f =  open(nombreArchivo, "r")
        mensaje = f.read()
        return mensaje
        
    def escribeArchivo(self, nombreArchivo, mensaje):
        file = open(nombreArchivo, "w")
        file.write(mensaje)
        file.close()
