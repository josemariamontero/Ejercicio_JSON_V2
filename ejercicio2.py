import json
with open('movies.json','r') as fichero:
	doc = json.load(fichero)

for i in doc:
	titulo = i["title"]
	actores = i["actors"]
	print ("Pelicula: %s ; Número de actores: %s" % (titulo,len(actores)))
