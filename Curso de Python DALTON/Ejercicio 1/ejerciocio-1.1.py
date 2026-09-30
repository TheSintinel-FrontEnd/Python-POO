
#Dastos de duracion

otros_cursos_min = 2.5
otros_cursos_max = 7.0
otros_cursos_prom = 4
dalto_curso = 1.5

#Diferencia de duracion

diferencia_con_min = 100 - (dalto_curso / otros_cursos_min *100)

#Agrego ceros y luego se los quito para redondear hacia abajo, con el 1000 agregro y con el 10 quito
diferencia_con_max = round(8.000-(dalto_curso / otros_cursos_max ),2) 


diferencia_con_prom = 100 - (dalto_curso / otros_cursos_prom *100)

print("-----------------------------------")

print(f"Este curso dura menos de un {diferencia_con_min}% que el curso más rapido")

print(f"Este curso dura menos de un {diferencia_con_max}% que otros curso más lento")

print(f"Este curso dura menos de un {diferencia_con_prom}% que el curso pomedio")


#Tiempo de duracion en crudo (vacio)

cusos_prom_vacio = 5
curso_dalto_vacio = 3.5

#calculado el tiempo vacio

t_vacio_prom = 100 - otros_cursos_prom * 1000 // cusos_prom_vacio / 10
t_dalto_crudo = 100 - dalto_curso *1000 // curso_dalto_vacio / 10

print("-----------------------------------")
print(f"Un curso promedio elimina un  {t_vacio_prom}% del tiempo vacio")

print(f"El cruso de dalto elimina un  {t_dalto_crudo}% del tiempo vacio")
print("-----------------------------------")
#print(f"timepo vacio promedio{t_vacio_prom}%")

#print(f"timepo vacio promedio{t_vacio_prom}%")

#C) Mostrando diferencias entre si los cusos duraran 10 horas


print(f"Ver 10 horas de este curso equivalen  a ver { otros_cursos_prom *100 // dalto_curso /10}  horas de otros cursos")

print(f"Ver 10 horas de otros curso equivalen  a ver { dalto_curso *100 // otros_cursos_prom /10}  horas de otros cursos")
print("-----------------------------------")