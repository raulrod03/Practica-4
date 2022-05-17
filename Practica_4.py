import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

#Creas la imagen color negro
img = np.zeros((500,500,3),np.uint8)

#Caracteristicas del texto
texto = "Hola Mundo"
ubicacion = (50,200)
font = cv2.FONT_HERSHEY_TRIPLEX
tamañoLetra = 1
colorLetra = (255,255,255)
grosorLetra = 1

#Coloca el texto en la imagen----------------
cv2.putText(img, texto, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)
#Guarda la imagen--------------------
cv2.imwrite('textoQuito.jpg', img)
#Muestra la imagen--------------------
cv2.imshow('imagen negra',img)

#Arreglo de zeros, es la base de una imagen
img1 = np.zeros((500,500,3),np.uint8)

#colocar valores en píxeles especìficos de segmentacion
img1[150:160,150:300] = 255
img1[150:300,150:160] = 255
img1[300:310,150:300] = 255
img1[150:300,300:310] = 255

#Guardo la imagen
cv2.imwrite('Img-zeros.jpg', img1)

cv2.imshow('imagen segmentada',img1)


cv2.waitKey(0)
cv2.destroyAllWindows()
