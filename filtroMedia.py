import cv2
import numpy as np
from dilatacao import geraCanalCinza
from statistics import median, mode
from preencheRegiao import imgUniao

def suavizaImg(img):
    filtro = np.ones((25, 25), dtype=int) / (25 * 25)  # Filtro de média 25x25
    extra = int((filtro.shape[0]-1)/2) #espaço extra para padding
    canalNovo = np.pad(img, extra, mode='constant', constant_values=0) #canal com padding
    canalFiltrado = np.zeros((img.shape[0], img.shape[1]), dtype = int) #canalFinal
    tamImg = img.shape[0] * img.shape[1] #tamanho total da imagem
    
    for i in range(extra, canalNovo.shape[0] - extra):
        for j in range(extra, canalNovo.shape[1] - extra):
            matrizTemp = canalNovo[i-extra:i+extra+1, j-extra:j+extra+1] #separa submatriz do canal novo
            total = 0
            
            for x in range(filtro.shape[0]):
                for y in range(filtro.shape[1]):
                    total += filtro[x][y] * matrizTemp[x][y]
                    
            canalFiltrado[i-extra][j-extra] = total
            
    return canalFiltrado.astype(np.uint8)
            
def filtroMediana(img, tamFiltro):
    extra = tamFiltro//2 #espaço extra para padding
    canalNovo = np.pad(img, extra, mode='constant', constant_values=0) #canal com padding
    canalFiltrado = np.zeros((img.shape[0], img.shape[1]), dtype = int) #canalFinal
    
    for i in range(extra, canalNovo.shape[0] - extra):
        for j in range(extra, canalNovo.shape[1] - extra):
            matrizTemp = canalNovo[i-extra:i+extra+1, j-extra:j+extra+1] #separa submatriz do canal novo
            temp = []
            
            for x in range(matrizTemp.shape[0]):
                for y in range(matrizTemp.shape[1]):
                    temp.append(matrizTemp[x][y])
            
            temp.sort()
                
            # tempOrdenado = np.sort(temp)
            
            canalFiltrado[i-extra][j-extra] = median(temp)
            
    return canalFiltrado.astype(np.uint8)
    
def filtroModa(img, tamFiltro):
        extra = tamFiltro//2 #espaço extra para padding
        canalNovo = np.pad(img, extra, mode='constant', constant_values=0) #canal com padding
        canalFiltrado = np.zeros((img.shape[0], img.shape[1]), dtype = int) #canalFinal
        
        for i in range(extra, canalNovo.shape[0] - extra):
            for j in range(extra, canalNovo.shape[1] - extra):
                matrizTemp = canalNovo[i-extra:i+extra+1, j-extra:j+extra+1] #separa submatriz do canal novo
                temp = []
                
                for x in range(matrizTemp.shape[0]):
                    for y in range(matrizTemp.shape[1]):
                        temp.append(matrizTemp[x][y])
                
                temp.sort()
                    
                # tempOrdenado = np.sort(temp)
                
                canalFiltrado[i-extra][j-extra] = mode(temp)
                
        return canalFiltrado.astype(np.uint8)    

def convolucao(canal, filtro):
    extra = int((filtro.shape[0]-1)/2)
    matrizTemp = np.zeros((canal.shape[0], canal.shape[1]), dtype = np.uint8)
    canalNovo = np.pad(canal, extra, mode='constant', constant_values=0)
    canalFiltrado = np.zeros((canal.shape[0], canal.shape[1]), dtype = int)
    count = 0
    
    for i in range(extra, canalNovo.shape[0] - extra):
        for j in range(extra, canalNovo.shape[1] - extra):
            matrizTemp = canalNovo[i-extra:i+extra+1, j-extra:j+extra+1]
            total = 0
            for x in range(filtro.shape[0]):
                for y in range(filtro.shape[1]):
                    total = total + (filtro[x][y] * matrizTemp[x][y])
            canalFiltrado[i-extra][j-extra] = total
            
    return np.clip(canalFiltrado, 0, 255).astype(np.uint8)

def filtroSobel(img, filtro1, filtro2):
    canalNovo = np.zeros((img.shape[0], img.shape[1]), dtype = np.uint8)
    
    canalFiltrado1 = convolucao(img, filtro1)
    canalFiltrado2 = convolucao(img, filtro2)
            
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if int(canalFiltrado1[i][j]) + int(canalFiltrado2[i][j]) <= 255:
                canalNovo[i][j] = canalFiltrado1[i][j] + canalFiltrado2[i][j]
            else: canalNovo[i][j] = 255
    
    return canalNovo
    

img = cv2.imread("saltPepper.png")
imgCinza = geraCanalCinza(img)
#imgSuavizada = suavizaImg(imgCinza)
imgMediana = filtroMediana(imgCinza, 9)
imgModa = filtroModa(imgCinza, 9)

filtro1 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
filtro2 = np.array([[-1,0,1], [-2,0,2], [1,2,-1]])
imgSobel = filtroSobel(imgMediana, filtro1, filtro2)

#cv2.imshow("Imagem original", img)
#cv2.imshow("Imagem cinza", imgCinza)
cv2.imshow("Imagem suavizada", imgMediana)
#cv2.imshow("Imagem moda", imgModa)
cv2.imshow("Imagem sobel", imgSobel)

cv2.waitKey(0)

