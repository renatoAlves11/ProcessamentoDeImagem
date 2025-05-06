import cv2
import numpy
import matplotlib.pyplot as plt
from temp import geraCanalCinza

def geraPretoEBranco(canalCinza):
    novoCanal = numpy.zeros((canalCinza.shape[0], canalCinza.shape[1]), dtype = numpy.uint8)
    for i in range(canalCinza.shape[0]):
        for j in range(canalCinza.shape[1]):
            if canalCinza[i][j] > 255/2:
                novoCanal[i][j] = 255
            else:
                novoCanal[i][j] = 0
    return novoCanal
    
def erosao(canal, filtro, fundo):
    extra = int((filtro.shape[0]-1)/2)
    canalNovo = numpy.pad(canal, extra, mode='constant', constant_values=0)
    canalFiltrado = numpy.zeros((canal.shape[0], canal.shape[1]), dtype = int)
    count = 0
    if fundo == 0: #FUNDO BRANCO
        for i in range(extra, canalNovo.shape[0] - extra):
            for j in range(extra, canalNovo.shape[1] - extra):
                matrizTemp = canalNovo[i-extra:i+extra+1, j-extra:j+extra+1]
                controle = True
                for x in range(filtro.shape[0]):
                    for y in range(filtro.shape[1]):
                        if filtro[x][y] == 0 and matrizTemp[x][y] != 0:
                            controle = False
                            break 
                    if not controle:
                        break
                canalFiltrado[i-extra][j-extra] = (0 if controle else 255)
    if fundo == 1: #FUNDO PRETO
        for i in range(extra, canalNovo.shape[0] - extra):
            for j in range(extra, canalNovo.shape[1] - extra):
                matrizTemp = canalNovo[i-extra:i+extra+1, j-extra:j+extra+1]
                controle = True
                for x in range(filtro.shape[0]):
                    for y in range(filtro.shape[1]):
                        if filtro[x][y] == 255 and matrizTemp[x][y] != 255:
                            controle = False
                            break 
                    if not controle:
                        break
                canalFiltrado[i-extra][j-extra] = (255 if controle else 0)
                
    return numpy.clip(canalFiltrado, 0, 255).astype(numpy.uint8)

imagem = cv2.imread("bolas.jpg")
filtroFundoBranco = numpy.array([[0,0,0],[0,0,0], [0,0,0]])
filtroFundoPreto = numpy.array([[255,255,255],[255,255,255], [255,255,255]])
canalCinza = geraCanalCinza(imagem)
canalPretoEBranco = geraPretoEBranco(canalCinza)
#canalErosao = erosao(canalPretoEBranco, filtroFundoPreto, 1)
canalErosao2 = erosao(canalPretoEBranco, filtroFundoBranco, 0)
for i in range(10):
    canalErosao2 = erosao(canalErosao2, filtroFundoBranco, 0)

cv2.imshow("Árvore preto e branco", canalPretoEBranco)
#cv2.imshow("Árvore com erosão", canalErosao)
cv2.imshow("Árvore com erosão2", canalErosao2)

cv2.waitKey(0)