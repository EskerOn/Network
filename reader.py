import functools
f = open('DocumentoCodigoError.txt', "r")
print("Leyendo de DocumentoCodigoError.txt")
tramas=f.readlines()
def checksum256(st):
    return functools.reduce(lambda x,y:x+y, map(ord, st)) % 256
buffer=""
for trama in tramas:
    mensaje= trama[5:len(trama)-5]
    chars=mensaje.split()
    ErrCode= int(trama[len(trama)-4:])
    temp=trama[:len(trama)-4]
    if ErrCode==checksum256(temp):
        print("Trama: {} Correcto".format(trama[1:4]))
    else:
        print("Trama: {} Incorrecto".format(trama[1:4]))
    leido=''.join(chr(int(i)) for i in chars)
    buffer+=leido
    print(leido)

e = open('DocumentoLeido.txt', "w")
e.write("*****informacion leida de: DocumentoCodigoError.txt*****\n\n")
e.write(buffer)
e.close()
