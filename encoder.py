from PIL import Image

immagine = Image.open("immagine.png")
#immagine = input("Inserire la path")
immagine = immagine.convert('RGB')
pixels = immagine.load()

messaggio = "Cagiva"
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
    finito = False
    
    while not finito:
        for y in range(alt):
            for x in range(largh):
                if puntatore < messaggio_len:
                    r, g, b = pixels[x, y]
                    r_bin = format(r, '08b')  # Convert red component to binary
                    r_bin = r_bin[:-1] + messaggio_bin[puntatore]  # Replace the LSB with the message bit
                    r = int(r_bin, 2)
                    pixels[x, y] = (r, g, b)
                    puntatore += 1
                else: #fine loop
                    finito = True        
except ValueError as e:
    print(e)

#salvataggio nuova immagine
path_salvataggio = "immagine_con_codifica.png"
immagine.save(path_salvataggio)
print(f"Messaggio codificato e salvato a {path_salvataggio}")

#testsssss
'''print(messaggio_bit)
print(immagine.format, immagine.size, immagine.mode)'''
immagine.show()
immagine_con_cod = Image.open("immagine_con_codifica.png")