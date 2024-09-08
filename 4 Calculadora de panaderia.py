precio = 3.49
descuento = 0.60

n = int(input("Introduce el número de panes del dia anterio: "))

pcd = precio * (1 - descuento)
cf = n * pcd

print(f"Precio habitual de una barra: {precio} pesos")
print(f"Descuento por no ser fresca: {descuento * 100}%")
print(f"Coste final por las {n} barras del dia anterior: {cf:.2f} pesos")

input("Presiona Enter para salir...")
