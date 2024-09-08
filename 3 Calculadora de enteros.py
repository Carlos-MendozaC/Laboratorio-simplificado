n = int(input("Introduce un número entero: "))

if n > 0:
    suma = n * (n + 1) // 2
    
    print(f"La suma de los primeros numeros {n} enteros positivos es: {suma}")
else:
    print("El número introducido no es un entero positivo.")

input("Presiona Enter para salir...")
