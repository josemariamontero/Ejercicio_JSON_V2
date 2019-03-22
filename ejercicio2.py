import json
with open('movies.json','r') as fichero:
	doc = json.load(fichero)

contador = 0

for i in doc:
	titulo = i["title"]
	actores = i["actors"]
	print ("Pelicula: %s ; Número de actores: %s" % (titulo,len(actores)))
