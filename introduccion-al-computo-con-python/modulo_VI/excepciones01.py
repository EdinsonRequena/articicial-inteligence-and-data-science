"""

Tema: Manejo de excepciones y uso del principio EAFP 
(easier to ask for forgiveness than permission, es más fácil pedir perdón que permiso, por sus siglas en inglés)..
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

def busca_pais(paises, pais):
    """
    Paises es un diccionario. Pais es la llave.
    Codigo con el principio EAFP.

    """
    error = "El dato ingesado no existe"
    try:
        return paises[pais]
    except KeyError:
        return error

paises = {
    'Venezuela': 'Caracas',
    'Colombia': 'Bogota',
    'Argentina': 'Cordova',
    'Canada': 'Ottawa'
}

if __name__ == '__main__':
    print(busca_pais(paises, 'Venezuela'))
    print(busca_pais(paises, 'Colombia'))
    print(busca_pais(paises, 'Italia'))