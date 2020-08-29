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


    
def ProesarSolicitud(solicitud):
    """
    procesa la solisitud para el ordenamiento
    retorna el orden a realizar
    """

    ordenes=solicitud.split("|")

    ordenesOK=[]
    for orden in ordenes:
        if "!" not in orden:
           #orden valida, me la quedo
            ordenesOK.append(orden)

    #print(ordenesOK)
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

def OrdenarMails(mails2, ordenes):
    """
    Ordena la lista de mails en el orden dado
    https://www.w3schools.com/python/ref_list_sort.asp
    """
    mails=mails2.copy()
    print("sin ordenar:")
    for newlst in mails:
        print(newlst)
    #    print(newlst["Flag"])
        print("")
    
    print("----"*12)
    
    
    
    """for mail in mails:
        if "A" in mail["Flag"]:
            #lo ordeno
    """        
    from operator import itemgetter 
    

    listaFlag=[]
    newlist=[]
    #recorro las ordenes
    for orden in ordenes:
        #separo la orden 
        orde = orden.split("-")
        #recorro los mail
        for mail in mails:
            #me fijo si tienen el flag
            print("reviso=",mail)
            index=mails.index(mail)
            print(index)
                
            if orde[0] in mail["Flag"]:
                #los guardo en la lista para ordenar
                listaFlag.append(mail.copy())
                #ahora tengo que sacarlo de la lista a revisar
                mail["Flag"]="--"
                print("remove=",mail)
            else:
                print("no tiene flag")
                                
        #me fijo si el orden es fifo o lifo
        if "FIFO" in orde[1]:
            #orden FIFO
            newlist = newlist + sorted(listaFlag, key=itemgetter('fecha')) 
        else:
            #orden LIFO
            newlist = newlist + sorted(listaFlag, key=itemgetter('fecha'),reverse=True) 

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



    

def OrdenarMails_0(mails, orden):
    """
    Ordena la lista de mails en el orden dado
    https://www.w3schools.com/python/ref_list_sort.asp
    """
    print("sin ordenar:")
    print(mails)
    print("----"*12)
    
    #mails.sort("Flag")
    
    """for mail in mails:
        if "A" in mail["Flag"]:
            #lo ordeno
    """        
    
    from operator import itemgetter 
    newlist = sorted(mails, key=itemgetter('Flag','fecha')) 
    for newlst in newlist:
        print(newlst)
        print("")
    
        
    
    
if __name__== "__main__":
    #ProesarSolicitud("B-LIFO|!C-FIFO|C-LIFO")
    #BuscarFecha("MailA Flag: A B Fecha de RecepciÃ³n: 01/04/15.")
    #BuscarFlags("MailA Flag: A B Fecha de RecepciÃ³n: 01/04/15.")
    mails=LeerArchivoMail()
    #orden=ProesarSolicitud("B-LIFO|!C-FIFO|C-LIFO")
    orden=ProesarSolicitud("B-LIFO|!C-FIFO|C-LIFO")
    mailsCustomizados= CustomizarMail(mails)
    OrdenarMails(mailsCustomizados, orden)
    
    
    