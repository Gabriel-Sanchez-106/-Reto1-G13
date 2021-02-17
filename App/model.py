﻿"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
#Lo

def newCatalog():
    catalog= {
        'title'        : None,
        'channel_title': None,
        'country'      : None,
        'publish_time' : None,
        'trending_date': None,
        'category_id'  : None,
        'views'        : None,
        'likes'        : None,
        'dislikes'     : None,
        'tags'         : None   }
    
    catalog['title']=lt.newList()
    catalog['channel_title']=lt.newList()
    catalog['country']=lt.newList()
    catalog['publish_time']=lt.newList()
    catalog['trending_date']=lt.newList()
    catalog['category_id']=lt.newList()
    catalog['views']=lt.newList()
    catalog['likes']=lt.newList()
    catalog['dislikes']=lt.newList()
    catalog['tags']=lt.newList()
    
    return catalog

def newId():
    id={}
    return id

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
     data={'title','channel_title','country','publish_time','trending_date','category_id','views','likes','dislikes'}

     for i in data:
         key=catalog[i]
         value=video[i]
         lt.addLast(catalog[i], video[i])


def addId(ids,row):
    row=row[0].split('\t')
    id=row[0]
    name=row[1]

    ids[id]=name
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento