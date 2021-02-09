alfabeto = ["walk", "rotate", "drop", "free", "pick", "grab", "walkTo", "NOP", "block","(", ")", "define", "blocked?", "facing", "if", "not", "can"]






def parser():
    file = open("input.txt", "r")
    f = file.read()

    valor = checker(f)

    if valor is False:
        print("Ha ocurrido un error en la comprobación del código")
    else:
        print("El programa no presentó errores.")


def checker(f:str) -> bool:
    palabra = ""
    listaPal = []
    contadorPar = 0
    for caracter in f:
        if " " in listaPal:
            listaPal.remove(" ")
        if contadorPar < 0:
            return False
        if caracter == "(" :
            contadorPar += 1
            listaPal.append(palabra)
            listaPal.append(caracter)   
        elif caracter == ")":
            contadorPar -= 1
            listaPal.append(palabra)
            listaPal.append(caracter)
            palabra = ""
        elif caracter == " ":
            if palabra == " " or palabra == "":
                pass
            else:
                listaPal.append(palabra)
                palabra = ""           
        elif caracter == "\n":
            listaPal.append(palabra)
            palabra = "" 
        else:
            palabra += caracter
    if contadorPar != 0:
        return False
    while "" in listaPal:
        listaPal.remove("")

    print(listaPal)

def comparador(listaPal:list, commands:list)->bool:
    for i in range(len(listaPal)):
        try:
            val = int(listaPal[i])
        except:
            pass #Completar
        if listaPal[i] not in alfabeto:
            pass #Completar
parser()