import re

def mosquito1():
    expresion = 'M(A|E|I)LO'

    with open("datos1.txt", "r") as datos:
        for linea in datos:
            res = re.findall(expresion, linea)
            if res:
                print(linea)

def mosquito2():
    expresion = '[0-5][0-9]'

    with open("datos2.txt", "r") as datos:
        for linea in datos:
            res = re.findall(expresion, linea)
            if res:
                print(res)
                #print(linea)

def mosquito3():
    # expresion = '^(\d{2})$'
    expresion = '^(\d{2}|\d{4})$'

    with open("data1.txt", "r") as datos:
        for linea in datos:
            res = re.findall(expresion, linea)
            if res:
                print(linea)

mosquito3()
