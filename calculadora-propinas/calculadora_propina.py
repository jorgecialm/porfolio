"""
Crea un programa que:
Pida al usuario el total de la cuenta del restaurante
Pida el porcentaje de propina que quiere dejar
Calcule el monto de la propina
Calcule el total a pagar (cuenta + propina)
Calcule cuanto paga cada comensal
Muestre los tres resultados
"""
print("****Calculadora de propinas****\n")
cuenta_valida=False
porcentaje_valido=False
personas_valido=False
#Cuenta
try:
    cuenta=float(input("Ingrese el valor de la  cuenta del restaurante : "))
    if cuenta <= 0:
        print("error")
    else:
        cuenta_valida=True
except ValueError:
    print("Debe ingresar solo numeros positivos")
# Porcentaje    
try:  
    porcentaje=int(input("Ingrese el porcentaje : "))
    if porcentaje >= 1 and porcentaje <=100:
        porcentaje_valido=True
    else:
        print("Error. Por favor ingrese un numeo entre 1 y 100 %")
except ValueError:
    print("Error.El porcentaje debe ser un numero entre 1 y 100")
#Personas    
try:
    personas = int(input("¿Entre cuántas personas dividir la cuenta? "))
    
    if personas > 0:
        personas_valido=True
except ValueError:
    print("Error,debe ingresar numeros mayores que cero")
    
if porcentaje_valido and cuenta_valida and personas_valido:
    propina=cuenta * (porcentaje/100)
    print(f"\nEl monto de la propina es de $ {propina:.2f}")
    print(f"El total de la cuenta mas la propina es de ${cuenta + propina:.2f}")
    total_persona=(cuenta + propina)/personas
    print(f"El total que paga cada persona es de ${total_persona:.2f}")
else:
    print("Debe corregir los errores, vuelva a ejecutar el programa con los datos correctos ")
