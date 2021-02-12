alfabeto = ["walk", "rotate", "drop", "free", "pick", "grab", "walkTo", "NOP", "block","(", ")", "define", "blocked?", "facing?", "if", "not", "can", "left", "right", "back", "N", "E", "W", "S"]
extra = {}
def parser():
    file = open("input.txt", "r")
    f = file.read()

    valor = checker(f)

    if valor is False:
        print("Ha ocurrido un error con la comprobación del código [Syntax Error].")
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
    if comparador(listaPal, alfabeto) is False:
        return False
    else:
        return True
    

def comparador(listaPal:list, alfabeto:list)->bool:
    for i in range(len(listaPal)):
        if listaPal[i] not in alfabeto:
            print(listaPal[i])
            return False
        else:
            definirVarFun(listaPal, i)
            caminar = compararWalk(listaPal, i)
            rotar = compararRotate(listaPal, i)
            mirar = compararLook(listaPal, i)
            soltar = compararDrop(listaPal, i)
            liberar = compararFree(listaPal, i)
            recoger = compararPick(listaPal, i)
            agarrar = compararGrab(listaPal, i)
            caminarA = compararWalkTo(listaPal, i)
            nada = compararNOP(listaPal, i)
            compararif = compareIf(listaPal, i)
            if caminar is False or rotar is False or mirar is False or soltar is False or liberar is False or recoger is False or agarrar is False or caminarA is False or nada is False or compararif is False:
                return False
            
            

def definirVarFun(listaPal:list, i:int):
    if listaPal[i] == "define" and listaPal[i+2] != "(":
        alfabeto.append(listaPal[i+1])
        try:
            val = int(listaPal[i+2])
            extra[listaPal[i+1]] = type(val)
            alfabeto.append(listaPal[i+2])
        except:
            extra[listaPal[i+1]] = str
            alfabeto.append(listaPal[i+2])
    elif listaPal[i] == "define" and listaPal[i+2] == "(":
        alfabeto.append(listaPal[i+1])
        param = []
        n = 3
        while True:
            if listaPal[i+n] == ")":
                break
            param.append(listaPal[i+n])
            n += 1  
        extra[listaPal[i+1]] = param
        if listaPal[i+n+1] != "(" or listaPal[i+n+1] != "block":
            return False
        else:
            return True


def compararWalk(listaPal:list, i:int)-> bool:
    if listaPal[i] == "walk" and listaPal[i-1] != "(":
            return False
    elif listaPal[i] == "walk":
        try:
            int(listaPal[i+1])
            alfabeto.append(listaPal[i+1])
            return True
        except:
            if not listaPal[i+1] in extra.keys():
                return False
            else:
                if extra[listaPal[i+1]] is not int:
                    return False
                else:
                    if listaPal[i+2] != ")":
                        return False
                    else:
                        return True
    else:
        return True   

def compararRotate(listaPal:list, i:int)-> bool:
    if listaPal[i] == "rotate" and (listaPal[i-1] != "(" or listaPal[i+2] != ")"):
        return False
    elif listaPal[i] == "rotate":
        parameters = ["left", "right", "back"]
        if listaPal[i+1] not in parameters:
            return False
        else:
            return True
    else:
        return True

def compararLook(listaPal:list, i:int)-> bool:
    if listaPal[i] == "look" and (listaPal[i-1] != "(" or listaPal[i+2] != ")"):
        return False
    elif listaPal[i] == "look":
        parameters = ["N", "E", "W", "S"]
        if listaPal[i+1] not in parameters:
            return False
        else:
            return True
    else:
        return True

def compararDrop(listaPal:list, i:int)-> bool:
    if listaPal[i] == "drop" and listaPal[i-1] != "(":
            return False
    elif listaPal[i] == "drop":
        try:
            int(listaPal[i+1])
            alfabeto.append(listaPal[i+1])
            return True
        except:
            if not listaPal[i+1] in extra.keys():
                return False
            else:
                if extra[listaPal[i+1]] is not int:
                    return False
                else:
                    if listaPal[i+2] != ")":
                        return False
                    else:
                        return True
    else:
        return True

def compararFree(listaPal:list, i:int)-> bool:
    if listaPal[i] == "free" and listaPal[i-1] != "(":
            return False
    elif listaPal[i] == "free":
        try:
            int(listaPal[i+1])
            alfabeto.append(listaPal[i+1])
            return True
        except:
            if not listaPal[i+1] in extra.keys():
                return False
            else:
                if extra[listaPal[i+1]] is not int:
                    return False
                else:
                    if listaPal[i+2] != ")":
                        return False
                    else:
                        return True
    else:
        return True
    
def compararPick(listaPal:list, i:int)-> bool:
    if listaPal[i] == "pick" and listaPal[i-1] != "(":
            return False
    elif listaPal[i] == "pick":
        try:
            int(listaPal[i+1])
            alfabeto.append(listaPal[i+1])
            return True
        except:
            if not listaPal[i+1] in extra.keys():
                return False
            else:
                if extra[listaPal[i+1]] is not int:
                    return False
                else:
                    if listaPal[i+2] != ")":
                        return False
                    else:
                        return True
    else:
        return True

def compararGrab(listaPal:list, i:int)-> bool:
    if listaPal[i] == "grab" and listaPal[i-1] != "(":
            return False
    elif listaPal[i] == "grab":
        try:
            int(listaPal[i+1])
            alfabeto.append(listaPal[i+1])
            return True
        except:
            if not listaPal[i+1] in extra.keys():
                return False
            else:
                if extra[listaPal[i+1]] is not int:
                    return False
                else:
                    if listaPal[i+2] != ")":
                        return False
                    else:
                        return True
    else:
        return True
def compararWalkTo(listaPal:list, i:int)-> bool:
    if listaPal[i] == "walkTo" and listaPal[i-1] != "(":
            return False
    elif listaPal[i] == "walkTo":
        try:
            int(listaPal[i+1])
            alfabeto.append(listaPal[i+1])
            return True
        except:
            if not listaPal[i+1] in extra.keys():
                return False
            else:
                if extra[listaPal[i+1]] is not int:
                    return False
                else:
                    if listaPal[i+3] != ")":
                        return False
                    else:
                        parameters = ["N", "E", "W", "S"]
                        if listaPal[i+2] not in parameters:
                            return False
                        else:
                            return True
    else:
        return True

def compararNOP(listaPal:list, i:int)->bool:
    if listaPal[i] == "NOP" and (listaPal[i-1] != "(" or listaPal[i+1] != ")"):
        return False
    else:
        return True

def compareIf(listaPal:list, i:int)->bool:
    parameters = ["blocked?", "not", "facing?", "can"]
    if listaPal[i] == "if" and (listaPal[i-1] != "("or listaPal[i+1] != "("):
        return False
    elif listaPal[i] == "if" and listaPal[i+2] not in parameters:
        return False
    elif listaPal[i] == "if" and listaPal[i+2] == "facing?":
        paramFacing = ["N", "E", "W", "S"]
        if listaPal[i+3] not in paramFacing:
            return False
    elif listaPal[i] == "if" and listaPal[i+2] == "can":
        paramCan = ["grab", "drop", "free", "pick"]
        if listaPal[i+3] not in paramCan:
            return False
    elif listaPal[i] == "if" and listaPal[i+2] == "not" and listaPal[i+4] not in parameters:
        return False
    elif listaPal[i] == "if" and listaPal[i+2] == "not":
        res = ifnot(listaPal, i+4)
        if res is False:
            return False
        else:
            return True
    else:
        return True


def ifnot(listaPal:list, i:int)->bool:
    parameters = ["blocked?", "not", "facing?", "can"]
    if listaPal[i] == "not" and (listaPal[i-1] != "("or listaPal[i+1] != "("):
        return False
    elif listaPal[i] == "not" and listaPal[i+2] not in parameters:
        return False
    elif listaPal[i] == "not" and listaPal[i+2] == "facing?":
        paramFacing = ["N", "E", "W", "S"]
        if listaPal[i+3] not in paramFacing:
            return False
    elif listaPal[i] == "not" and listaPal[i+2] == "can":
        paramCan = ["grab", "drop", "free", "pick"]
        if listaPal[i+3] not in paramCan:
            return False
    elif listaPal[i] == "not" and listaPal[i+2] == "not" and listaPal[i+3] not in parameters:
        return False
    elif listaPal[i] == "not" and listaPal[i+2] == "not":
        res = ifnot(listaPal, i+4)
        if res is False:
            return False
        else:
            return True
    else:
        return True

parser()