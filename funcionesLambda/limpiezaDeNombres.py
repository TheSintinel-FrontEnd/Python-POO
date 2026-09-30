# Dada la siguiente lista de nombres desprolijos: nombres = [" juan", "MAría ", " peDro ", "aNa"] Usá
# map() junto con una función lambda para generar una nueva lista donde todos los nombres
# estén sin espacios extra y con la primera letra en mayúscula (formato Título).


nombres = ["juan", "MAría", "peDro", "aNa"]


nombresProlijos = list(map(lambda s: s.strip().title(), nombres))


print(nombresProlijos)

