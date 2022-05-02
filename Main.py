from ViajeroFrecuente import ViajeroFrecuente
if __name__=='__main__':
    viajero=ViajeroFrecuente(100,20455567,'Jose','Perez',1000)
    viajero2=ViajeroFrecuente(130,25089998,'Juan','Olivares',1000)
    print("----------Viajeros---------")
    print(viajero)
    print(viajero2)
    print("*** Comparar***")
    if viajero==1000:
        print("Tiene 1000 millas acumuladas.")
    else:
        print("No tiene 1000 millas acumuladas.")
    if 100==viajero2:
        print("Tiene 100 millas acumuladas. ")
    else:
        print("No tiene 100 millas acumuladas.")
    print("***Acumular millas***")
    viajero3=200+viajero
    viajero4=300+viajero2
    print(viajero3)
    print(viajero4)
    print("***Canjear millas***")
    viajero5=100-viajero
    viajero6=200-viajero2
    print(viajero5)
    print(viajero6)
    
    viajero.funcionTestViajero()
