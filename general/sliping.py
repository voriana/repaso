from posixpath import split


b = "Hello, World!"
print(b[-5:-1])

c="Departamento en Alquiler en Ramos Mejia, La Matanza"
c="Departamento en Alquiler en Villa Devoto, Capital Federal"
#d= c[:c.find(" ")]
d= c.split(",")[0]
print(d)