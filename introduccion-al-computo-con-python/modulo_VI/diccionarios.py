"""

Tema: Diccionarios.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

capitales = {
    'Venezuela': 'Caracas',
    'Colombia': 'Bogota',
    'Argentina': 'Cordova',
    'Canada': 'Ottawa'
}
print(capitales)
print(capitales['Venezuela']) # Nos devuelve el valor de Venzuela
print(capitales['Argentina']) # Nos devuelve el valor de Argentina

print(capitales.get('Mexico')) # Nos devuelve None
print(capitales.get('Mexico', 'Ciudad de Mexico')) # Nos devuelve Ciudad de Mexico

a = 'Buenos Aires'
capitales['Argentina'] = a # Modificamos el valor de llave Argentina y le pasamos el valor de la variable a
print(capitales)

capitales['Peru'] = 'Lima' # Le agregamos la llave Peru con el valor Lima al diccionario
print(capitales)

del capitales['Canada'] # Eliminamos la llave Canada
print(capitales)

#del capitales['Lima'] # Esto nos dara error, porque no hay una llave llamada Lima
#print(capitales)

del capitales['Peru'] # Aca eliminamos la llave Peru y por ende se elimina su valor; peru
print(capitales)

for key in capitales.keys(): # Iteramos en las todas las llaves de capitales
    print(key) # Imprimimos las llaves

for value in capitales.values(): # Iteramos en todos los valores de capitales
    print(value) # Imprimimos todos los valores de capitales