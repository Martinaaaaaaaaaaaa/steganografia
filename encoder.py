from PIL import Image

immagine = Image.open("immagine.png")
#immagine = input("Inserire la path")
immagine = immagine.convert('RGB')
pixels = immagine.load()

messaggio = "Let's try a longer message because I can't see shit"
#messaggio = input("inserire il messaggio da inserire nell'immagine: ")

#come funzia: ord piglia l'ASCII di ogni carattere, format lo converte in numero a 8 bit, join congiunge in una stringa
messaggio_bin = ''.join(format(ord(char), '08b') for char in messaggio)+"00000000"

#controllo se l'immagine è grande abbastanza
messaggio_len = len(messaggio_bin)
largh, alt = immagine.size

if messaggio_len > (largh*alt):
    raise ValueError("L'immagine è troppo piccola o il messaggio è troppo lungo")

#tentiamo di fare encoding
try:
    puntatore = 0
    for y in range(alt): #scorrimento righe
        for x in range(largh): #scorrimento colonne
            if puntatore < messaggio_len: 
                r, g, b = pixels[x, y] 
                colors = [r, g, b] #valori rgb del pixel in questione
                
                for i in range(3): #andiamo a modificare tutti e 3 i valori rgb del pixel
                        binary = format(colors[i], '08b') #conversione in binario del valore colore
                        binary = binary[:-1] + messaggio_bin[puntatore] #cambiamo ultimo bit con il nostro super segreto bit del messaggio super ultra segreto
                        colors[i] = int(binary, 2) #riconversione in decimale
                        puntatore += 1
                
                pixels[x, y] = tuple(colors)
except ValueError as e:
    print(e)

#salvataggio nuova immagine
path_salvataggio = "immagine_con_codifica.png"
immagine.save(path_salvataggio)
print(f"Messaggio codificato e salvato a {path_salvataggio}")

#testsssss
'''print(messaggio_bin)
print(immagine.format, immagine.size, immagine.mode)
immagine.show()
immagine_con_cod = Image.open("immagine_con_codifica.png")
immagine_con_cod.show()'''