# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 09:50:11 2020

@author: Matias
python3
"""
#importo librerias
# manejo de fechas
from datetime import datetime
# manejo de string
# documentacion: https://docs.python.org/2/library/re.html
import re
from operator import itemgetter

class ManejadorArchivo():
    
    def __str__(self):
        return ("Lee y escribe archivos")
    
    def LeerArchivoMail(arvivo):
        """
        lee el archivo mail.txt y me quedo solo con lo que tiene Flag
        retorna los mail a ordenar
        """
        #Abro el archivo con los mails
        archivoMail=open(arvivo,"r")
        #Leo el archivo con los mails
        listaDeMail=archivoMail.read()
        #cierro el archivo con los mails
        archivoMail.close()
    
       
        #Del archivo me quedo solo con los mail utiles que tiene Flag
        mailsOK=[]
        a=listaDeMail.splitlines()
        for linea in a:
            if "Flag" in linea :
                
                mailsOK.append(linea)
           
        return(mailsOK)
    
    
  
       
    def EscribirArchivo(archivo, mails):
        """
        escribo el archivo con la salida solicitada
        """
        archivoOrdenado = open(archivo, "a")
        archivoOrdenado.write("ordenados\n")
        print("----"*12)
        print("ordenados\n")
        for mail in mails:
            archivoOrdenado.write(mail["cuerpo"])
            archivoOrdenado.write("\n")
            print(mail["cuerpo"])
        archivoOrdenado.write("-----\n")    
        
        archivoOrdenado.close()


#----fin de clase ManejadorArchivo-----

class OrdenadorDeMail():
    
    def __str__(self):
        return("clase para ordenar los mails de IMAP")
    
    def ProcesarSolicitud(solicitud):
        """
        procesa la solisitud para el ordenamiento
        retorna el orden a realizar
        """
    
        ordenes=solicitud.split("|")
        ordenesOK=[]
        for orden in ordenes:
            ordenesOK.append(orden)
    
        
        return(ordenesOK)
    
    
    def BuscarFecha(mail):
        """
        retorna la fecha del string que pasa
        """
        stringFecha=mail[-9:-1]
    
        #convierto en formato fecha
        fecha = datetime.strptime(stringFecha, '%d/%m/%y')
    
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
            aux= {"Flag":OrdenadorDeMail.BuscarFlags(mail) ,"fecha":OrdenadorDeMail.BuscarFecha(mail)  ,"cuerpo":mail }
            camposArmados.append(aux)
    
            
        print("Para ordenar\n")
        for mail in camposArmados:
            print(mail["cuerpo"])
            
        return(camposArmados)
    
    
    
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
        for mail in mails:
            if "--" !=  mail["Flag"]:
                listaFlag.append(mail.copy())
                mail["Flag"]="--"        
                
        for orden in ordenes:               
            orde = orden.split("-")
            if "!" in orde[0]:
                if "FIFO" in orde[1]:
                    #orden FIFO
                    newlist2 = newlist2+ sorted(listaFlag.copy(), key=itemgetter('fecha'))
                    break
                else:
                    #orden LIFO
                    newlist2 = newlist2+ sorted(listaFlag.copy(), key=itemgetter('fecha'),reverse=True)
                    break
    
        #borro tolos los elementos de la listaFlag
        listaFlag.clear()
       
        
        flagNo=1
        #me fijo si esta primero o ultimo el !
        for orden in ordenes:
            orde = orden.split("-")
            if "!" in orde[0]:
                flagNo=0            
                if 0 == ordenes.index(orden):
                    #"esta primero"
                    #lo pongo principio
                    newlist=newlist2+newlist
                    flagNo=1
                    for newl in newlist:                    
                        index=newlist.index(newl)
                    
                elif ordenes.index(orden) == (len(ordenes)-1):
                    #esta ultimo
                    newlist=newlist+newlist2
                    flagNo=1
                    
                    
                    
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
                        #me fijo si !flag tiene que ir
                        a=ordenes[orden+1].split("-")
                        if "!" in a[0]:
                            #incerto la lista en el lugar
                            j=0
                            for newlst2 in newlist2:
                                newlist.insert(index+j , newlst2.copy())
                                j=j+1
                                   
                            ManejadorArchivo.EscribirArchivo("./mailOrdenados.txt",newlist)   
                            return(0)
        ManejadorArchivo.EscribirArchivo("./mailOrdenados.txt",newlist) 
        return(0)
        
                    
                        
        
    def OrdenarMailsIMAP(ordenes):
        """
        lee del archivo mail,txt y los ordena en el orden especificado guardandolos 
        en mailOrdenados.txt
        """
        mails=ManejadorArchivo.LeerArchivoMail("./mail.txt")
        orden=OrdenadorDeMail.ProcesarSolicitud(ordenes)
        mailsCustomizados= OrdenadorDeMail.CustomizarMail(mails)
        OrdenadorDeMail.OrdenarMails(mailsCustomizados, orden)
    
    
if __name__== "__main__":

    
    OrdenadorDeMail.OrdenarMailsIMAP("B-LIFO|!C-FIFO|C-LIFO")
