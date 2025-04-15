
import cv2
import numpy
import matplotlib.pyplot as plt
from equalizaHist import mapeiaEqualizado, equalizaHist
from temp import histograma

def especificaHist(canal):
    final = mapeiaEqualizado(canal)
    normalizado = 256 * [0]
    mapeado = 256 * [0]
    acumulado = 256 * [0]
    especificado = [0] * 256
    qtd = 256 * [0]
    probabilidade = 256 * [0]
    
    for i in range(256):
        if i < 100:
            especificado[i] = i
        elif i < 200:
            especificado[i] = 100
        else:
            especificado[i] = 255 - i
            
    tamanho = canal.shape[0] * canal.shape[1]
    
    for x in range(0, canal.shape[0]):
            for y in range(0, canal.shape[1]):
                pixelValue = canal[x][y]
                qtd[pixelValue] += 1
            
    #Normaliza novo histograma
    for i in range(256):
        normalizado[i] = especificado[i]/255
        probabilidade[i] = qtd[i]/tamanho
        
    #calcula o acumulado
    for i in range(256):
        for j in range (0,i):
            acumulado[i] += probabilidade[j]
    
    plt.plot(normalizado)
    plt.show()
    
    for x in range(256):
            especificado[x] = round(acumulado[x] * 255)
            print(acumulado[x])
            print(especificado[x])
    
    canalEspecificado = numpy.zeros((canal.shape[0], canal.shape[1]), dtype = numpy.uint8)
    memo = 0
    for i in range(256):
        if final[i] != memo:
            
            
    histograma(canalEspecificado)
    return canalEspecificado


imagem = cv2.imread('arvore1.jfif')

canalCinza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)

for x in range(0, imagem.shape[0]):
        for y in range(0, imagem.shape[1]):
            canalCinza[x][y] = imagem[x][y].sum()//3
canalEspecificado = especificaHist(canalCinza)
arrayEqualizado = mapeiaEqualizado(canalCinza)
canalEqualizado = equalizaHist(canalCinza, arrayEqualizado)
histograma(canalEqualizado)
cv2.imshow("Imagem Equalizada", canalEqualizado)
cv2.imshow("Especificado", canalEspecificado)
cv2.waitKey(0)

    