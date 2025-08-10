from random import *

lista=["pollos","ivan","carro","vaca","pan"]
indice=randint(0,len(lista)-1)
pal=lista[indice]

indice2=len(pal)

primPal=pal[0]
ultiPal=pal[indice2-1]
sub=(len(pal)-2)*" _ "
print("pista: ",primPal,sub,ultiPal)

respuesta=input("digite la palabre que cree que es: ")

cond=respuesta==pal

print("la respuesta es correcta? ",cond)