"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv
from DISClib.ADT import list as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    catalog=model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    loadVids(catalog)
    loadIds(catalog)

def loadVids(catalog):
    vfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(vfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadIds(catalog):
    ifile = cf.data_dir + 'category-id.csv'
    input_file =csv.reader(open(ifile, encoding='utf-8'))

    for row in input_file:
        model.addId(catalog,row)
    
def print_inf2(sorted_cv, n)->None:
    p=1

    while p<=n:
        a=lt.getElement(sorted_cv, p)
        print(a['trending_date'], a['title'], a['channel_title'],a['publish_time'], a['views'], a['likes'], a['dislikes'])

        p+=1
    
# Funciones de ordenamiento
def insertsortbv(catalog,country,id)->list:
    return model.insertsortbv(catalog, country, id)

def selectionsortbv(cv, country, id)->list:
    return model.selectionsortbv(cv, country, id)

def shellsortbv(cv, country, id)->list:
    return model.shellsortbv(cv, country, id)


def getbestbyccn(catalog,category,country):
    id=model.nametid(catalog,category)
    ans=insertsortbv(catalog, country, id)

    return ans

# Funciones de consulta sobre el catálogo

def veryveryverylazy(catalog)->None:
    main=catalog['videos'].copy()

    c1=   lt.subList(main, 1, 1000)
    c2=   lt.subList(main, 1, 2000)
    c4=   lt.subList(main, 1, 4000)
    c8=   lt.subList(main, 1, 8000)
    c16=  lt.subList(main, 1, 16000)
    c32=  lt.subList(main, 1, 32000)
    c64=  lt.subList(main, 1, 64000)
    c128= lt.subList(main, 1, 128000)
    c256= lt.subList(main, 1, 256000)

    minis=[c1, c2, c4, c8, c16, c32, c64, c128, c256]

    for mini in minis:
        ma=model.dataim(mini)
        print (ma)