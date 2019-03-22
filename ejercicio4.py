import json
with open('movies.json','r') as fichero:
	doc = json.load(fichero)

indicador = False

actor = input("Dime el nombre de un actor: ")

for i in doc:
	titulo = i["title"]
	actores = i["actors"]
	if actor in actores:
		indicador = True
		print (titulo)
if not indicador:
	print ("No existe ese actor")