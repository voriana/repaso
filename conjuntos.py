#definicion de conjuntos
#no mantienen un orden (no tienen indices)

conj={9,7,5}
conj2={3,5,3,1} # no permite almacenar elementos repetidos
print(conj2)

#convertir una lista en un conjunto (set)
list=[3,4,5]
conj3= set(list)
print(type(conj3))

#agregar o eliminar un elemento al conjunto
conj.add("materia")
conj2.remove(3)
print(conj)


#matematicas de conjuntos
conj4= conj.union(conj2).union(conj3)
print(conj4)

#recorrer un conjunto
for elem in conj4:
    print(elem)

#buscar elemento en un conjunto
if (5 in conj4):
    print("elemento encontrado")

print(conj4.intersection(conj))

