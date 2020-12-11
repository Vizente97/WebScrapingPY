import requests
import os

contenido = requests.get("https://es.python-requests.org/es/latest/user/quickstart.html")
print (contenido.headers)

file = open("ArchivoHTML.txt", "w")
file.write(str(contenido.content, 'utf-8'))
file.close()