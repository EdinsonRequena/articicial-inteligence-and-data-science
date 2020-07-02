"""
Tema: Algoritmos de busqueda y ordenamiento - Ordenamiento por Inserccion.
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.
"""

def insertion_sort(arr): 

    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 

        key = arr[i] 

        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

if __name__ == '__main__':
    # Driver code to test above 
    arr = [12, 11, 13, 5, 6] 
    insertion_sort(arr) 
    print ("Sorted array is:") 
    for i in range(len(arr)): 
        print (arr[i]) 