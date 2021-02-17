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

def initId():
    id=model.newId()
    return id

# Funciones para la carga de datos

def loadData(catalog,ids):
    loadVids(catalog)
    loadIds(ids)

def loadVids(catalog):
    vfile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(vfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadIds(ids):
    ifile = cf.data_dir + 'category-id.csv'
    input_file =csv.reader(open(ifile, encoding='utf-8'))

    for row in input_file:
        model.addId(ids,row)
    
    
# Funciones de ordenamiento

def getfd(catalog):
    data={'title','channel_title','trending_date','country','views','likes','dislikes'}
    a=[]

    for i in data:
        var=lt.firstElement(catalog[i])
        a.append(var)
    return a
# Funciones de consulta sobre el catálogo
