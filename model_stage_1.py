# -*- coding: utf-8 -*-
"""model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/fancagi/timetabling_upb/blob/main/model.ipynb
"""

import pandas as pd
import pulp as plp
import json

"""# read data"""

horas_curso=json.loads(open('data/horas_curso.json').read())
idoneidad=json.loads(open('data/idoneidad.json').read())
horas_reglamento=json.loads(open('data/horas_reglamento.json').read())
labor_instruccional=json.loads(open('data/labor_instruccional.json').read())
grupo_requerimiento=json.loads(open('data/grupo_requerimiento.json').read())
ubicacion_semestral=json.loads(open('data/ubicacion_semestral.json').read())

L={str(i):[str(grupo_requerimiento[i]['codigo'])+'-'+str(j) for j in range(grupo_requerimiento[i]['n_grupos'])] for i in grupo_requerimiento.keys()}
curso_base={str(i)+"-"+str(j):str(i)  for i in grupo_requerimiento.keys() for j in range(grupo_requerimiento[i]['n_grupos']) }

grupos=[]
for l in L.values():
    for ele in l:
        grupos.append(ele)

"""# Modelo"""

# Conjuntos

I=set(idoneidad.keys()) # Profesores
J=set(grupos) # Grupos
K=set(grupo_requerimiento.keys()) # Cursos
# Conjunto auxiliar que sirve para enumerar la cantidad de cursos que un docente tiene asignados
C=set(range(1,7)) # Posibles valores para el número de clases en un semestre asignadas a un docente

# combinaciones posibles de profesores ygrupo
tuplas=[(i,j) for i in I for j in J if i in idoneidad.keys() and curso_base[j] in idoneidad[i]['idoneidad'] ]
# subindices usados para denotar la carga asignada a un profesor
doc_carga=[(i,c) for i in I for c in C]
# tuplas profesor y curso
prof_curso=[(i,j) for i in I for j in idoneidad[i]['idoneidad'].keys()]

"""# Modelo

## Declaración de variables
"""

import pulp as plp

# Create the 'prob' variable to contain the problem data
prob = plp.LpProblem("Modelo William", plp.LpMaximize)

# Create problem variables from dictionary
# Docente i es asignado a grupo j (binaria)
x=plp.LpVariable.dicts("x",tuplas,0,1,plp.LpBinary)

# Docente i es asignado a c cursos diferentes
N=plp.LpVariable.dicts("N",doc_carga,0,1,plp.LpBinary)

# Un profesor es asignado a un curso
z=plp.LpVariable.dicts("z",prof_curso,0,1,plp.LpBinary)

"""## Funcion objetivo 1
 maximizar la suma de la idoneidad de los profesores asignados a los diferentes grupos


"""

# e=(i,j) representa la tupla
prob+=plp.lpSum([x[(i,j)]*idoneidad[i]['idoneidad'][curso_base[j]] for (i,j) in tuplas])

"""### Restricciones"""

# restriccion 1
cursos_excluir=['8833-0022','8833-0083','8833-0101','5568-0011','5562-0013']
# Cada curso tiene un docente asignado
for j in J:

    #

    if curso_base[j] not in cursos_excluir:
        prob+=plp.lpSum([x[i,j] for i in I if (i,j) in tuplas])==1,"asignacion curso %s"%j

        prob.solve(solver=plp.PULP_CBC_CMD(msg=0))
        if prob.status==-1:
            print("El problema es infactible")
            print(plp.lpSum([x[i,j] for i in I if (i,j) in tuplas])==1,"asignacion curso %s"%j)
            break

# Contar cuantos cursos diferentes da un profesor
for i in I:
    prob+=plp.lpSum([z[(i,k)] for k in K if (i,k) in prof_curso])==plp.lpSum([l*N[i,l] for l in C])
# el profesor tiene una cantidad de cursos asignada
for i in I:
    prob+=plp.lpSum([N[i,l] for l in C])==1

# el profesor no puede dar mas cursos de los que tiene asignados
for i in I:
    for k in K:
        if (i,k) in prof_curso:
            plp.lpSum([x[(i,j)] for j in L[k] if (i,j) in tuplas])<=z[(i,k)]*len(L[k])

prob.solve()


for (i,j) in tuplas:
    if x[(i,j)].value()>0.5:
        try:
            print(i,j,curso_base[j],labor_instruccional[i]['docente'],horas_curso[curso_base[j]]["ASIGNATURA"])
        except:
            print(i,j,curso_base[j])