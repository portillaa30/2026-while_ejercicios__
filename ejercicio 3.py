n=float(input("Ingrese una nota"))

promedio=0.0
suma_notas=(0.0)
cantidad_notas=0.0

while n != -99:
    suma_notas += n
    cantidad_notas=(range(suma_notas))
    promedio=(suma_notas/cantidad_notas)
    n=float(input("Ingrese una nota: "))

print("cantidad",cantidad_notas,"promedio:",promedio)