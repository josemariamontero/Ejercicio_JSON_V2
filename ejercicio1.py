import json
with open('movies.json','r') as fichero:
	doc = json.load(fichero)
	#print(doc)

for i in doc:
	titulo = i["title"]
	año = i["year"]	
	duracion = i["duration"]
	print ("Titulo: %s, Año: %s, Duracion: %s" % (titulo,año,duracion))
