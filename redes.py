import functools 
f = open('Documento.txt', "r")
aux = f.read()
f.close()

rest=len(aux)%100
#while rest>0:
	#aux=aux+" "
	#rest=len(aux)%100
pieces = len(aux)//100

i = 0
buffera = ""
bufferb = ""
def checksum256(st):
    return reduce(lambda x,y:x+y, map(ord, st)) % 256
while(i < pieces):
	h = hex(i+1)
	buffera += chr(1)+h+chr(2)+"{}".format(aux[i*100:(i+1)*100])+chr(3)+"FF"+"\n"
	print("formato de trama")
	print(buffera)
	ascii_char=[ord(c) for c in aux[i*100:(i+1)*100]]
	print("en ascii")
	stringas = ""
	for trama in ascii_char:
		stringas+=str(trama)
	bufferb+= "1"+str((int(h, 16)))+"2"+"{}".format(stringas)+"3"+str(int("0xFF", 16))+"\n"
	print(bufferb)
	print("\n")
	i += 1
if rest>0:
	h = hex(i+1)
	buffera += chr(1)+h+chr(2)+"{}".format(aux[len(aux)-rest:])+chr(3)+"FF"+"\n"
	print("formato de trama")
	print(buffera)
	ascii_char=[ord(c) for c in aux[len(aux)-rest:]]
	print("en ascii")
	stringas = ""
	for trama in ascii_char:
		stringas+=str(trama)
	bufferb+= "1"+str(int(h, 16))+"2"+"{}".format(stringas)+"3"+str(int("0xFF", 16))+"\n"
	print(bufferb)
	print("\n")

	
f = open('DocumentoFormat.txt', "w")
e = open('DocumentoFormatASCII.txt', "w")
f.write(buffera)
e.write(bufferb)

e.close()
f.close()