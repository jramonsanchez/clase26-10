def Ejercicio1():
    salario= float(input("Introduce tu sueldo: "))
    if(salario<1000):
        salario = salario*.15 + salario
    elif(salario >= 1000):
        salario= salario*.12 + salario
    
    print("El sueldo final es: ", salario)

def Ejercicio2():
    ciclo =  True
    while (ciclo==True):
        print("Trabajador")
        print("Categoría 1, Categoría 2, Categoría 3, Categoría 4")
        tipo= int(input("¿Cuál es la clase de trabajador que es? "))
        sueldo= float(input("Ingrese su sueldo: "))

        if(tipo==1):
            sf= sueldo*.15+sueldo
            print("El sueldo final es: ", sf)
        elif(tipo==2):
            sf= sueldo*.10+sueldo
            print("El sueldo final es: ", sf)
        elif(tipo==3):
            sf= sueldo*.08+sueldo
            print("El sueldo final es: ", sf)
        elif(tipo==4):
            sf= sueldo*.07+sueldo
            print("El sueldo final es: ", sf)
        else:
            print("Valor inválido")
        opc=input("¿Desea ingresar otro trabajador? (Y/N)")
        if (opc== "Y" or opc== "y"):
            ciclo=True
        else:
            ciclo=False
