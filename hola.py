print("Bienvenido al programa para saber tu promedio")
nom=input("Escriba su nombre:")
print("Bienvenido:",nom)
cal1=int(input("Escriba la primera calificacion:"))
cal2=int(input("Escriba la segunda calificacion:"))
cal3=int(input("Escriba la tercera calificacion:"))
cal4=int(input("Escriba la cuarta calificacion:"))
total=(cal1+cal2+cal3+cal4)/4
print ("Tu npromedio es:",total)
if total>=6:
    print("Felicidades aprobaste la materia")
else:
    print("Esfuerzate para pasar tu materia")
