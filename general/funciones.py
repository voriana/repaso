#funcion suma elementos de un arreglo

def sum_valores(lista):
    sum=0
    for elem in lista:
        sum+=elem
    return sum
    

arreglo=[2,5,7,9]
print(sum_valores(arreglo))


