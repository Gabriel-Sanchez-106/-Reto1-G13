"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time as t

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar videos destacados por país, categoria y cantidad")
    print("3- Consultar el video más famoso por país")
    print("4- Consultar el video más famoso por categoria")
    print("5- Consultar videos con más likes por país y etiqueta")
    print("0- Salir")

def initCatalog():
    return controller.initCatalog()

def loadData(catalog, ids):
    return controller.loadData(catalog, ids)

def initId():
    return controller.initId()

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog=initCatalog()
        ids=initId()

        loadData(catalog,ids)

        print('Registros de videos cargados: ' + str(lt.size(catalog['title'])))
        print('Primer video: ' + str(controller.getfd(catalog)))
        print('Categorias: ' + str(ids))


    elif int(inputs[0]) == 2:
        category=str(input("Escriba la categoria que le interesa"))
        country=str(input("Ecriba el nombre del país"))
        n=int(input("Ingrese el número de videos que desea conocer"))

        ans=controller.getbestbyccn(catalog,category, country, n)
        print(ans)

    elif int(inputs[0]) == 3:
        country=str(input("Ecriba el nombre del país"))

        ans=controller.getbestbycountry(catalog, country)
        print(ans)

    elif int(inputs[0]) == 4:
        category=str(input("Ecriba la categoria que le interesa"))

        ans=controller.getbestbycategory(catalog,category)
        print(ans)
    
    elif int(inputs[0]) == 5:
        tag=str(input("Escriba la etiqueta(tag) de su interés"))
        n=int(input("Ingrese el numero de videos que desea conocer"))
        
        ans=controller.getbytag(catalog, tag, n)
        print(ans)

    else:
        sys.exit(0)
sys.exit(0)