import numpy as np
from PIL import Image 
import sys, os
sys.path.insert(0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import esteganografia
"""
Método main para correr el programa
"""

def main():
    ocultadorDevelador =  esteganografia.Esteganografia()
    ocultadorDevelador.ocultaDevela()
    
if __name__ == "__main__":
    main()


