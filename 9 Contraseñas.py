contrasena = "contraseña"

introducida = ""

while introducida != contrasena:
    introducida = input("Introduce la contraseña: ")
    
    if introducida != contrasena:
        print("Contraseña incorrecta. Inténtalo de nuevo.")

print("¡Contraseña correcta!")

input("Presiona Enter para salir...")
