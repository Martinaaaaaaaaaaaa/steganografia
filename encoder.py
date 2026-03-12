from PIL import Image

immagine = Image.open("immagine.png")
grandezza_im = immagine.size[0]*immagine.size[1]

messaggio = "Cagiva"
#messaggio = input("inserire il messaggio da inserire: ")

#ord piglia l'ASCII di ogni carattere, format lo converte in numero a 8 bit, join congiunge in una stringa
messaggio_bit = ''.join(format(ord(char), '08b') for char in messaggio)+"00000000"

#controlllo se l'immagine è grande abbastanza
if len(messaggio_bit) > grandezza_im:
    raise ValueError("L'immagine è troppo piccola o il messaggio è troppo lungo")

try:
    pass
except ValueError as e:
    pass

#testsssss
print(messaggio_bit)
'''print(immagine.format, immagine.size, immagine.mode)
immagine.show()'''