import cv2
import numpy as np
import matplotlib.pyplot as plt
from erosao import geraPretoEBranco


def geraCanalCinza(imagem):
    canalCinza = np.zeros((imagem.shape[0], imagem.shape[1]), dtype = np.uint8)
    for x in range(0, imagem.shape[0]):
        for y in range(0, imagem.shape[1]):
            canalCinza[x][y] = imagem[x][y].sum()//3
    return canalCinza;

def dilatacao(canal, filtro):
    # Tamanho do filtro
    extra = filtro.shape[0] // 2  # Assume filtro quadrado e de tamanho ímpar
    canalPad = np.pad(canal, extra, mode='constant', constant_values=255)  # Preenchendo com fundo branco (255)
    canalFiltrado = np.zeros_like(canal, dtype=np.uint8)  # Inicializa a imagem dilatada com fundo preto (0)

    altura, largura = canal.shape

    # Aplica o filtro em cada pixel
    for i in range(altura):  # i: 0 até altura-1
        for j in range(largura):  # j: 0 até largura-1
            # Aplica o filtro centralizado em (i,j)
            roi = canalPad[i:i + filtro.shape[0], j:j + filtro.shape[1]]

            # Verifica se existe sobreposição entre filtro e a região da imagem
            for x in range(filtro.shape[0]):
                for y in range(filtro.shape[1]):
                    if roi[x][y] == 0 and filtro[x][y] == 0:
                        canalFiltrado[i][j] = 0
                        continue

    return canalFiltrado

# imagem = cv2.imread("teste.jpg")
# if imagem is None:
#     print("Erro ao carregar a imagem. Verifique o caminho do arquivo.")
#     exit()  # Sai do programa, caso a imagem não seja carregada

# filtroFundoBranco = np.array([[0,0,0],[0,0,0], [0,0,0]])
# filtroFundoPreto = np.array([[255,255,255],[255,255,255], [255,255,255]])
# canalCinza = geraCanalCinza(imagem)
# canalPretoEBranco = geraPretoEBranco(canalCinza)
# canalErosao2 = dilatacao(canalPretoEBranco, filtroFundoBranco)
# #for i in range(10):
#  #   canalErosao2 = erosao(canalErosao2, filtroFundoBranco, 0)

# cv2.imshow("Árvore preto e branco", canalPretoEBranco)
# #cv2.imshow("Árvore com erosão", canalErosao)
# cv2.imshow("Árvore com dilatação", canalErosao2)

# cv2.waitKey(0)