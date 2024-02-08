
numero = int(input("Ingresa un número entero: "))

print(numero, end=" ")

while numero != 1:
    if numero % 2 == 0:  # Si el número es par
        numero = numero // 2
    else:  # Si el número es impar
        numero = 3 * numero + 1
    print(numero, end=" ")
