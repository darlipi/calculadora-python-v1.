A = int(input("Escribe el primer numero: "))
B = int(input("Escribe el segundo numero: "))

while True:
    print("Que operacion quieres realizar: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    operacion = int(input("Escribe el numero de la operacion: "))
    
    if operacion == 1:
        resultado = A + B
        print("El resultado de la suma es: ", resultado)
        break
    elif operacion == 2:
        resultado = A - B
        print("El resultado de la resta es: ", resultado)
        break
    elif operacion == 3:
        resultado = A * B
        print("El resultado de la multiplicacion es: ", resultado)
        break
    elif operacion == 4:
        if B == 0:
            print("No se puede dividir entre cero")
        else:  
            resultado = A / B
            print("El resultado de la division es: ", resultado)
            break       
    else:
        print("Tu numero no es valido intenta de nuevo, selecciona un numero del 1 al 4")
