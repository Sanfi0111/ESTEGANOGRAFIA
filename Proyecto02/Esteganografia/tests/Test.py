import numpy as np
from PIL import Image 
import unittest
import sys, os
sys.path.insert(0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import esteganografia

class Test (unittest.TestCase):

    """
        Test que revisa que Devela() funcione de forma adecuada.
    """
    def test_Devela(self):
        ocultador = esteganografia.Esteganografia()
        ocultador.Oculta("macacos.jpg","SOYUNMACACOMIRAME","macacoEncriptado.png")
        mensajeDevelado = ocultador.Devela("macacoEncriptado.png")
        print("Mensaje es ", mensajeDevelado)
        self.assertEqual("SOYUNMACACOMIRAME",mensajeDevelado)
        """
        Test que revisa que oculta() funcione de forma adecuada.
    """
    def test_Oculta(self):
        ocultador = esteganografia.Esteganografia()
        macacoConfiable ="SOYUNMACACOMIRAME"
        ocultador.Oculta("macacos.jpg",macacoConfiable,"macacoEncriptado.png")
        mensajeDevelado = ocultador.Devela("macacoEncriptado.png")
        self.assertEqual(macacoConfiable,mensajeDevelado)
if __name__ == "__main__":
    unittest.main()