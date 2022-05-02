import csv
class ViajeroFrecuente:
    __num_viajero=0
    __dni=''
    __nombre=''
    __apellido=''
    __milla_acum=0
    
    def __init__(self,num_viajero=0, dni='',nombre='',apellido='',milla_acum=0):
        self.__num_viajero=num_viajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__milla_acum=milla_acum
    def __eq__(self,millas):
        return self.__milla_acum==millas
    def __req__(self,millas):
        return self.__milla_acum==millas
    def __radd__(self,can):
        return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__milla_acum+can)
    def __rsub__(self,can):
        return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__milla_acum-can)
    def __str__(self):
        return "Numero de viajero:%d, DNI:%s,Nombre:%s,Apellido:%s, Cantidad de millas:%d"%(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__milla_acum)
    def funcionTestViajero(self):
        print("---------Funcion test Viajero:---------")
        print("****Viajeros****")
        viajero1=ViajeroFrecuente(500,'33444555','Paulo','Diaz',600) 
        viajero2=ViajeroFrecuente(400,'21345678','Kevin','Trump',700)
        print(viajero1)
        print(viajero2)
        print("---Acumular millas---")
        viajero3=400+viajero1
        viajero4=300+viajero2
        print(viajero3)
        print(viajero4)
        print("---Canjear millas---")
        viajero5=100-viajero1
        viajero6=100-viajero2
        print(viajero5)
        print(viajero6)
        print("---Comparar millas---")
        if 600==viajero1:
            print("Tiene 600 millas")
        else:
            print("No tiene 600 millas")
        if viajero2==400:
            print("Tiene 400 millas")
        else:
            print("No tiene 400 millas")


