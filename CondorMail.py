# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 09:50:11 2020

@author: Matias
"""
#importo librerias
# manejo de fechas
from datetime import datetime
# manejo de string
# documentacion: https://docs.python.org/2/library/re.html
import re
from operator import itemgetter

def LeerArchivoMail():
    """
    lee el archivo mail.txt y me quedo solo con lo que tiene Flag
    retorna los mail a ordenar
    """
    #Abro el archivo con los mails
    archivoMail=open("./mail.txt","r")
    #Leo el archivo con los mails
    listaDeMail=archivoMail.read()
    #cierro el archivo con los mails
    archivoMail.close()

    #print(listaDeMail)
    #Del archivo me quedo solo con los mail utiles que tiene Flag
    mailsOK=[]
    a=listaDeMail.splitlines()
    for linea in a:
        if "Flag" in linea :
            #print(linea)
            mailsOK.append(linea)

    #print("mailsOK:", mailsOK)
    #MailA Flag: A B Fecha de RecepciÃ³n: 01/01/15.

    return(mailsOK)



def ProcesarSolicitud(solicitud):
    """
    procesa la solisitud para el ordenamiento
    retorna el orden a realizar
    """

    ordenes=solicitud.split("|")
    ordenesOK=[]
    for orden in ordenes:
        #if "!" not in orden:
           #orden valida, me la quedo
        ordenesOK.append(orden)

    
    return(ordenesOK)


def BuscarFecha(mail):
    """
    retorna la fecha del string que pasa
    """
    #MailA Flag: A B Fecha de RecepciÃ³n: 01/01/15.
    #print(mail[-9:-1])
    stringFecha=mail[-9:-1]

    #convierto en formato fecha
    fecha = datetime.strptime(stringFecha, '%d/%m/%y')
    #print(fecha.date())
    return(fecha.date())

def BuscarFlags(mail):
    """
    retorna los flags del mail
    """
    try:
        # busco los flags en la secuencia en el estring que este entre
        # las palabras Flag: XXXX Fecha
        # MailA Flag: A B Fecha de RecepciÃ³n: 01/04/15.

        flag = re.search('Flag: (.+?) Fecha ', mail).group(1)
        #print(flag)
        return(flag)
    except :
        # no se encontro nada
        print("no se encontro flags en el mail nada")

def CustomizarMail(mails):
    """
    a la lista de mail la prepara para analizarla
    """

    camposArmados=[]

    for mail in mails:
        # los armo en este orden [flags, fecha, cotenido¨]
        aux= {"Flag":BuscarFlags(mail) ,"fecha":BuscarFecha(mail)  ,"cuerpo":mail }
        camposArmados.append(aux)
    #print(a)
    return(camposArmados)

def OrdenarMails_0(mails_original, ordenes):
    """
    Ordena la lista de mails en el orden dado
    
    """
    mails=mails_original.copy()
  


    listaFlag=[]
    newlist=[]
    #recorro las ordenes
    for orden in ordenes:
        #separo la orden
        orde = orden.split("-")
        #recorro los mail
        for mail in mails:
            #me fijo si tienen el flag
            if orde[0] in mail["Flag"]:
                #los guardo en la lista para ordenar
                listaFlag.append(mail.copy())
                #ahora tengo que sacarlo de la lista a revisar
                mail["Flag"]="--"
             

        #me fijo si el orden es fifo o lifo
        if "FIFO" in orde[1]:
            #orden FIFO
            newlist = newlist + sorted(listaFlag.copy(), key=itemgetter('fecha'))
        else:
            #orden LIFO
            newlist = newlist + sorted(listaFlag.copy(), key=itemgetter('fecha'),reverse=True)
        #borro tolos los elementos de la listaFlag
        listaFlag.clear()

    #especifica el critero para los flag algunos flag los ordeno por fecha
    newlist2=[]
    for orden in ordenes:               
        orde = orden.split("-")
        for mail in mails:
            if "--"!=  mail["Flag"]:
                listaFlag.append(mail.copy())
                mail["Flag"]="--"        
        if "FIFO" in orde[1]:
            #orden FIFO
            newlist2 = newlist2+ sorted(listaFlag.copy(), key=itemgetter('fecha'))
        else:
            #orden LIFO
            newlist2 = newlist2+ sorted(listaFlag.copy(), key=itemgetter('fecha'),reverse=True)

        #borro tolos los elementos de la listaFlag
        listaFlag.clear()
   
    #
    flagNo=1
    for orden in ordenes:
        orde = orden.split("-")
        if "!" in orde[0]:
            flagNo=0
            
    if 0==flagNo:
        #tengo que incertar la lista de las ! flag en su posicion
        for orden in range(len(ordenes)):
            #separo la orden
            orde = ordenes[orden].split("-")
            #recorro los mail
            for mail in newlist:
                #me fijo si tienen el flag
     #           print("reviso=",mail)
                index=newlist.index(mail)
      #          print(index)
                if orde[0] not in mail["Flag"]:
                #salto de flag en la lista ordenada
       #             print("orde[0] in mail[Flag]")
                
                    #me fijo si !flag tiene que ir
                    a=ordenes[orden+1].split("-")
                    if "!" in a[0]:
                        #incerto la lista en el lugar
                        newlist.insert(index,newlist2)
                        
                        ##muestro las cosas y e voy                    
                        print("----"*12)
                        print("ordenado:")
                        for newl in newlist:
                            print(newl)
                            index=newlist.index(newl)
                            print(index)
                            print("")
                    
                        #return(0)
                        print("////"*12)
                        print("sin ordenar:")
                        for newlst in mails:
                            print(newlst)
                            #print(newlst["Flag"])
                            print("")
                            
                        return(0)

def OrdenarListaPorFecha(lista, sentido):
    """
    ordena la lista en el sentido que corresponde
    """
    
    
    
def EscribirArchivo(mails):
    """
    escribo el archivo con la salida solicitada
    """
    archivoOrdenado = open("./mailOrdenados.txt", "a")
    archivoOrdenado.write("ordenados\n")
    for mail in mails:
        archivoOrdenado.write(mail["cuerpo"]+"\n")
    
    archivoOrdenado.write("-----\n")    
    
    archivoOrdenado.close()


def OrdenarMails(mails_original, ordenes):
    """
    Ordena la lista de mails en el orden dado
    
    """
    mails=mails_original.copy()
  

    listaFlag=[]
    newlist=[]
    #recorro las ordenes
    for orden in ordenes:
        #separo la orden
        orde = orden.split("-")
        #recorro los mail
        for mail in mails:
            #me fijo si tienen el flag
            if orde[0] in mail["Flag"]:
                #los guardo en la lista para ordenar
                listaFlag.append(mail.copy())
                #ahora tengo que sacarlo de la lista a revisar
                mail["Flag"]="--"
             

        #me fijo si el orden es fifo o lifo
        if "FIFO" in orde[1]:
            #orden FIFO
            newlist = newlist + sorted(listaFlag.copy(), key=itemgetter('fecha'))
        else:
            #orden LIFO
            newlist = newlist + sorted(listaFlag.copy(), key=itemgetter('fecha'),reverse=True)
        #borro tolos los elementos de la listaFlag
        listaFlag.clear()

    #especifica el critero para los flag algunos flag los ordeno por fecha
    newlist2=[]
    for orden in ordenes:               
        orde = orden.split("-")
        for mail in mails:
            if "--"!=  mail["Flag"]:
                listaFlag.append(mail.copy())
                mail["Flag"]="--"        
        if "FIFO" in orde[1]:
            #orden FIFO
            newlist2 = newlist2+ sorted(listaFlag.copy(), key=itemgetter('fecha'))
        else:
            #orden LIFO
            newlist2 = newlist2+ sorted(listaFlag.copy(), key=itemgetter('fecha'),reverse=True)

        #borro tolos los elementos de la listaFlag
        listaFlag.clear()
   
    
    flagNo=1
    for orden in ordenes:
        orde = orden.split("-")
        if "!" in orde[0]:
            print("orde[0]",orde[0])
            flagNo=0
            print(" ordenes.index(orden)  == len(ordenes)", ordenes.index(orden))
            print( len(ordenes)-1)
            if 0 == ordenes.index(orden):
                print("es esta primero")
                #lo pongo principio
                newlist=newlist2+newlist
                flagNo=1
                print("----"*12)
                print("ordenado:")
                for newl in newlist:
                    print(newl)
                    index=newlist.index(newl)
                    print(index)
                    print("")
                EscribirArchivo(newlist)            
                
            if ordenes.index(orden) == (len(ordenes)-1):
                print("esta ultimo")
                newlist=newlist+newlist2
                flagNo=1
                EscribirArchivo(newlist)            
                
                
    if 0==flagNo:
        #tengo que incertar la lista de las ! flag en su posicion
        for orden in range(len(ordenes)):
            #separo la orden
            orde = ordenes[orden].split("-")
            #recorro los mail
            for mail in newlist:
                #me fijo si tienen el flag
     #           print("reviso=",mail)
                index=newlist.index(mail)
      #          print(index)
                if orde[0] not in mail["Flag"]:
                #salto de flag en la lista ordenada
       #             print("orde[0] in mail[Flag]")
                
                    #me fijo si !flag tiene que ir
                    a=ordenes[orden+1].split("-")
                    if "!" in a[0]:
                        #incerto la lista en el lugar
                        newlist.insert(index,newlist2)
                        EscribirArchivo(newlist)            

    

if __name__== "__main__":

    mails=LeerArchivoMail()
    #no pincha
    #orden=ProcesarSolicitud("!C-FIFO|B-LIFO|C-LIFO")
   # orden=ProcesarSolicitud("A-LIFO|C-LIFO|!C-FIFO")
    #---
    
    orden=ProcesarSolicitud("B-LIFO|!C-FIFO|C-LIFO")#pincha
    mailsCustomizados= CustomizarMail(mails)
    OrdenarMails(mailsCustomizados, orden)
