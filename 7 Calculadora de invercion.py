Invercion = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual (en %): ")) / 100
tiempo = int(input("Introduce el número de años: "))

capital = Invercion

print("\nAño\tCapital")
for anio in range(1, tiempo + 1):
    capital += capital * interes  
    print(f"{tiempo}\t{capital:.2f} pesos")

input("Presiona Enter para salir...")
