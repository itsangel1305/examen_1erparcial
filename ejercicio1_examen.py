
numero = int(input("Ingresa un número par entre 200 y 400: "))


if numero < 200 or numero > 400 or numero % 2 != 0:
    print("El número no es válido. Debe ser par y estar entre 200 y 400.")
else:
    # Usar un bucle para mostrar los números pares hasta 400
    for i in range(numero, 401, 2):
        print(i, end=", ")
