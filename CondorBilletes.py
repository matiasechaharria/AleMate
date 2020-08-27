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
    
    def CargaInicialStandar(self):
        """
        CargaInicial:
            cuando se carga el cajero se ingresa la cantidad de billetes 
            por cada denominacion
        """
        carga={
            "billete100" : {
                "denominacion" : 100,
                "cantidad" : 10
                },
            "billete50" : {
                "denominacion" : 50,
                "cantidad" : 10
                },
            "billete20" : {
                "denominacion" : 20,
                "cantidad" : 10
                },
            "billete10" : {
                "denominacion" : 10,
                "cantidad" : 10
                },
            "billete5" : {
                "denominacion" : 5,
                "cantidad" : 10
                },
            "billete1" : {
                "denominacion" : 1,
                "cantidad" : 10
                }
            }
        
        for billete in self.dinero:
            self.dinero[billete]["cantidad"]=carga[billete]["cantidad"]
            
        
    def EntregaDinero(self, entregado):
        """
        resta la cantidad correspondiete a cada denominacion extraida
        """
        
       # print("emito el dinero ")
        
        for billete in self.dinero:
            self.dinero[billete]["cantidad"]=self.dinero[billete]["cantidad"]-entregado[billete]["cantidad"]
            

    def SolicitudDinero(self, montoSolicitado):
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
        monto=montoSolicitado
        
        montoMaximo=0
        for billete in dinero:
            montoMaximo+=dinero[billete]["denominacion"]*dinero[billete]["cantidad"]
            
        if monto > montoMaximo:
            print("no hay suficiente dinero disponible")
            return(despacho)
        
        
        for billete in dinero:
                        
            if 0 < monto:
                 #tengo billetes de 100
                 if 0 < dinero[billete]["cantidad"]:
                     #Cantidad de 100 que necesito
                     cant100= int(monto /dinero[billete]["denominacion"])
                     #tengo esa cantidad?
                     if 0 < dinero[billete]["cantidad"]-cant100:
                         #tengo esa cantidad   
                         despacho[billete]["cantidad"]=cant100
                     else:
                         #no tengo esa cantidad, asi que entrego los que tengo
                         despacho[billete]["cantidad"]=dinero[billete]["cantidad"]
                #monto restante = cantidad * denominacion
                 monto=monto-despacho[billete]["denominacion"]*despacho[billete]["cantidad"]           
        
            
        return( despacho)
        
        
        
    def CantidadDenominacion(self):
        """
        muestra la cantidad de dinero por cada denominacion
        """
        dinero=self.dinero
        
        for billete in dinero:
            print("denominacion=" , dinero[billete]["denominacion"])
            print("cantidad=", dinero[billete]["cantidad"])
       
        
    def CantidadMaximaDisponible(self):
        """
        calcula cuanto es el total de dinero que tiene el cajero
        """
        montoMaximo=0
        for billete in self.dinero:
            montoMaximo+=self.dinero[billete]["denominacion"]*self.dinero[billete]["cantidad"]
        return(montoMaximo)

if __name__ == "__main__":
   cjro=cajero()
   
   print("---"*12)
   print("veo que el cajero este vacio")
   cjro.CantidadDenominacion()
   
   print("---"*12)
   print("hago la carga inicial standar")
   cjro.CargaInicialStandar()
   
   
   print("---"*12)
   print("cuanto dinero tiene el cajero?")
   dineroTotal=cjro.CantidadMaximaDisponible()
   print("el total de dinero es= ",dineroTotal)
   
   print("---"*12)
   print("veo quedo cargado en el cajero")
   cjro.CantidadDenominacion()
   
   
   
   print("---"*12)
   print("hago una solicitud de dinero")
   entregar=cjro.SolicitudDinero(46)
  
   
   print("---"*12)
   print("entrega dinero")
   cjro.EntregaDinero(entregar)
   
   
   print("---"*12)
   print("veo cuanto quedo en el cajero")
   cjro.CantidadDenominacion()
   