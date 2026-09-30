ingreso_mensual = 15000
grato_mensual = 5000

#Ejemplos de if anidados y el-if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - grato_mensual < 0: # No queda plata
        print("Estas en deficit, gastas más de lo que te pagan")
    elif ingreso_mensual - grato_mensual > 11000:  # Queda algo de plata
        print("Estas muy bien, te queda plata ")
    else:
        print("Estas en regla, no gastas demaciado, pero tene cuidado") # No queda mucha plata
    
elif ingreso_mensual >1000:  # En python el if  == elif 
    print("Estas bien en latam")

elif ingreso_mensual >500:
    print("Estas bien en Argentina pa")

elif ingreso_mensual >200:
    print("Estas bien en venezuela")

else:
    print("Sos pobre")


