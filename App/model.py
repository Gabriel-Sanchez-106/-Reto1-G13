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
from DISClib.Algorithms.Sorting import mergesort as sa
from DISClib.Algorithms.Sorting import quicksort as qs


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
        'tags'  : None,
        'ids'   : None, }
    
    catalog['videos']=lt.newList('LINKED_LIST')
    catalog['tags']={}
    catalog['ids']={}


    return catalog
## ids to list

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video)->None:
     cv=catalog['videos']
     data={'title','channel_title','country','publish_time','trending_date','category_id','views','likes','dislikes', 'tags'}
     sub={}

     for i in data:
         value=video[i]
         sub[i]=value

         if i=='tags':
             datagsthing(value, catalog, video['title'])
        
     lt.addLast(cv, sub)


def addId(catalog, row)->None:
    row=row[0].split('\t')
    i=row[0]
    n=row[1]
    n=n.lower().strip()
    ci=catalog['ids']
    
    ci[i]=n

def datagsthing(value,catalog, name):
    name=name.strip().lower()
    tags=catalog['tags']
    main=value.split('|')

    for i in main:

        if not i in tags: 
            tags[i]=lt.newList()
            lt.addLast(tags[i], name)
        
        else:
            lt.addLast(tags[i], name)

# Funciones para creacion de datos
def f_rq1(cv, country, id)->list:
    card=lt.size(cv)
    p=1
    c=country.lower()
    ans=lt.newList()

    while p<=card:
        e=lt.getElement(cv, p)
        ec=str(e['country'])
        ei=int(e['category_id'])
        a=dict(title=e['title'], channel_title=e['channel_title'],publish_time=e['publish_time'],
                    views=e['views'], likes=e['likes'], dislikes=e['dislikes'], trending_date=e['trending_date'])


        if ec.lower()==c and ei==id:
            lt.addLast(ans, a)

        p+=1
    return ans

def f_rq2(cv, country):
    p=1
    c=country.lower()
    ans=lt.newList()

    while p<=lt.size(cv):
        e=lt.getElement(cv,p)
        ec=str(e['country'])
        a=dict(title=e['title'], channel_title=e['channel_title'], country=e['country'])

        if ec.lower()==c:
            lt.addLast(ans,a)
        
        p+=1
    return ans

def f_rq3(cv,id):
    p=1
    ans=lt.newList()

    while p<=lt.size(cv):
        e=lt.getElement(cv,p)
        ei=int(e['category_id'])
        a=a=dict(title=e['title'], channel_title=e['channel_title'], category_id=e['category_id'])

        if ei==id:
            lt.addLast(ans,a)
        
        p+=1
    return ans

def f_rq4(cv, titles,country):
    p=1
    ans=lt.newList()
    c=country.lower()

    while p<=lt.size(cv):
        e=lt.getElement(cv,p)
        et=str(e['title'])
        ec=str(e['country'])
        et=et.strip().lower()
        a=dict(title=e['title'], channel_title=e['channel_title'],publish_time=e['publish_time'],
                    views=e['views'], likes=e['likes'], dislikes=e['dislikes'], tags=e['tags'])

        if lt.isPresent(titles, et)>0 and ec.lower()==c:
            lt.addLast(ans, a)
        
        p+=1
    return ans

def counting_days(cv)->list: 
    titles={}
    p=1

    while p<=lt.size(cv):
        t=list(titles.keys())
        e=lt.getElement(cv, p)
        et=e['title']
        
        if (et in t)==False:
            titles[et]=1
        else:
            titles[et]+=1

        p+=1
    return titles

def find(cv, title):
    p=1

    while p<=lt.size(cv):
        e=lt.getElement(cv,p)
        t=e['title']

        if t==title:
            return p

        p+=1

def acotador(cv,mini):
    titles=list(mini.keys())
    p=0
    ans=lt.newList()

    while p<len(titles):
        t=titles[p]
        k=find(cv,t)
        e=lt.getElement(cv,k)
        e['trending_days']=mini[t]

        lt.addLast(ans, e)
        p+=1
    return ans

# Funciones de consulta

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

def cmpVideosByTrend(video1, video2)->bool:
    return (float(video1['trending_days']) > float(video2['trending_days']))

def cmpVideosByLikes(video1, video2)->bool:
    return (float(video1['likes']) > float(video2['likes']))

# Funciones de ordenamiento
def dataim(mini,k)->float:

    t1=t.perf_counter()
    qs.sort(mini, cmpVideosByViews)
    t2=t.perf_counter()

    main=(t2-t1)*1000
    return main

def reque1(catalog, country, id)->list:
    cv=catalog['videos']
    dans=f_rq1(cv,country,id)

    t1=t.process_time()
    ans=sa.sort(dans, cmpVideosByViews)
    t2=t.process_time()
    tans=(t2-t1)*100
    
    a=(ans, tans)
    return a 

def reque2(catalog,country):
    cv=catalog['videos']
    dans=f_rq2(cv,country)
    mini=counting_days(dans)
    dans=acotador(dans,mini)

    t1=t.process_time()
    ans=sa.sort(dans, cmpVideosByTrend)
    t2=t.process_time()
    ans=lt.firstElement(ans)
    tans=(t2-t1)*100
    
    a=(ans, tans)
    return a

def reque3(catalog,id):
    cv=catalog['videos']
    dans=f_rq3(cv,id)
    mini=counting_days(dans)
    dans=acotador(dans,mini)

    t1=t.process_time()
    ans=sa.sort(dans, cmpVideosByTrend)
    t2=t.process_time()
    ans=lt.firstElement(ans)
    tans=(t2-t1)*100
    
    a=(ans, tans)
    return a

def reque4(catalog, tag, country):
    cv=catalog['videos']
    tags=catalog['tags']
    titles=tags[tag]
    dans=f_rq4(cv, titles, country)

    t1=t.process_time()
    ans=sa.sort(dans, cmpVideosByLikes)
    t2=t.process_time()
    tans=(t2-t1)*100
    
    a=(ans, tans)
    return a