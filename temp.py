import cv2
import numpy
import matplotlib.pyplot as plt

imagem = cv2.imread('leao.jfif')

print('largura da imagem em pixels:', end = '')
print(imagem.shape[1])

print('Altura em pixels:')
print(imagem.shape[0])

print('Qtd de canais:', end = '')
print(imagem.shape[2])

canalBlue = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype = numpy.uint8)
canalGreen = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype = numpy.uint8)
canalRed = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype = numpy.uint8)
canalCinza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)

canalBlue[:,:,0] = imagem[:,:,0]
canalGreen[:,:,1] = imagem[:,:,1]
canalRed[:,:,2] = imagem[:,:,2]

for x in range(0, imagem.shape[0]):
        for y in range(0, imagem.shape[1]):
            canalCinza[x][y] = imagem[x][y].sum()//3

#cv2.imshow("Pikachu", imagem)
# cv2.imshow("canal Blue", canalBlue)
# cv2.imshow("canal Green", canalGreen)
# cv2.imshow("canal Red", canalRed)
cv2.imshow("canal Cinza", canalCinza)

cv2.waitKey(0)

#plotando histograma da imagem cinza

#criando o eixo x
pixel = 256 * [0]
qtd = 256 * [0]

for i in range(256):
    pixel[i] = i
    
for x in range(0, imagem.shape[0]):
        for y in range(0, imagem.shape[1]):
            qtd[canalCinza[x][y]] = qtd[canalCinza[x][y]] + 1; 
    
    
plt.xlabel('Pixel')

plt.ylabel('Quantidade')

plt.title('Histograma')

plt.bar(pixel, qtd, color = 'blue')
plt.show()