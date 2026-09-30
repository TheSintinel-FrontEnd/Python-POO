import re

#Detectando un numero de CABA  y ocultandolo

texto = "Hola mi, numero es: +54 11 1234-1234"

pattern = r"\+\d{2}\s\d{2}\s\d{4}-\d{4}"

reeplazo = re.sub (pattern,"(Numero oculto)",texto)

print(reeplazo)