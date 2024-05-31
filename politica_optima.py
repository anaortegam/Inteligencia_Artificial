# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random

fichero = 'on_tabla.csv'


with open(fichero, 'r') as archivo:
    contenido = archivo.read()
    numero = ""
    tabla_on = []
    fila = []
    for caracter in contenido:
        if caracter != ";" and caracter != "\n":
            numero += str(caracter)
        elif numero != "":
            if len(fila) != 0:
                fila.append(round(float(numero), 1))
            else:
                fila.append(numero)
            numero = ""
        if caracter == "\n":
            tabla_on.append(fila)
            fila = []

fichero = 'off_tabla.csv'

with open(fichero, 'r') as archivo:
    contenido = archivo.read()
    numero = ""
    tabla_off = []
    fila = []
    for caracter in contenido:
        if caracter != ";" and caracter != "\n":
            numero += str(caracter)
        elif numero != "":
            if len(fila) != 0:
                fila.append(round(float(numero), 1))
            else:
                fila.append(numero)
            numero = ""
        if caracter == "\n":
            tabla_off.append(fila)
            fila = []

def politica_optima(c_off, c_on):
    temp_final = 12
    actual = []
    siguiente = []
    optima = []
    coste = min(c_off, c_on)

    for i in range(19):
        actual.append(0)
        siguiente.append(coste)
        optima.append("")
        if i == temp_final:
            siguiente[i] = 0
            actual[i] = 0
            optima[i] = 0

    #Calcular bellman
    while actual != siguiente:
    #while cont < 1:
        for i in range(19):
            actual[i] = siguiente[i]
        for indice in range(19):
            valor_off = 0
            valor_on = 0
            if indice != temp_final:
                for valor in range(19):
                    valor_off += round(actual[valor]*tabla_off[indice+1][valor+1],5)
                    valor_on += round(actual[valor]*tabla_on[indice+1][valor+1],5)
                valor_off += c_off
                valor_on += c_on
                siguiente[indice] = min(valor_off, valor_on)


                if siguiente[indice] == valor_off:
                    optima[indice] = "off"
                elif siguiente[indice] == valor_on:
                    optima[indice] = "on"
    print(siguiente)
    return optima

temperatura_deseada = 22
temperatura_actual = (random.randint(1,19)+31)/2
bellman = politica_optima(1, 20)
print(bellman)

while temperatura_deseada != temperatura_actual:
    numero = random.randint(1,10)
    indice = int((temperatura_actual * 2) - 31)
    if bellman[indice-1] == "off":
        for i in range(19):
            if tabla_off[indice][i+1] != 0.0 and numero > 0:
                sustraendo = int(float(tabla_off[indice][i + 1]) * 10)
                numero -= sustraendo
                if numero <= 0:
                    temperatura_actual = (i+32)/2
    elif bellman[indice-1] == "on":
        for i in range(19):
            if tabla_on[indice][i+1] != 0.0 and numero > 0:
                sustraendo = int(float(tabla_on[indice][i + 1]) * 10)
                numero -= sustraendo
                if numero <= 0:
                    temperatura_actual = (i+32)/2
    print(temperatura_actual)