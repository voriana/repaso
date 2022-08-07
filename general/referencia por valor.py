d = [0, 1, 2, 3, 4, 5, 6]
#e = d.copy() por referencia
e = d #por valor
e[-1] = 50
d[2] = 40
print(d)