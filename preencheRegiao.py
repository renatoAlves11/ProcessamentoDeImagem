import cv2
import numpy as np
from dilatacao import dilatacao
from erosao import geraPretoEBranco, geraCanalCinza
from extraiFronteiras import extraiFronteiras

def geraComplemento(canal):
    canalComplemento = np.zeros((canal.shape[0],canal.shape[1]), dtype = np.uint8)
    for i in range(canal.shape[0]):
        for j in range(canal.shape[1]):
            if canal[i][j] == 0:
                canalComplemento[i][j] = 255
            else: canalComplemento[i][j] = 0
    return canalComplemento

def imgIntersecao(canalA, canalB):
    
    novoCanal = np.zeros((canalA.shape[0], canalA.shape[1]), dtype = np.uint8)
    
    for i in range(canalA.shape[0]):
        for j in range(canalB.shape[1]):
            if canalA[i][j] == 0 and canalB[i][j] == 0:
                novoCanal[i][j] = 0
            else: novoCanal[i][j] = 255
            
    return novoCanal

def imgUniao(canalA, canalB):
    canalNovo = np.zeros((canalA.shape[0], canalB.shape[1]), dtype = np.uint8)
    
    for i in range(canalA.shape[0]):
        for j in range(canalB.shape[1]):
            if canalA[i][j] == 0 or canalB[i][j] == 0:
                canalNovo[i][j] = 0
            else: 
                canalNovo[i][j] = 255
    
    return canalNovo
    
def geraCanalPonto(canal):
    novoCanal = np.zeros((canal.shape[0], canal.shape[1]), dtype = np.uint8)
    found = False
    
    for i in range(canal.shape[0]):
        for j in range(canal.shape[1]):
            if canal[i][j] == 0:
                novoCanal[i][j] = 255
                found = True
                break
        if found == True:
            break
            
    return geraComplemento(novoCanal)

def preencheReg(canal):
    
    mask = np.array([[255,0,255],[0,0,0],[255,0,255]], dtype = np.uint8)
    
    canalComplemento = geraComplemento(canal)
    
    canalPonto = geraCanalPonto(canal)
    canalDilatado = dilatacao(canalPonto, mask)
    
    anterior = imgIntersecao(canalComplemento, canalDilatado)
    
    canalDilatado = dilatacao(canalDilatado, mask)
    atual = imgIntersecao(canalComplemento, canalDilatado)
    
    while not np.array_equal(anterior, atual):
        canalDilatado = dilatacao(canalDilatado, mask)
        anterior = atual
        atual = imgIntersecao(canalComplemento, canalDilatado)
    
    # cv2.imshow("Interseção", canalIntersection1)
    # cv2.imshow("Complemento", canalComplemento)
    
    return imgUniao(atual, extraiFronteiras(canal, mask))

img = cv2.imread("teste6.png")
canalC = geraCanalCinza(img)
canalPB = geraPretoEBranco(canalC)
canalPreenchido = preencheReg(canalPB)

cv2.imshow("canalIntesection", canalPreenchido)
cv2.imshow("canalOrigem", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
    
                  
    
    
    
    