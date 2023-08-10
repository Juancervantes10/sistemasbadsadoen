from random import choice
from sistemadereglas import*
import json

graph={}
data = {}
data ['Datos'] = [] 


engine = sistemadereglas()


engine.reset()


def verifyFile(): 
    try:
        with open ('data.json') as file:
            return True     
    except FileNotFoundError as e:
        return False
    
def verifyFileLogin():
    try:
        with open ('login.json') as file:
            return True     
    except FileNotFoundError as e:
        return False

def preguntas(v_nombre):
    v_identificacion = int(input("Digite su numero de identeficación: \n"))  
    v_cepillarse = input("se cepilla a diario? \n si :  \n no :\n ")
    engine.declare(reglas(cepillare=choice([str(v_cepillarse)])))

    v_enjuage_bucal = input("se enjuaga la boca cuando se cepilla? \n si :  \n no : \n ")
    engine.declare(reglas(enjuage=choice([str(v_enjuage_bucal)])))

    v_obs = input("tiene alguna obsesion al cepillarse los dientes? \n si :  \n no : \n ")
    engine.declare(reglas(obs=choice([str(v_obs)])))

    v_mes= input("se cepilla los dientes todos los dias del mes? \n si :  \n no :\n ")
    engine.declare(reglas(mes=choice([str(v_mes)])))

    v_cepi = input("Todas las semanas utiliza ceda dental? \n si :  \n no :\n ")
    engine.declare(reglas(cepi=choice([str(v_cepi)])))

    def fillJson():
        diccionario = {
            'Id': v_identificacion,
            'Nombre': v_nombre,
            'Preguntas' : ['se cepilla a diario?', 'se enjuaga la boca cuando se cepilla?', 'tiene alguna obsesion al cepillarse los dientes?', 'se cepilla los dientes todos los dias del mes?', 'Todas las semanas utiliza ceda dental?'],
            'Respuesta': [v_cepillarse, v_enjuage_bucal, v_obs, v_mes, v_cepi]}
        return diccionario

    def dataJson():
        if verifyFile() == True:
            with open ("data.json") as file:
                datos = json.load(file)
            datos['Datos'].append(fillJson())

            with open("data.json", 'w') as newFile:
                json.dump(datos, newFile)
        else:
            with open("data.json", 'w') as newFile:
                data['Datos'].append(fillJson())
                json.dump(data, newFile)
    engine.run()
    dataJson()
    
def buscarPorId(buscarId):
    if (verifyFile()):
        with open ("data.json") as file:
                datos = json.load(file)
                for key in datos:
                    value = datos[key]
                    for i in range(len(value)):
                        item = value[i]
                        if (item['Id'] == buscarId):
                            datos = ('Nombre, ', item['Nombre'], 'Preguntas: ', item['Preguntas'], 'Respuestas ', item['Respuesta'])
                            print (datos)
                            return datos
                        elif (i == len(value)-1):
                            return "Id no encontrado"
    else:
        print("No existe ningun archivo JSON")

def inicio():    
  
    v_nombre = input("Digite su nombre por favor: \n")
    Menu = True
    while Menu == True:
     n = int(input("Hola "+v_nombre+", Bienvenid@! \n -------Menú-------\n 1. Utilizar sistema de reglas. \n 2. Consultar Historial. \n 3. Salir \n"))

     if (n == 1):
        preguntas(v_nombre)
     elif (n == 2):
        n2 = int(input(" -------Menú-------\n 1. Consultar Historial por usuario. \n"))
        if (n2):
            id = int(input("Digite su ID: \n"))
            buscarPorId(id)
     else:
        print("¡Gracias por utilizar nuestro programa, espero verte pronto!")
        exit()

def login(id, contrasena):    
    if (verifyFileLogin()):
        with open ("login.json") as file:
                datos = json.load(file)
                for key in datos:
                    value = datos[key]
                    for i in range(len(value)):
                        item = value[i]
                        if (item['Id'] == id and item['Contrasena'] == contrasena):
                            print("Bienvenido "+ item['Nombre'])
                            inicio()
                        elif (i == len(value)-1):
                            return ("El usuario "+ usuario + "no se encuentra registrado")
    else:
        print("No existe ningun archivo JSON")

print("Hola, te damos la bienvenida a nuestro programa.\nPara iniciar sesión necesitmos su número de indentificación y su contraseña.")
usuario = int(input("Digite su Identificación \n"))
contrasena = input("Digite su contrasena \n")
login(usuario, contrasena)