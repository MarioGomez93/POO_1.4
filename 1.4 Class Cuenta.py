'''

1) Pedir la clave al momento de hacer una extraccion.
2) Hacer una lista de registro de extraccion y deposito incluyendo fecha y hora de la
operacion (libreria)
3) Pedir la clave al momento de hacer una modificacion de clave.
4) Si ingresa 3 veces una clave no valida, entonces mostrar un mensaje
con el telefono de la financiera e invitando al usuario a contactarse.
Y bloquear cuenta
5)Agregar nombre y apellido asociado a la cuenta.

PARA EL VIERNES 5/5/23

'''



class Cuenta:
    
    def __init__(self,nCuenta):
        self.__nCuenta=nCuenta
        self.__saldo=0
        self.__limExt=300
        self.__clave=1234
        
    def depositar(self,monto):
        self.__saldo=self.__saldo+monto
    
    def extraer(self,monto):
        msj=""
        if self.__limExt>=monto:
            if self.__saldo>=monto:
                self.__saldo-=monto
                msj="Extraccion con exito ({})".format(monto)
                
            else:
                msj="ERROR: Saldo insuficiente ({})".format(self.__saldo)
        
        else:
            msj="ERROR: Supera el limite de extraccion ({})".format(self.__limExt)
            
        return msj
    
    def obtenerSaldo(self):
        return self.__saldo
    
    def modiClave(self,claveNueva):
        if len(claveNueva)>=4:
            self.__clave=claveNueva