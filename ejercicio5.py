import json
with open('movies.json','r') as fichero:
	doc = json.load(fichero)

for i in doc:
	titulo = i["title"]
	poster = i["posterurl"]
	puntuacion = i["ratings"]
	media = sum(puntuacion) / len(puntuacion)
	print (titulo,media)