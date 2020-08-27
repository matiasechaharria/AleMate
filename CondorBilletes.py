# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 09:49:54 2020

@author: Matias
"""
class cajero(  ):
    
    
    def __init__(self ):
       
        self.dinero={
            "billete100" : {
                "denominacion" : 100,
                "cantidad" : 0
                },
            "billete50" : {
                "denominacion" : 50,
                "cantidad" : 0
                },
            "billete20" : {
                "denominacion" : 20,
                "cantidad" : 0
                },
            "billete10" : {
                "denominacion" : 10,
                "cantidad" : 0
                },
            "billete5" : {
                "denominacion" : 5,
                "cantidad" : 0
                },
            "billete1" : {
                "denominacion" : 1,
                "cantidad" : 0
                }
            }
    
    def CargaInicial(self, carga100=0, carga50=0, carga10=0,
                     carga20=0 ,  carga5=0,    carga1=0):
        """
        CargaInicial:
            cuando se carga el cajero se ingresa la cantidad de billetes 
            por cada denominacion
        """
        self.billete100=carga100
        self.billete50=carga50
        self.billete20=carga20
        self.billete10=carga10
        self.billete5=carga5
        self.billete1=carga1
        
    def EntregaDinero(self, entregado):
        """
        resta la cantidad correspondiete a cada denominacion extraida
        """
        dinero=self.dinero
        print("emito el dinero y veo cuanto queda por cada denominacion")
        
        for k in dinero:
            self.dinero[k]["canitdad"]=self.dinero[k]["canitdad"]-despacho["canitdad"]
            print("denominacion=" , self.dinero[k]["denominacion"])
            print("cantidad=", self.dinero[k]["cantidad"])

    def SolicitudDinero2(self, montoSolicitado):
        """
        calcula cuanto tiene que despachar
        """           
        despacho={
            "billete100" : {
                "denominacion" : 100,
                "cantidad" : 0
                },
            "billete50" : {
                "denominacion" : 50,
                "cantidad" : 0
                },
            "billete20" : {
                "denominacion" : 20,
                "cantidad" : 0
                },
            "billete10" : {
                "denominacion" : 10,
                "cantidad" : 0
                },
            "billete5" : {
                "denominacion" : 5,
                "cantidad" : 0
                },
            "billete1" : {
                "denominacion" : 1,
                "cantidad" : 0
                }
            }

        dinero=self.dinero
        montoSolicitado=521
        print("billete ")
    
        monto=montoSolicitado
        for k in dinero:
            #print ("k",k) # billete
            print("denominacion=",dinero[k]["denominacion"])
            print("cantidad=",dinero[k]["cantidad"])    
            
            if 0 < monto:
                 #tengo billetes de 100
                 if 0 < dinero[k]["cantidad"]:
                     #Cantidad de 100 que necesito
                     cant100= int(monto /dinero[k]["denominacion"])
                     #tengo esa cantidad?
                     if 0 < dinero[k]["cantidad"]-cant100:
                         #tengo esa cantidad   
                         despacho[k]["cantidad"]=cant100
                     else:
                         #no tengo esa cantidad, asi que entrego los que tengo
                         despacho[k]["cantidad"]=dinero[k]["cantidad"]
                #monto restante = cantidad * denominacion
                 monto=monto-despacho[k]["denominacion"]*despacho[k]["cantidad"]           
                 print("monto", monto)
                    
        print("---"*12)            
        print("despacho")
        
        for k in despacho:
            #print ("k",k) # billete
            print("denominacion=",despacho[k]["denominacion"])
            print("cantidad=",despacho[k]["cantidad"])
            
        EntregaDinero( despacho)
        
    def SolicitudDinero(self, montoSolicitado):
        """
        Calcula como entregar el dinero
        """
        dinero={
            "billete100" : {
                "denominacion" : 100,
                "cantidad" : 4
                },
            "billete50" : {
                "denominacion" : 50,
                "cantidad" : 2007
                },
            "billete20" : {
                "denominacion" : 50,
                "cantidad" : 2007
                }
            }
        
        monto=montoSolicitado
        
        #tengo villetes de 100
        if 0==self.billete100:
            #Cantidad de 100 que necesito
            cant100=monto/100
            if 0 < self.billete100-cant100:
                #tengo esa cantidad   
                despacho100=cant100
            else:
                #no tengo esa cantidad, asi que entrego los que tengo
                despacho100=self.billete100
        
        #monto restante = cantidad * denominacion
        monto=monto-despacho100*100
        
        
                
            
        
        
    def CantidadDenominacion():
        """
        """
        
        
    
        


if __name__ == "__main__":
   # cajero.CargaInicial(1, 2 , 3 , 4 , 5 , 6)
    #valor = input("Ingrese un valor a retirar: ")
        
    dinero={
            "billete100" : {
                "denominacion" : 100,
                "cantidad" : 4
                },
            "billete50" : {
                "denominacion" : 50,
                "cantidad" : 3
                },
            "billete20" : {
                "denominacion" : 20,
                "cantidad" : 6
                },
            "billete10" : {
                "denominacion" : 10,
                "cantidad" : 9
                },
            "billete5" : {
                "denominacion" : 5,
                "cantidad" : 12
                },
            "billete1" : {
                "denominacion" : 1,
                "cantidad" : 24
                }
            }
    despacho={
            "billete100" : {
                "denominacion" : 100,
                "cantidad" : 0
                },
            "billete50" : {
                "denominacion" : 50,
                "cantidad" : 0
                },
            "billete20" : {
                "denominacion" : 20,
                "cantidad" : 0
                },
            "billete10" : {
                "denominacion" : 10,
                "cantidad" : 0
                },
            "billete5" : {
                "denominacion" : 5,
                "cantidad" : 0
                },
            "billete1" : {
                "denominacion" : 1,
                "cantidad" : 0
                }
            }

    
    
    montoSolicitado=521
    print("billete ")

    monto=montoSolicitado
    for k in dinero:
        #print ("k",k) # billete
        print("denominacion=",dinero[k]["denominacion"])
        print("cantidad=",dinero[k]["cantidad"])    
        
        if 0 < monto:
             #tengo billetes de 100
             if 0 < dinero[k]["cantidad"]:
                 #Cantidad de 100 que necesito
                 cant100= int(monto /dinero[k]["denominacion"])
                 #tengo esa cantidad?
                 if 0 < dinero[k]["cantidad"]-cant100:
                     #tengo esa cantidad   
                     despacho[k]["cantidad"]=cant100
                 else:
                     #no tengo esa cantidad, asi que entrego los que tengo
                     despacho[k]["cantidad"]=dinero[k]["cantidad"]
            #monto restante = cantidad * denominacion
             monto=monto-despacho[k]["denominacion"]*despacho[k]["cantidad"]           
             print("monto", monto)
                
    print("---"*12)            
    print("despacho")
    
    for k in despacho:
        #print ("k",k) # billete
        print("denominacion=",despacho[k]["denominacion"])
        print("cantidad=",despacho[k]["cantidad"])    
        