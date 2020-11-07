def action(state, symbol):
    if state == 0:
        if symbol == "inicio":
            return ["s", 2]

        else:
            return ["Erro", 0]

    if state == 1:
        if symbol == "$":
            return ["ACC", 0]

        else:
            return ["Erro", 0]

    if state == 2:
        if symbol == "varinicio":
            return ["s", 4]

        else:
            return ["Erro", 0]

    if state == 3:
        if symbol == "id":
            return ["s", 12]
        elif symbol == "leia":
            return ["s", 10]
        elif symbol == "escreva":
            return ["s", 11]
        elif symbol == "se":
            return ["s", 14]
        elif symbol == "fim":
            return ["s", 9]

        else:
            return ["Erro", 0]

    if state == 4:
        if symbol == "varfim":
            return ["s", 17]
        elif symbol == "id":
            return ["s", 18]

        else:
            return ["Erro", 0]

    if state == 5:
        if symbol == "$":
            return ["r", 2]

        else:
            return ["Erro", 0]

    if state == 6:
        if symbol == "id":
            return ["s", 12]
        elif symbol == "leia":
            return ["s", 10]
        elif symbol == "escreva":
            return ["s", 11]
        elif symbol == "se":
            return ["s", 14]
        elif symbol == "fim":
            return ["s", 9]

        else:
            return ["Erro", 0]

    if state == 7:
        if symbol == "id":
            return ["s", 12]
        elif symbol == "leia":
            return ["s", 10]
        elif symbol == "escreva":
            return ["s", 11]
        elif symbol == "se":
            return ["s", 14]
        elif symbol == "fim":
            return ["s", 9]

        else:
            return ["Erro", 0]

    if state == 8:
        if symbol == "id":
            return ["s", 12]
        elif symbol == "leia":
            return ["s", 10]
        elif symbol == "escreva":
            return ["s", 11]
        elif symbol == "se":
            return ["s", 14]
        elif symbol == "fim":
            return ["s", 9]

        else:
            return ["Erro", 0]

    if state == 9:
        if symbol == "$":
            return ["r", 30]

        else:
            return ["Erro", 0]

    if state == 10:
        if symbol == "id":
            return ["s", 23]

        else:
            return ["Erro", 0]

    if state == 11:
        if symbol == "id":
            return ["s", 28]
        elif symbol == "literal":
            return ["s", 26]
        elif symbol == "num":
            return ["s", 27]

        else:
            return ["Erro", 0]

    if state == 12:
        if symbol == "rcb":
            return ["s", 29]

        else:
            return ["Erro", 0]

    if state == 13:
        if symbol == "id":
            return ["s", 12]
        elif symbol == "leia":
            return ["s", 10]
        elif symbol == "escreva":
            return ["s", 11]
        elif symbol == "se":
            return ["s", 14]
        elif symbol == "fimse":
            return ["s", 34]

        else:
            return ["Erro", 0]

    if state == 14:
        if symbol == "(":
            return ["s", 35]

        else:
            return ["Erro", 0]

    if state == 15:
        if symbol == "id":
            return ["r", 3]
        elif symbol == "leia":
            return ["r", 3]
        elif symbol == "escreva":
            return ["r", 3]
        elif symbol == "se":
            return ["r", 3]
        elif symbol == "fimse":
            return ["r", 3]

        else:
            return ["Erro", 0]

    if state == 16:
        if symbol == "varfim":
            return ["s", 17]
        elif symbol == "id":
            return ["s", 18]

        else:
            return ["Erro", 0]

    if state == 17:
        if symbol == ";":
            return ["s", 37]

        else:
            return ["Erro", 0]

    if state == 18:
        if symbol == "int":
            return ["s", 39]
        elif symbol == "real":
            return ["s", 40]
        elif symbol == "lit":
            return ["s", 41]

        else:
            return ["Erro", 0]

    if state == 19:
        if symbol == "$":
            return ["r", 10]

        else:
            return ["Erro", 0]

    if state == 20:
        if symbol == "id":
            return ["r", 12]
        elif symbol == "leia":
            return ["r", 12]
        elif symbol == "escreva":
            return ["r", 12]
        elif symbol == "se":
            return ["r", 12]
        elif symbol == "fimse":
            return ["r", 12]
        elif symbol == "fim":
            return ["r", 12]

        else:
            return ["Erro", 0]

    if state == 21:
        if symbol == "$":
            return ["r", 10]

        else:
            return ["Erro", 0]

    if state == 22:
        if symbol == "$":
            return ["r", 10]

        else:
            return ["Erro", 0]

    if state == 23:
        if symbol == ";":
            return ["s", 24]

        else:
            return ["Erro", 0]

    if state == 24:
        if symbol == "id":
            return ["r", 11]
        elif symbol == "leia":
            return ["r", 11]
        elif symbol == "escreva":
            return ["r", 11]
        elif symbol == "se":
            return ["r", 11]
        elif symbol == "fimse":
            return ["r", 11]
        elif symbol == "fim":
            return ["r", 11]

        else:
            return ["Erro", 0]

    if state == 25:
        if symbol == ";":
            return ["s", 20]

        else:
            return ["Erro", 0]

    if state == 26:
        if symbol == ";":
            return ["r", 13]

        else:
            return ["Erro", 0]

    if state == 27:
        if symbol == ";":
            return ["r", 14]

        else:
            return ["Erro", 0]
    
    if state == 28:
        if symbol == ";":
            return ["r", 15]

        else:
            return ["Erro", 0]

    if state == 29:
        if symbol == "id":
            return ["s", 44]
        elif symbol == "num":
            return ["s", 45]

        else:
            return ["Erro", 0]

    if state == 30:
        if symbol == "id":
            return ["r", 23]
        elif symbol == "leia":
            return ["r", 23]
        elif symbol == "escreva":
            return ["r", 23]
        elif symbol == "se":
            return ["r", 23]
        elif symbol == "fimse":
            return ["r", 23]
        elif symbol == "fim":
            return ["r", 23]

        else:
            return ["Erro", 0]

    if state == 31:
        if symbol == "id":
            return ["s", 12]
        elif symbol == "leia":
            return ["s", 10]
        elif symbol == "escreva":
            return ["s", 11]
        elif symbol == "se":
            return ["s", 14]
        elif symbol == "fimse":
            return ["s", 34]

        else:
            return ["Erro", 0]

    if state == 32:
        if symbol == "id":
            return ["s", 12]
        elif symbol == "leia":
            return ["s", 10]
        elif symbol == "escreva":
            return ["s", 11]
        elif symbol == "se":
            return ["s", 14]
        elif symbol == "fimse":
            return ["s", 34]

        else:
            return ["Erro", 0]

    if state == 33:
        if symbol == "id":
            return ["s", 12]
        elif symbol == "leia":
            return ["s", 10]
        elif symbol == "escreva":
            return ["s", 11]
        elif symbol == "se":
            return ["s", 14]
        elif symbol == "fimse":
            return ["s", 34]

        else:
            return ["Erro", 0]

    if state == 34:
        if symbol == "id":
            return ["r", 29]
        elif symbol == "leia":
            return ["r", 29]
        elif symbol == "escreva":
            return ["r", 29]
        elif symbol == "se":
            return ["r", 29]
        elif symbol == "fimse":
            return ["r", 29]
        elif symbol == "fim":
            return ["r", 29]

        else:
            return ["Erro", 0]

    if state == 35:
        if symbol == "id":
            return ["s", 44]
        elif symbol == "num":
            return ["s", 45]

        else:
            return ["Erro", 0]

    if state == 36:
        if symbol == "id":
            return ["r", 4]
        elif symbol == "leia":
            return ["r", 4]
        elif symbol == "escreva":
            return ["r", 4]
        elif symbol == "se":
            return ["r", 4]
        elif symbol == "fim":
            return ["r", 4]

        else:
            return ["Erro", 0]

    if state == 37:
        if symbol == "id":
            return ["r", 5]
        elif symbol == "leia":
            return ["r", 5]
        elif symbol == "escreva":
            return ["r", 5]
        elif symbol == "se":
            return ["r", 5]
        elif symbol == "fim":
            return ["r", 5]

        else:
            return ["Erro", 0]

    if state == 38:
        if symbol == ";":
            return ["s", 51]

        else:
            return ["Erro", 0]

    if state == 39:
        if symbol == ";":
            return ["r", 7]

        else:
            return ["Erro", 0]

    if state == 40:
        if symbol == ";":
            return ["r", 8]

        else:
            return ["Erro", 0]

    if state == 41:
        if symbol == ";":
            return ["r", 9]

        else:
            return ["Erro", 0]

    if state == 42:
        if symbol == ";":
            return ["s", 52]

        else:
            return ["Erro", 0]

    if state == 43:
        if symbol == ";":
            return ["r", 19]
        elif symbol == "opm":
            return ["s", 53]

        else:
            return ["Erro", 0]

    if state == 44:
        if symbol == ";":
            return ["r", 20]
        elif symbol == "opm":
            return ["r", 20]
        elif symbol == "opr":
            return ["r", 20]
        elif symbol == ")":
            return ["r", 20]

        else:
            return ["Erro", 0]

    if state == 45:
        if symbol == ";":
            return ["r", 21]
        elif symbol == "opm":
            return ["r", 21]
        elif symbol == "opr":
            return ["r", 21]
        elif symbol == ")":
            return ["r", 21]

        else:
            return ["Erro", 0]

    if state == 46:
        if symbol == "id":
            return ["r", 26]
        elif symbol == "leia":
            return ["r", 26]
        elif symbol == "escreva":
            return ["r", 26]
        elif symbol == "se":
            return ["r", 26]
        elif symbol == "fimse":
            return ["r", 26]
        elif symbol == "fim":
            return ["r", 26]

        else:
            return ["Erro", 0]


    if state == 47:
        if symbol == "id":
            return ["r", 27]
        elif symbol == "leia":
            return ["r", 27]
        elif symbol == "escreva":
            return ["r", 27]
        elif symbol == "se":
            return ["r", 27]
        elif symbol == "fimse":
            return ["r", 27]
        elif symbol == "fim":
            return ["r", 27]

        else:
            return ["Erro", 0]

    if state == 48:
        if symbol == "id":
            return ["r", 28]
        elif symbol == "leia":
            return ["r", 28]
        elif symbol == "escreva":
            return ["r", 28]
        elif symbol == "se":
            return ["r", 28]
        elif symbol == "fimse":
            return ["r", 28]
        elif symbol == "fim":
            return ["r", 28]

        else:
            return ["Erro", 0]

    if state == 49:
        if symbol == ")":
            return ["s", 54]

        else:
            return ["Erro", 0]

    if state == 50:
        if symbol == "opr":
            return ["s", 55]

        else:
            return ["Erro", 0]

    if state == 51:
        if symbol == "varfim":
            return ["r", 6]
        elif symbol == "id":
            return ["r", 6]

        else:
            return ["Erro", 0]

    if state == 52:
        if symbol == "id":
            return ["r", 17]
        elif symbol == "leia":
            return ["r", 17]
        elif symbol == "escreva":
            return ["r", 17]
        elif symbol == "se":
            return ["r", 17]
        elif symbol == "fimse":
            return ["r", 17]
        elif symbol == "fim":
            return ["r", 17]

        else:
            return ["Erro", 0]

    if state == 53:
        if symbol == "id":
            return ["s", 44]
        elif symbol == "num":
            return ["s", 45]

        else:
            return ["Erro", 0]

    if state == 54:
        if symbol == "entao":
            return ["s", 57]

        else:
            return ["Erro", 0]

    if state == 55:
        if symbol == "id":
            return ["s", 44]
        elif symbol == "num":
            return ["s", 45]

        else:
            return ["Erro", 0]

    if state == 56:
        if symbol == ";":
            return ["r", 18]

        else:
            return ["Erro", 0]

    if state == 57:
        if symbol == "id":
            return ["r", 24]
        elif symbol == "leia":
            return ["r", 24]
        elif symbol == "escreva":
            return ["r", 24]
        elif symbol == "se":
            return ["r", 24]
        elif symbol == "fimse":
            return ["r", 24]

        else:
            return ["Erro", 0]

    if state == 56:
        if symbol == ")":
            return ["r", 25]

        else:
            return ["Erro", 0]