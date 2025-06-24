import cv2
import numpy
import matplotlib.pyplot as plt
from temp import geraCanalCinza 
from filtroMedia import suavizaImg


#Filtro  Laplaciano:
# 0   1  0;
# 1  -4  1;
# 0   1  0;

def convolucao(canal, filtro):
    extra = int((filtro.shape[0]-1)/2)
    matrizTemp = numpy.zeros((canal.shape[0], canal.shape[1]), dtype = numpy.uint8)
    canalNovo = numpy.pad(canal, extra, mode='constant', constant_values=0)
    canalFiltrado = numpy.zeros((canal.shape[0], canal.shape[1]), dtype = int)
    count = 0
    
    for i in range(extra, canalNovo.shape[0] - extra):
        for j in range(extra, canalNovo.shape[1] - extra):
            matrizTemp = canalNovo[i-extra:i+extra+1, j-extra:j+extra+1]
            total = 0
            for x in range(filtro.shape[0]):
                for y in range(filtro.shape[1]):
                    total = total + (filtro[x][y] * matrizTemp[x][y])
            canalFiltrado[i-extra][j-extra] = total
            
    return numpy.clip(canalFiltrado, 0, 255).astype(numpy.uint8)

def somaImgs (img1, img2, fatorK):
    novoCanal = numpy.zeros((img1.shape[0], img1.shape[1]), dtype = numpy.uint8)
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            if (int(img1[i][j]) + fatorK * int(img2[i][j])) > 255:
                novoCanal[i][j] = 255
            else:
                novoCanal[i][j] = img1[i][j] + img2[i][j] 
    return novoCanal

def subtraiImgs (img1, img2):
    novoCanal = numpy.zeros((img1.shape[0], img1.shape[1]), dtype = numpy.uint8)
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            if int(img1[i][j]) - int(img2[i][j]) < 0:
                novoCanal[i][j] = 0
            else:
                novoCanal[i][j] = img1[i][j] - img2[i][j] 
    return novoCanal            

def  filtroAltoReforço(img, fatorK):
    canalSubtrai = suavizaImg(img, 5)
    canalMascara = subtraiImgs(img, canalSubtrai)
    novoCanal = somaImgs(img, canalMascara, fatorK)
    return novoCanal

imagem = cv2.imread("arvore1.jfif")
                
canalCinza = geraCanalCinza(imagem)

canalAltoReforco = filtroAltoReforço(canalCinza, 3)

# filtro = numpy.array([[1,1,1],[1,-8, 1], [1, 1, 1]])

# filtro1 = numpy.array([[-2,-1,0],[-1,1, 1], [0, 1, 2]])

# canalFiltrado = convolucao(canalCinza, filtro)
# canalFiltrado1 = convolucao(canalCinza, filtro1)

cv2.imshow("Original", canalCinza)
cv2.imshow("Alto reforço", canalAltoReforco)
            
cv2.waitKey(0)

