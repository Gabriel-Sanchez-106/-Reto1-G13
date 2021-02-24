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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time as t
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ir
from DISClib.Algorithms.Sorting import selectionsort as ss

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
#Lo

def newCatalog()->dict:
    catalog= {
        'videos': None,
        'ids':    None, }
    
    catalog['videos']=lt.newList('LINKED_LIST')
    catalog['ids']={}

    return catalog
## ids to list

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video)->None:
     cv=catalog['videos']
     data={'title','channel_title','country','publish_time','trending_date','category_id','views','likes','dislikes', 'tags'}
     sub={}

     for i in data:
         value=video[i].lower()
         sub[i]=value
        
     lt.addLast(cv, sub)


def addId(catalog, row)->None:
    row=row[0].split('\t')
    i=row[0]
    n=row[1]
    n=n.lower().strip()
    ci=catalog['ids']
    
    ci[i]=n

# Funciones para creacion de datos
def cutcv(cv, country, id)->list:
    card=lt.size(cv)
    p=0
    c=country.lower()
    ans=lt.newList()

    while p<=card:
        e=lt.getElement(cv, p)
        ec=str(e['country'])
        ei=int(e['category_id'])

        if c!= None and id!=None: 
            if ec==c and ei==id: 
                lt.addLast(ans, e)
        
        elif c==None:
            if ei==id: 
                lt.addLast(ans, e)

        elif id==None:
            if c==ec: 
                lt.addLast(ans, e)
        
        p+=1

    return ans

def egein(sorted_cv, n)->list:
    a=lt.newList()

    p=0
    while p<n:
        element=lt.getElement(sorted_cv,p)
        lt.addLast(a,element)

        p+=1
    return a

# Funciones de consulta

def getviews(cv, pos)->int:
    num=cv[pos]['views']
    return num

def idtname(catalog, id)->str:
    i=catalog['ids']
    n=i[id]
    return str(n)

def nametid(catalog, name)->int:
    i=catalog['ids']
    k=list(i.keys())
    v=list(i.values())
    n=name.lower()
    a=v.index(n)

    return int(k[a])

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByViews(video1, video2)->bool:
    return (float(video1['views']) > float(video2['views']))


# Funciones de ordenamiento
def dataim(mini)->float:
    t1=t.perf_counter()
    ir.sort(mini, cmpVideosByViews)
    t2=t.perf_counter()
    main=(t2-t1)*1000

    return main


def insertsortbv(catalog, country, id)->list:
    cv=catalog['videos']
    dans=cutcv(cv,country,id)

    t1=t.process_time()
    ans=ir.sort(dans, cmpVideosByViews)
    t2=t.process_time()
    tans=(t2-t1)*1000
    
    a=(ans, tans)
    return a 


def selectionsortbv(catalog, country, id)->list:
    cv=catalog['videos']
    dans=cutcv(cv,country,id)

    t1=t.process_time()
    ans=ss.sort(dans, cmpVideosByViews)
    t2=t.process_time()
    tans=(t2-t1)*1000
    
    a=(ans, tans)
    return a 


def shellsortbv(catalog, country, id)->list:
    cv=catalog['videos']
    dans=cutcv(cv,country,id)

    t1=t.process_time()
    ans=sa.sort(dans, cmpVideosByViews)
    t2=t.process_time()
    tans=(t2-t1)*1000
    
    a=(ans, tans)
    return a 

