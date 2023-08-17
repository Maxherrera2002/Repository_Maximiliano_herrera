 #Eje1
numero1=4

#ejer2 
numero2=2.4

#ejer3 
suma=numero1+numero2

#ejer4
resta=numero1-numero2
mul=numero1*numero2
div=numero1/numero2

#ejer5
nombre="Maximiliano"

#ejer6
precio=23.50

#ejer7
descuento=0.33

#ejer8
precio_final=precio-(precio*descuento)

#ejer9
cadena="hola mundo"

#ejer10
longitud=len(cadena)

#ejer11
precio2=5.25
precio2=int(precio2)

#ejer12
nombre2="Maximiliano"
apelido="Herrera"
nombreapellido=nombre2+" "+apelido
print(nombreapellido)

#ejer13
edad= 20
edad=edad+5
edad=edad-10

#ejer14

altura=1.75
altura= altura*4
altura= altura/3

#ejer15

nommayus= "MAXIMILIANO"
print(nommayus)
nommayus=nommayus.lower()
print(nommayus)
nommayus=nommayus.upper()
print(nommayus)


print("----------------")


#ejer16
cad=nommayus
print(cad)
aux="true"
for con in cad:
    if (aux=="true"):
        cad2=con
        aux="False"
    else:
        cad2=cad2 + con.lower()
    
print(cad2)


  