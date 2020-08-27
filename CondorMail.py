# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 09:50:11 2020

@author: Matias
"""

def LeerArchivoMail():
    """ 
    lee el archivo mail.txt y me quedo solo con lo que tiene Flag
    retorna los mail a ordenar
    """
    #Abro el archivo con los mails
    archivoMail=open("mail.txt","r")
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
    for mail in mailsOK:
        if "A" in mail :
            print(mail)
                
                
                
            
            
    return(mailsOK)
def CustomizarMail():
    """
    a la lista de mail la prepara para analizarla
    """
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
            
    print(ordenesOK)
    return(ordenesOK)
    
def OrdenarMails(mails, orden):
    """
    Ordena la lista de mails en el orden dado
    """
    


if __name__== "__main__":
    #ProesarSolicitud("B-LIFO|!C-FIFO|C-LIFO")
    LeerArchivoMail()