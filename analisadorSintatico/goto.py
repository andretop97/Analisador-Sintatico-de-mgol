def goto(state , symbol):
    if state == 0:
        if symbol == "P":
            return 1
    elif state == 2:
        if symbol == "V":
            return 3
    elif state == 3:
        if symbol == "A":
            return 5
        elif symbol == "ES":
            return 6
        elif symbol == "CMD":
            return 7
        elif symbol == "COND":
            return 8
        elif symbol == "CABECALHO":
            return 13
    elif state == 4:
        if symbol == "LV":
            return 15
        elif symbol == "D":
            return 16
    elif state == 6:
        if symbol == "A":
            return 19
        elif symbol == "ES":
            return 6
        elif symbol == "CMD":
            return 7
        elif symbol == "COND":
            return 8
        elif symbol == "CABECALHO":
            return 13
    elif state == 7:
        if symbol == "A":
            return 21
        elif symbol == "ES":
            return 6
        elif symbol == "CMD":
            return 7
        elif symbol == "COND":
            return 8
        elif symbol == "CABECALHO":
            return 13
    elif state == 8:
        if symbol == "A":
            return 22
        elif symbol == "ES":
            return 6
        elif symbol == "CMD":
            return 7
        elif symbol == "COND":
            return 8
        elif symbol == "CABECALHO":
            return 13
    elif state == 11:
        if symbol == "ARG":
            return 25
    elif state == 13:
        if symbol == "ES":
            return 31
        elif symbol == "CMD":
            return 32
        elif symbol == "COND":
            return 33
        elif symbol == "CABECALHO":
            return 13
        elif symbol == "CORPO":
            return 30
    elif state == 16:
        if symbol == "LV":
            return 36
        elif symbol == "D":
            return 16
    elif state == 18:
        if symbol == "TIPO":
            return 38
    elif state == 29:
        if symbol == "LD":
            return 42
        elif symbol == "OPRD":
            return 43
    elif state == 31:
        if symbol == "ES":
            return 31
        elif symbol == "CMD":
            return 32
        elif symbol == "COND":
            return 33
        elif symbol == "CABECALHO":
            return  13
        elif symbol == "CORPO":
            return 46
    elif state == 32:
        if symbol == "ES":
            return 31
        elif symbol == "CMD":
            return 32
        elif symbol == "COND":
            return 33
        elif symbol == "CABECALHO":
            return  13
        elif symbol == "CORPO":
            return 47
    elif state == 33:
        if symbol == "ES":
            return 31
        elif symbol == "CMD":
            return 32
        elif symbol == "COND":
            return 33
        elif symbol == "CABECALHO":
            return  13
        elif symbol == "CORPO":
            return 48
    elif state == 33:
        if symbol == "OPRD":
            return 50
        elif symbol == "EXP_R":
            return 49
    elif state == 53:
        if symbol == "OPRD":
            return 56
    elif state == 55:
        if symbol == "OPRD":
            return 58