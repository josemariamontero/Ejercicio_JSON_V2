import json
with open('movies.json','r') as fichero:
	doc = json.load(fichero)

indicador = False

fecha = input("Dime una fecha de estreno: ")
fecha2 = input("Dime otra fecha de estreno: ")

for i in doc:
	titulo = i["title"]
	poster = i["posterurl"]
	puntuacion = i["ratings"]
	estreno = i["releaseDate"]
	media = round(sum(puntuacion) / len(puntuacion))
	if fecha <= estreno and fecha2 >= estreno:
		indicador = True
		print ("Titulo:",titulo)
		print ("Media:",media)
		print ("Poster:",poster)

if not indicador:
	print("No hay peliculas entre las fechas dadas")

#1968-04-10
#1999-12-25