import json
with open('movies.json','r') as fichero:
	doc = json.load(fichero)

indicador = False

cadena = input("Dime una cadena para buscar una sinopsis: ")
cadena2 = input("Dime otra cadena para buscar una sinopsis: ")

for i in doc:
	sinopsis = i["storyline"]
	if cadena in sinopsis and cadena2 in sinopsis:
		indicador = True
		print (i["title"])
if not indicador:
	print ("No existe ninguna sinopsis con esa cadena dada")