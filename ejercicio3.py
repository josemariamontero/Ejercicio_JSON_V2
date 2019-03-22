import json
with open('movies.json','r') as fichero:
	doc = json.load(fichero)

indicador = False

cadena = input("Dime una cadenas para buscar una sinopsis: ")

for i in doc:
	sinopsis = i["storyline"]
	if cadena in sinopsis:
		indicador = True
		print (sinopsis)
if not indicador:
	print ("No existe ninguna sinopsis con esa cadena dada")