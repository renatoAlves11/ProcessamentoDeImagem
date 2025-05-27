from erosao import erosao, geraPretoEBranco
from dilatacao import dilatacao, geraCanalCinza
import cv2
import numpy as np

def hitOrMiss(patternB1, canal):
    patternB2 = np.where(patternB1 == 0, 255, 0).astype(np.uint8)
    patternB2 = np.pad(patternB2, 1, mode='constant', constant_values = 0)
    erosao1 = erosao(canal, patternB1, 0)
    cv2.imshow("imagem com erosão", erosao1)
    heightCanal = canal.shape[0]
    widthCanal = canal.shape[1]
    canalComplemento = np.zeros((heightCanal, widthCanal), dtype = np.uint8)
    canalFinal = np.zeros((heightCanal, widthCanal), dtype = np.uint8)
    for i in range(heightCanal):
        for j in range(widthCanal):
            if canal[i][j] == 255:
                canalComplemento[i][j] = 0
            else:
                canalComplemento[i][j] = 255
    print(patternB1)
    print(patternB2)
    erosao2 = erosao(canalComplemento, patternB2, 0)
    cv2.imshow("imagem 2 com erosão", erosao2)
    for i in range(heightCanal):
        for j in range(widthCanal):
            if erosao1[i][j] == 0 and erosao2[i][j] == 0:
                canalFinal[i][j] = 0
            else:
                canalFinal[i][j] = 255
    return canalFinal

imagem = cv2.imread("teste5.png")
filtroFundoBranco = np.zeros((25, 25), dtype=np.uint8)
filtroFundoPreto = np.array([[255,255,255],[255,255,255], [255,255,255]])
canalCinza = geraCanalCinza(imagem)
canalPretoEBranco = geraPretoEBranco(canalCinza)
canalHitMiss = hitOrMiss(filtroFundoBranco, canalPretoEBranco)


cv2.imshow("Árvore preto e branco", canalPretoEBranco)
cv2.imshow("Árvore com hit e miss", canalHitMiss)
dilatado = dilatacao(canalHitMiss, filtroFundoBranco)
cv2.imshow("Árvore dilatada", canalHitMiss)


# Salvar a imagem
cv2.imwrite("imgHitMiss.png", canalHitMiss)

cv2.waitKey(0)
cv2.destroyAllWindows()
    