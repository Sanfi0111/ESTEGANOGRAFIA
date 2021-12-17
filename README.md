# ESTEGANOGRAFIA
Este programa en python oculta mensajes en imágenes y devela los mismos usando el método de esteganografía LSB,
Este código te permite ocultar o develar un mensaje en una imagen, usando el método LSB de esteganografía.
Este método como funciona es que toma el bit menos significativo de cada pixel de una imagen, dependiendo de su formato (JPG,PNG,JPGN) sus 
pixeles tienen forma RGB ó RGBA, donde RBG significa los parámetros de color Red, Green y Blue, y a A se refiere a Alpha, un parámetro de transparencia.
Lo que hace este método, es cambiar el último bit con con un número. Se cambiará el bit menos significativo de cada pixel con el valor del mensaje en binario, por lo tanto para develar un mensaje en una imagen sólo basta con traducir los últimos bits de cada pixel de binario a ASCII

Linux : python3 main.py

Windows- Entrar a powershell y ejecutar: python3.\main.py

