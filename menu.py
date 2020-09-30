import os
def Numeros():
    print ("******Opcion de numeros********")
    #ingresar n numeros donde n es un numero ingresado por teclado , calcular y mostrar
    #cantidad de numeros positivos , cantidad de numeros negaticos y catidad de iguales a 0
    pos=0
    neg=0
    cero=0
    veces=int(input("cuantos numeros decea ingresar: "))
    for x in range(veces):

        nume=int(input("ingrese un numero : "))

        if(nume>0):
            pos=pos+1
        elif(nume<0):
            neg=neg+1
        else:
            cero=cero+1
    
    
    print(  "Cantidad de numeros negativos: " +str(pos)+
            "\nCantidad de numeros negativos : " + str(neg)+
            "\nCantidad de nuemros iguales a cero: " + str(cero))
    pausa=input("presione una tecla para continuar")

def Datos():
    print("*********Opcion de datos de personas*********")
    #ingresar para n personas donde n es un número ingresado por teclado: nombre y edad. 
    #calcular y mostrar: cantidad de personas mayores de edad y cantidad de menores de edad. 
    #subir la modificar a github con el siguiente mensaje: "se programo la opción 2 del menú"
    pausa=input("presione una tecla para continuar")

seguir=True
while (seguir):
    os.system('cls')
    print("1. Opción Numeros ")
    print("2. Opción Datos de Personas ")
    print("3. Finalizar")
    op=int(input("Ingrese opción 1,2,3: "))
    if (op==1):
        Numeros()
    if (op==2):
        Datos()
    if (op==3):
        seguir=False
        break
    
