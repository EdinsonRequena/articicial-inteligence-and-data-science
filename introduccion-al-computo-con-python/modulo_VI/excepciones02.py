"""

Tema: Manejo de excepciones y uso de afirmaciones.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

def primera_letra(lista_de_palabras):
    primeras_letras = []
    
    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'no se permiten srt vacios'
        
        primeras_letras.append(palabra[0])
            
    return primeras_letras

if __name__ == '__main__':
    hola = 'hola'
    lista_de_palabras = [hola]
    
    print(primera_letra(lista_de_palabras))