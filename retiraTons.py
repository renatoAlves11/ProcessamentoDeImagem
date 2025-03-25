# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 14:23:42 2025

@author: aluno
"""

from temp import histograma 
import cv2
import numpy
import matplotlib.pyplot as plt

def retiraPico(canalAntigo, imagem, inicio, fim):
    novoCanal = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)

    for x in range(0, imagem.shape[0]):
            for y in range(0, imagem.shape[1]):
                if canalAntigo[x][y] >= inicio and canalAntigo[x][y] <= fim:
                    novoCanal[x][y] = 255
                else:
                    novoCanal[x][y] = canalAntigo[x][y]
    return novoCanal
            
def deixaPico(canalAntigo, imagem, inicio, fim):
    novoCanal = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)

    for x in range(0, imagem.shape[0]):
            for y in range(0, imagem.shape[1]):
                if canalAntigo[x][y] <= inicio or canalAntigo[x][y] >= fim:
                    novoCanal[x][y] = 255
                else:
                    novoCanal[x][y] = canalAntigo[x][y]
    return novoCanal

def main():
    imagem = cv2.imread("testePBC.jpg")
    
    print('largura da imagem em pixels:', end = '')
    print(imagem.shape[1])
    
    print('Altura em pixels:')
    print(imagem.shape[0])
    
    print('Qtd de canais:', end = '')
    print(imagem.shape[2])
    
    canalCinza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
    
    # novoCanalBranco = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
    
    # novoCanalPreto = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
    
    # novoCanalCinza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
    
    for x in range(0, imagem.shape[0]):
            for y in range(0, imagem.shape[1]):
                canalCinza[x][y] = imagem[x][y].sum()//3
    #             if canalCinza[x][y] > 200:
    #                 novoCanalBranco[x][y] = canalCinza[x][y]
    #                 novoCanalPreto[x][y] = 255
    #             else:
    #                 novoCanalPreto[x][y] = canalCinza[x][y]
    #                 novoCanalBranco[x][y] = 255
                    
    
    # for x in range(0, imagem.shape[0]):
    #         for y in range(0, imagem.shape[1]):
    #             if canalCinza[x][y] < 50 or canalCinza[x][y] > 200:
    #                 novoCanalCinza[x][y] = 255
    #             else:
    #                 novoCanalCinza[x][y] = canalCinza[x][y]
                
    histograma(canalCinza)
    #histograma(novoCanalPreto)
    
    opcao = int(input("Digite 1 para retirar um pico ou 2 para só deixar um pico"))
    
    if opcao == 1:
        inicio = int(input("Digite inicio do pico:"))
        fim = int(input("Digite o fim do pico:"))
        novoCanal = retiraPico(canalCinza, imagem, inicio, fim)
    else: 
        if opcao == 2:
            inicio = int(input("Digite inicio do pico:"))
            fim = int(input("Digite o fim do pico:"))
            novoCanal = deixaPico(canalCinza, imagem, inicio, fim)
        else:
            print("Não tem essa opção")
            return
    
   # histograma(novoCanal)
    
    cv2.imshow("Palhaço", canalCinza)
    #cv2.imshow("Palhaço só branco", novoCanalBranco)
    #cv2.imshow("Palhaço só preto", novoCanalPreto)
    cv2.imshow("Mickey só cinza", novoCanal)
    
    cv2.waitKey(0)
    
main()