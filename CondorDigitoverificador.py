# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:12:08 2020

@author: Matias
"""



def PasoA( numero):
    """Hace el paso A
    Invierte un numero ingresado
    Invertir el número. (e.g: de 201012341 a 143210102).
    Interesante ananlis temporal de conversion: https://stackoverflow.com/questions/13905936/converting-integer-to-digit-list
    """

    revertir = 0
    try:
        valor = int( numero)
        while valor > 0:
            residuo = valor % 10
            revertir = (revertir * 10) + residuo
            valor //= 10
        print('El inverso del número ingresado es: ', revertir)
        return( revertir)
    except ValueError as error:
        #si da error seguro que dio error al castear el numero a int
        print('Error funcion PasoA!! ::-> ' , error)
        
    
def PasoB( numeroIngresado):
    """hace el paso B del digito verificador
    Multiplicar los dígitos por la secuencia 2, 3, 4, 5, 6, 7, si es que se acaban los números, se debe
comenzar de nuevo, por ejemplo , con 143210102:
1×2+4×3+3×4+2×5+1×6+0×7+1×2+0×3+2×4=52
       
    """
    secuencia = [ 2 , 3 , 4 , 5 , 6 , 7 ]
    valor = numeroIngresado
    listaAux=[]
    
    #utlizo la misma logica para recorrer el numero para generar una lista
    while valor > 0:
        residuo = valor % 10   
        valor //= 10
        
        listaAux= [residuo] + listaAux
    
    print("",listaAux)
    
    
    #multiplico los conenidos de las lista
    j=0
    listaMultiplicada=[]
    for i in listaAux:
        listaMultiplicada.append( i * secuencia[j])
        j = j+1
        j = j %  len(secuencia)
        
        
    print("lista multiplicada",listaMultiplicada)
    print("sumo todos los valores de la lista y la paso a entero",int(sum(listaMultiplicada)))
    return(int(sum(listaMultiplicada)))

def PasoC(numero):
    """
    Al resultado obtenido, es decir, 52, debemos sacarle el módulo 11, es decir:
52 % 11 = 8
    """
    return(numero % 11)

def PasoD(numero):
    """
    Con el resultado obtenido en el paso anterior, debemos restarlo de 11:
11 − 8 = 3
    """
    return( 11 - numero)

def PasoE(numero):
    """
    Si el numero es 11 entonces se intercambia por 0, si es 10 es 1.
    como no se especifica se retorna -1 para otros casos
    """
    if 11 == numero:
        return(0)
    elif 1 == numero:
        return(1)
    else:
        return(-1)


def DigitoVerificador():
    """
    Realiza la deteccion sobre el digito verificador
    """
    numeroIngresado = (input("Ingrese un número: "))    
    numeroInvertido = PasoA( numeroIngresado )
    numeroProcesado = PasoB(numeroInvertido)
    
    digitoVerificador=PasoD(PasoC(numeroProcesado))
    
    digitoVerificado=PasoE(digitoVerificador)
    print(digitoVerificado)
    return(digitoVerificado)
        
    
if __name__ == "__main__":
    DigitoVerificador()
  

    
    
    