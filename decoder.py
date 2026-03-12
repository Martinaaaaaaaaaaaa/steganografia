from PIL import Image

immagine = Image.open("immagine_con_codifica.png")
immagine = immagine.convert('RGB')
pixels = immagine.load()

largh, alt = immagine.size
messaggio_bin = ""

#estrazione dei bit nascosti
for y in range(alt):
    for x in range(largh):
        r, g, b = pixels[x, y]
        colors = [r, g, b]
        
        for i in range(3):
            binary = format(colors[i], '08b')
            messaggio_bin += binary[-1]  #prendiamo l'ultimo bit (LSB)

#conversione da binario a testo
messaggio = ""
for i in range(0, len(messaggio_bin), 8):
    byte = messaggio_bin[i:i+8]
    if byte == "00000000":  #stop marker
        break
    messaggio += chr(int(byte, 2))

print(f"Messaggio estratto: {messaggio}")
