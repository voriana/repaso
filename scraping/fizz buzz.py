num = int(input("Ingrese un numero"))

# hago un bucle hasta el numero que me pasan

for i in range(num):
    if i % 2 == 0:
        continue
    elif i % 3 == 0 and i % 5 == 0:
        print("fizz-buzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

for i in range(1, num, 1):
    print(i)
