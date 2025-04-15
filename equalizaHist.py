# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 14:53:01 2025

@author: Renato
"""

import cv2
import numpy
import matplotlib.pyplot as plt

def mapeiaEqualizado(canal):
    qtd = 256 * [0]
    normalizados = 256 * [0]
    probabilidade = 256 * [0]
    acumulado = 256 * [0]
    final = 256 * [0]
    
    tamanho = canal.shape[0] * canal.shape[1]
    
    for x in range(0, canal.shape[0]):
            for y in range(0, canal.shape[1]):
                pixelValue = canal[x][y]
                qtd[pixelValue] += 1
                
    #Calculando valores de cada tom normalizado em normalizados
    #Calculando valores de distribuição de probabilidade em probabilidades
    for i in range(256):
        normalizados[i] = i/256
        probabilidade[i] = qtd[i]/tamanho
        
    #Calculando somatório do histograma acumulado normalizado da função de distribuição
    for i in range(256):
        for j in range (0,i):
            acumulado[i] += probabilidade[j]
            
    for x in range(256):
            final[x] = round(acumulado[x] * 255)
            print(acumulado[x])
            print(final[x])
    
    #plt.plot(acumulado)
    #plt.show()
    return final

def equalizaHist(canal, final):
    
    canalEqualizado = numpy.zeros((canal.shape[0], canal.shape[1]), dtype = numpy.uint8)
    for i in range(0, canal.shape[0]):
        for j in range(0, canal.shape[1]):
            canalEqualizado[i][j] = final[canal[i][j]] 
            
    return canalEqualizado
            
    
def histograma(canal):
    pixel = 256 * [0]
    qtd = 256 * [0]
    normalizados = 256 * [0]
    probabilidades = 256 * [0]
    acumulado = 256 * [0]

    tamanho = canal.shape[0] * canal.shape[1]
    for i in range(256):
        pixel[i] = i
        
    for x in range(0, canal.shape[0]):
            for y in range(0, canal.shape[1]):
                pixelValue = canal[x][y]
                qtd[pixelValue] += 1
    plt.xlabel('Pixel')

    plt.ylabel('Quantidade')

    plt.title('Histograma')

    plt.bar(pixel, qtd, color = 'blue')
    plt.show()
                
def main():
    imagem = cv2.imread('arvore1.jfif')
    canalCinza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)
    
    for x in range(0, imagem.shape[0]):
            for y in range(0, imagem.shape[1]):
                canalCinza[x][y] = imagem[x][y].sum()//3
            
    histograma(canalCinza)
    arrayEqualizado = mapeiaEqualizado(canalCinza)
    canalEqualizado = equalizaHist(canalCinza, arrayEqualizado)
    histograma(canalEqualizado)
    cv2.imshow("Imagem", canalCinza)
    cv2.imshow("Imagem Equalizada", canalEqualizado)
    cv2.waitKey(0)
    


