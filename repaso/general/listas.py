
cadena = " anita lava la tina  "
tmp = []
for c in cadena:
    tmp.append(c)
tmp.reverse()
nuevaCadena = "".join(tmp)
print (nuevaCadena)

#starwith , devuele true o false si la cadena empiezar por..

print(cadena.strip().startswith("anita"))

#strip quita los espacios
print(cadena.strip())
