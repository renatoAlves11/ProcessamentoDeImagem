from temp import histograma
import numpy
import matplotlib.pyplot as plt
import cv2


            
def alteraHist(canalCinza, c, l):
    canalNovo = numpy.zeros((canalCinza.shape[0], canalCinza.shape[1]), numpy.uint8)
    
    for x in range(0, canalCinza.shape[0]):
        for y in range(0, canalCinza.shape[1]):
            val = (int(canalCinza[x][y]) * c + l)
            if val > 255:
                canalNovo[x][y] = 255
            elif val < 0:
                canalNovo[x][y] = 0
            else:
                canalNovo[x][y] = val
        
    return canalNovo

def parabolicoHist(canalCinza):
    canalNovo = numpy.zeros((canalCinza.shape[0], canalCinza.shape[1]), numpy.uint8)
    for x in range(0, canalCinza.shape[0]):
        for y in range(0, canalCinza.shape[1]):
            val = ((int(canalCinza[x][y]) * 1/256)**2)*256
            if val > 255:
                canalNovo[x][y] = 255
            elif val < 0:
                canalNovo[x][y] = 0
            else:
                canalNovo[x][y] = val
        
    return canalNovo

def expandeHist(canalCinza, r1, r2):
    canalNovo = numpy.zeros((canalCinza.shape[0], canalCinza.shape[1]), numpy.uint8)
    for x in range(0, canalCinza.shape[0]):
        for y in range(0, canalCinza.shape[1]):
            if canalCinza[x][y] >= r2:
                canalNovo[x][y] = 255
            elif canalCinza[x][y] <= r1:
                canalNovo[x][y] = 0
            else:
                canalNovo[x][y] = 255*((canalCinza[x][y]-r1)/(r2-r1))
    return canalNovo
            
def main():
    imagem = cv2.imread("arvore1.jfif")
    
    canalCinza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
    for x in range(0, imagem.shape[0]):
            for y in range(0, imagem.shape[1]):
                canalCinza[x][y] = imagem[x][y].sum()//3
    
    # f(r) = 2r
    
    canalNovo1 = alteraHist(canalCinza, 2, 0)
    histograma(canalNovo1)
    cv2.imshow("Mickey alterado 1", canalNovo1)
    
    # f(r) = r + 100
    
    canalNovo2 = alteraHist(canalCinza, 1, 100)
    histograma(canalNovo2)
    cv2.imshow("Mickey alterado 2", canalNovo2)
    
    # f(r) = -r + 255
    
    canalNovo3 = alteraHist(canalCinza, -1, 255)
    histograma(canalNovo3)
    cv2.imshow("Mickey alterado 3", canalNovo3)
    
    # f(r) = ((1/256)*r)**2
    
    canalNovo4 = parabolicoHist(canalCinza)
    histograma(canalNovo4)
    cv2.imshow("Mickey alterado 4", canalNovo4)
    
    # Expande histograma
    
    canalNovo5 = expandeHist(canalCinza, 50, 220)
    histograma(canalNovo5)
    cv2.imshow("Mickey alterado 5", canalNovo5)
    
    histograma(canalCinza)
    cv2.imshow("Minions origem", canalCinza)
    cv2.waitKey(0)
        
main()

