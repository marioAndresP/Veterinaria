from datetime import date
from datetime import datetime
from datetime import timedelta
class Veterninaria:
    edificio =""
    direccion =""
    telefono = 0
    asensor = False
    puertas = False

    def __init__(self, edificio, direccion, telefono):
        self.edificio = edificio
        self.direccion = direccion
        self.telefono = telefono

    def hacerLlamada(self,pTelefono):
        if self.telefono == pTelefono:
            return "Llamando... "
        else:
            return "Telefono incorrecto"

    def setAsensor (self,pAsensor):
        if pAsensor=="si":
            self.asensor=True
        else:
            self.asensor=False 

    def subirAsensor(self):
        if self.asensor==True:
            return "Asensor sube"
        else:
            return "Asensor no sube"
            
    def setPuerta (self,pPuerta):
        if pPuerta=="si":
            self.puertas=True
        else:
            self.puertas=False 
    def abrirPuerta(self):
        if self.puertas==True:
            return "Puertas abiertas"
        else:
            return "No se abrieron puertas"


class Mascota:
    nombre = ""
    edad = 0
    especie=""
    genero =""
    raza=""
    estaEnPeligro = False

    def __init__(self, nombre, edad, especie, genero, raza):
        self.nombre=nombre
        self.edad = edad
        self.especie = especie
        self.genero = genero
        self.raza = raza 

    def mayorEdad(self):
        if self.edad>7:
            return self.nombre+" es mayor"
        else:
            return self.nombre+" es menor"

    def darNombre(self):
        return self.nombre

    
    def setEstaEnPeligro(self,pPeligro):
            if pPeligro == "si":
                self.estaEnPeligro=True
            else:
                pPeligro = False

    def darEstaEnPeligro(self):
        if self.estaEnPeligro == True:
            return self.nombre+" puede morir"
        else:
            return self.nombre+" esta fuera de peligro"
    
    def necesitaOperar(self):
        if self.estaEnPeligro == True:
            return self.nombre+" Necesita operacion"
        else:
            return self.nombre+" No necesita operacion"

class Duenio(Mascota):

    nombre = ""
    edad = 0
    telefono=""
    genero =""
    correo=""

    def __init__(self, nombre, edad, telefono, genero, correo):
        self.nombre=nombre
        self.edad = edad
        self.telefono = telefono
        self.genero = genero
        self.correo = correo 
        super().__init__(nombre,edad,"Perro", genero, "raza")

    def mayorEdad(self):
        if self.edad >= 18:
            return self.nombre+"Es mayor de edad"
        else:
            return self.nombre+"Es menor de edad"
    def nombreMascota(self):
        return "Nombre mascota: Pepito"+super().nombre
    def tieneDinero(self,pDinero):
        if pDinero == "si":
            return "El dueño si tiene dinero"
        else:
            return "El dueño no tiene dinero"
    
class Consulta:
    especialista =""
    costo = 0
    paciente = ""
    Herramientas = ""
    consultorio = ""

    def __init__(self,especialista,costo,paciente,Herramientas,consultorio):
        self.especialista = especialista
        self.costo =costo
        self.paciente = paciente
        self.Herramientas = Herramientas
        self.consultorio = consultorio

    def darCostoTotal(self):
        cst = Mascota
        if cst.estaEnPeligro == True:
            return self.costo+3000
        else:
            return self.costo
    def darReporte(self):
        return("-------------REPORTE---------------"+"\n"+"Nombre especialista: "+self.especialista +"\n"+ "Costo consulta: "+str(self.darCostoTotal())+"\n"+"paciente: "+self.paciente+"\n"+"Herramientas: "+self.Herramientas
        +"\n"+"Consultorio: "+ self.consultorio)
    def necesitaMedicamento(self, pMedicamento):
        if pMedicamento == "si":
            return "El paciente necesita medicamentos"
        else:
            return "El paciente no necesita medicamentos"

class Medicamento:
    fechaVencimiento = ""
    nombre = ""
    farmacia = ""
    precio = 0
    cantidad = 0

    def __init__(self,fechaVencimiento,nombre,farmacia,precio,cantidad):
        self.fechaVencimiento = datetime.now() + timedelta(days=2)
        self.nombre =nombre
        self.farmacia = farmacia
        self.precio = precio
        self.cantidad = cantidad

    def estaVencido(self):
        now = datetime.now()
        new_date = now + timedelta(days=2)
        print ("Fecha de Vencimiento: ")
        print(new_date)
        if now < new_date:
            return "El medicamento no esta vencido"
        else:
            return "El medicamento esta vencido"



    def darReporte(self):
        return("-------------REPORTE MEDICAMENTO---------------"+"\n"+"Nombre medicamento: "+self.nombre +"\n"+ "Farmacia: "+self.farmacia+"\n"+"Precio: "+str(self.precio)
        +"\n"+"cantidad: "+ str(self.cantidad)+" gramos.")
    def necesitaMedicamento(self, pMedicamento):
        if pMedicamento == "si":
            return "El paciente necesita medicamentos"
        else:
            return "El paciente no necesita medicamentos"

    

print("_____________________CLASE VETERINARIA_____________________")    
vt1 = Veterninaria("Maxdog","calle 10 #24 a 50",3147290203)
vt1.setAsensor(input("subir asensor? "))
print(vt1.subirAsensor())
vt1.setPuerta(input("abrir puerta? "))
print(vt1.abrirPuerta())
print(vt1.hacerLlamada(int(input("digite el telefono: "))))

print("_____________________-CLASE MASCOTA________________________")    
msc1 = Mascota("Pepito",3,"Perro","Macho","labrador")
msc1.setEstaEnPeligro(input("Esta en peligro? "))
print (msc1.darEstaEnPeligro())
print (msc1.necesitaOperar())
print (msc1.mayorEdad())

print("-_____________________CLASE DUENIO________________________") 
dno = Duenio("Juan Simarrones ",19,31522302,"Hombre","JP@gmai.com")
print(dno.mayorEdad())
print(dno.nombreMascota())
print(dno.tieneDinero("si"))

print("______________________CLASE CONSULTA_______________________")    
cnslt = Consulta("Dr. Herrera23",str(1000),"Pepito","visturi, entre otros","calle 20 #21 - 50")
print("Costo: " +cnslt.darCostoTotal())
print(cnslt.darReporte())
print(cnslt.necesitaMedicamento("no"))

print("______________________CLASE MEDICAMENTO_______________________")    
mdcm = Medicamento(date.today(),"Amoxasilina","Drgas la rebaja",25.000,25)
print(mdcm.estaVencido())
print(mdcm.darReporte())
print("No se me ocurre un metodo con parametros jajaja")