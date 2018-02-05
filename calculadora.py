#!/usr/bin/python3
#Jaime Fernández Sánchez
#Calculadora
import sys

try:
    Operador = sys.argv[1]
    Operando_1 = float(sys.argv[2])
    Operando_2 = float(sys.argv[3])

    if Operador == 'suma':
        Resultado = Operando_1 + Operando_2
        print("Resultado: ",Resultado)

    elif Operador == 'resta':
        Resultado = Operando_1 - Operando_2
        print("Resultado: ",Resultado)

    elif Operador == 'multiplicacion':
        Resultado = Operando_1 * Operando_2
        print("Resultado: ",Resultado)

    elif Operador == 'division':
        try:
            Resultado = Operando_1 / Operando_2
            print("Resultado: ",Resultado)
        except ZeroDivisionError:
            print("Error: Intento de division por cero")
    else:
        print("Solo puede utilizar los siguientes operadores/funciones: 'suma','resta','multiplicacion' y 'division'")
except ValueError:
    print("Por favor, introduzca solamente números como operandos. Gracias")