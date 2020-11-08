def action(state, token):
    if state == 0:
        if token == "inicio":
            return ["s", 2]

        else:
            return ["Err", 5]

    if state == 1:
        if token == "$":
            return ["ACC", 0]

        else:
            return ["Erro", 0]

    if state == 2:
        if token == "varinicio":
            return ["s", 4]

        else:
            return ["Err", 6]

    if state == 3:
        if token == "id":
            return ["s", 12]
        elif token == "leia":
            return ["s", 10]
        elif token == "escreva":
            return ["s", 11]
        elif token == "se":
            return ["s", 14]
        elif token == "fim":
            return ["s", 9]

        else:
            return ["Erro", 0]

    if state == 4:
        if token == "varfim":
            return ["s", 17]
        elif token == "id":
            return ["s", 18]

        else:
            return ["Erro", 0]

    if state == 5:
        if token == "$":
            return ["r", 2]

        else:
            return ["Erro", 0]

    if state == 6:
        if token == "id":
            return ["s", 12]
        elif token == "leia":
            return ["s", 10]
        elif token == "escreva":
            return ["s", 11]
        elif token == "se":
            return ["s", 14]
        elif token == "fim":
            return ["s", 9]

        else:
            return ["Erro", 0]

    if state == 7:
        if token == "id":
            return ["s", 12]
        elif token == "leia":
            return ["s", 10]
        elif token == "escreva":
            return ["s", 11]
        elif token == "se":
            return ["s", 14]
        elif token == "fim":
            return ["s", 9]

        else:
            return ["Erro", 0]

    if state == 8:
        if token == "id":
            return ["s", 12]
        elif token == "leia":
            return ["s", 10]
        elif token == "escreva":
            return ["s", 11]
        elif token == "se":
            return ["s", 14]
        elif token == "fim":
            return ["s", 9]

        else:
            return ["Erro", 0]

    if state == 9:
        if token == "$":
            return ["r", 30]

        else:
            return ["Erro", 0]

    if state == 10:
        if token == "id":
            return ["s", 23]

        else:
            return ["Erro", 0]

    if state == 11:
        if token == "id":
            return ["s", 28]
        elif token == "Literal":
            return ["s", 26]
        elif token == "Num":
            return ["s", 27]

        else:
            return ["Erro", 0]

    if state == 12:
        if token == "RCB":
            return ["s", 29]

        else:
            return ["Erro", 0]

    if state == 13:
        if token == "id":
            return ["s", 12]
        elif token == "leia":
            return ["s", 10]
        elif token == "escreva":
            return ["s", 11]
        elif token == "se":
            return ["s", 14]
        elif token == "fimse":
            return ["s", 34]

        else:
            return ["Erro", 0]

    if state == 14:
        if token == "AB_P":
            return ["s", 35]

        else:
            return ["Erro", 0]

    if state == 15:
        if token == "id":
            return ["r", 3]
        elif token == "leia":
            return ["r", 3]
        elif token == "escreva":
            return ["r", 3]
        elif token == "se":
            return ["r", 3]
        elif token == "fimse":
            return ["r", 3]

        else:
            return ["Erro", 0]

    if state == 16:
        if token == "varfim":
            return ["s", 17]
        elif token == "id":
            return ["s", 18]

        else:
            return ["Erro", 0]

    if state == 17:
        if token == "PT_V":
            return ["s", 37]

        else:
            return ["Err", 7]

    if state == 18:
        if token == "inteiro":
            return ["s", 39]
        elif token == "real":
            return ["s", 40]
        elif token == "lit":
            return ["s", 41]

        else:
            return ["Erro", 0]

    if state == 19:
        if token == "$":
            return ["r", 10]

        else:
            return ["Erro", 0]

    if state == 20:
        if token == "id":
            return ["r", 12]
        elif token == "leia":
            return ["r", 12]
        elif token == "escreva":
            return ["r", 12]
        elif token == "se":
            return ["r", 12]
        elif token == "fimse":
            return ["r", 12]
        elif token == "fim":
            return ["r", 12]

        else:
            return ["Erro", 0]

    if state == 21:
        if token == "$":
            return ["r", 10]

        else:
            return ["Erro", 0]

    if state == 22:
        if token == "$":
            return ["r", 10]

        else:
            return ["Erro", 0]

    if state == 23:
        if token == "PT_V":
            return ["s", 24]

        else:
            return ["Err", 7]

    if state == 24:
        if token == "id":
            return ["r", 11]
        elif token == "leia":
            return ["r", 11]
        elif token == "escreva":
            return ["r", 11]
        elif token == "se":
            return ["r", 11]
        elif token == "fimse":
            return ["r", 11]
        elif token == "fim":
            return ["r", 11]

        else:
            return ["Erro", 0]

    if state == 25:
        if token == "PT_V":
            return ["s", 20]

        else:
            return ["Err", 7]

    if state == 26:
        if token == "PT_V":
            return ["r", 13]

        else:
            return ["Err", 7]

    if state == 27:
        if token == "PT_V":
            return ["r", 14]

        else:
            return ["Err", 7]
    
    if state == 28:
        if token == "PT_V":
            return ["r", 15]

        else:
            return ["Err", 7]

    if state == 29:
        if token == "id":
            return ["s", 44]
        elif token == "Num":
            return ["s", 45]

        else:
            return ["Erro", 0]

    if state == 30:
        if token == "id":
            return ["r", 23]
        elif token == "leia":
            return ["r", 23]
        elif token == "escreva":
            return ["r", 23]
        elif token == "se":
            return ["r", 23]
        elif token == "fimse":
            return ["r", 23]
        elif token == "fim":
            return ["r", 23]

        else:
            return ["Erro", 0]

    if state == 31:
        if token == "id":
            return ["s", 12]
        elif token == "leia":
            return ["s", 10]
        elif token == "escreva":
            return ["s", 11]
        elif token == "se":
            return ["s", 14]
        elif token == "fimse":
            return ["s", 34]

        else:
            return ["Erro", 0]

    if state == 32:
        if token == "id":
            return ["s", 12]
        elif token == "leia":
            return ["s", 10]
        elif token == "escreva":
            return ["s", 11]
        elif token == "se":
            return ["s", 14]
        elif token == "fimse":
            return ["s", 34]

        else:
            return ["Erro", 0]

    if state == 33:
        if token == "id":
            return ["s", 12]
        elif token == "leia":
            return ["s", 10]
        elif token == "escreva":
            return ["s", 11]
        elif token == "se":
            return ["s", 14]
        elif token == "fimse":
            return ["s", 34]

        else:
            return ["Erro", 0]

    if state == 34:
        if token == "id":
            return ["r", 29]
        elif token == "leia":
            return ["r", 29]
        elif token == "escreva":
            return ["r", 29]
        elif token == "se":
            return ["r", 29]
        elif token == "fimse":
            return ["r", 29]
        elif token == "fim":
            return ["r", 29]

        else:
            return ["Erro", 0]

    if state == 35:
        if token == "id":
            return ["s", 44]
        elif token == "Num":
            return ["s", 45]

        else:
            return ["Erro", 0]

    if state == 36:
        if token == "id":
            return ["r", 4]
        elif token == "leia":
            return ["r", 4]
        elif token == "escreva":
            return ["r", 4]
        elif token == "se":
            return ["r", 4]
        elif token == "fim":
            return ["r", 4]

        else:
            return ["Erro", 0]

    if state == 37:
        if token == "id":
            return ["r", 5]
        elif token == "leia":
            return ["r", 5]
        elif token == "escreva":
            return ["r", 5]
        elif token == "se":
            return ["r", 5]
        elif token == "fim":
            return ["r", 5]

        else:
            return ["Erro", 0]

    if state == 38:
        if token == "PT_V":
            return ["s", 51]

        else:
            return ["Err", 7]

    if state == 39:
        if token == "PT_V":
            return ["r", 7]

        else:
            return ["Err", 7]

    if state == 40:
        if token == "PT_V":
            return ["r", 8]

        else:
            return ["Err", 7]

    if state == 41:
        if token == "PT_V":
            return ["r", 9]

        else:
            return ["Err", 7]

    if state == 42:
        if token == "PT_V":
            return ["s", 52]

        else:
            return ["Err", 7]

    if state == 43:
        if token == "PT_V":
            return ["r", 19]
        elif token == "OPM":
            return ["s", 53]

        else:
            return ["Erro", 0]

    if state == 44:
        if token == "PT_V":
            return ["r", 20]
        elif token == "OPM":
            return ["r", 20]
        elif token == "OPR":
            return ["r", 20]
        elif token == "FC_P":
            return ["r", 20]

        else:
            return ["Erro", 0]

    if state == 45:
        if token == "PT_V":
            return ["r", 21]
        elif token == "OPM":
            return ["r", 21]
        elif token == "OPR":
            return ["r", 21]
        elif token == "FC_P":
            return ["r", 21]

        else:
            return ["Err", 7]

    if state == 46:
        if token == "id":
            return ["r", 26]
        elif token == "leia":
            return ["r", 26]
        elif token == "escreva":
            return ["r", 26]
        elif token == "se":
            return ["r", 26]
        elif token == "fimse":
            return ["r", 26]
        elif token == "fim":
            return ["r", 26]

        else:
            return ["Erro", 0]


    if state == 47:
        if token == "id":
            return ["r", 27]
        elif token == "leia":
            return ["r", 27]
        elif token == "escreva":
            return ["r", 27]
        elif token == "se":
            return ["r", 27]
        elif token == "fimse":
            return ["r", 27]
        elif token == "fim":
            return ["r", 27]

        else:
            return ["Erro", 0]

    if state == 48:
        if token == "id":
            return ["r", 28]
        elif token == "leia":
            return ["r", 28]
        elif token == "escreva":
            return ["r", 28]
        elif token == "se":
            return ["r", 28]
        elif token == "fimse":
            return ["r", 28]
        elif token == "fim":
            return ["r", 28]

        else:
            return ["Erro", 0]

    if state == 49:
        if token == "FC_P":
            return ["s", 54]

        else:
            return ["Erro", 0]

    if state == 50:
        if token == "OPR":
            return ["s", 55]

        else:
            return ["Erro", 0]

    if state == 51:
        if token == "varfim":
            return ["r", 6]
        elif token == "id":
            return ["r", 6]
        elif token == "PT_V":
            return ["Err", 8]

        else:
            return ["Erro", 0]

    if state == 52:
        if token == "id":
            return ["r", 17]
        elif token == "leia":
            return ["r", 17]
        elif token == "escreva":
            return ["r", 17]
        elif token == "se":
            return ["r", 17]
        elif token == "fimse":
            return ["r", 17]
        elif token == "fim":
            return ["r", 17]

        else:
            return ["Erro", 0]

    if state == 53:
        if token == "id":
            return ["s", 44]
        elif token == "Num":
            return ["s", 45]

        else:
            return ["Erro", 0]

    if state == 54:
        if token == "entao":
            return ["s", 57]

        else:
            return ["Erro", 0]

    if state == 55:
        if token == "id":
            return ["s", 44]
        elif token == "Num":
            return ["s", 45]

        else:
            return ["Erro", 0]

    if state == 56:
        if token == "PT_V":
            return ["r", 18]

        else:
            return ["Err", 7]

    if state == 57:
        if token == "id":
            return ["r", 24]
        elif token == "leia":
            return ["r", 24]
        elif token == "escreva":
            return ["r", 24]
        elif token == "se":
            return ["r", 24]
        elif token == "fimse":
            return ["r", 24]

        else:
            return ["Erro", 0]

    if state == 58:
        if token == "FC_P":
            return ["r", 25]

        else:
            return ["Erro", 0]