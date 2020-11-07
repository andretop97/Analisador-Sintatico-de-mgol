def goto(state, notTerminal):
    if state == 0:
        if notTerminal == "P":
            return 1
    elif state == 2:
        if notTerminal == "V":
            return 3
    elif state == 3:
        if notTerminal == "A":
            return 5
        elif notTerminal == "ES":
            return 6
        elif notTerminal == "CMD":
            return 7
        elif notTerminal == "COND":
            return 8
        elif notTerminal == "CABECALHO":
            return 13
    elif state == 4:
        if notTerminal == "LV":
            return 15
        elif notTerminal == "D":
            return 16
    elif state == 6:
        if notTerminal == "A":
            return 19
        elif notTerminal == "ES":
            return 6
        elif notTerminal == "CMD":
            return 7
        elif notTerminal == "COND":
            return 8
        elif notTerminal == "CABECALHO":
            return 13
    elif state == 7:
        if notTerminal == "A":
            return 21
        elif notTerminal == "ES":
            return 6
        elif notTerminal == "CMD":
            return 7
        elif notTerminal == "COND":
            return 8
        elif notTerminal == "CABECALHO":
            return 13
    elif state == 8:
        if notTerminal == "A":
            return 22
        elif notTerminal == "ES":
            return 6
        elif notTerminal == "CMD":
            return 7
        elif notTerminal == "COND":
            return 8
        elif notTerminal == "CABECALHO":
            return 13
    elif state == 11:
        if notTerminal == "ARG":
            return 25
    elif state == 13:
        if notTerminal == "ES":
            return 31
        elif notTerminal == "CMD":
            return 32
        elif notTerminal == "COND":
            return 33
        elif notTerminal == "CABECALHO":
            return 13
        elif notTerminal == "CORPO":
            return 30
    elif state == 16:
        if notTerminal == "LV":
            return 36
        elif notTerminal == "D":
            return 16
    elif state == 18:
        if notTerminal == "TIPO":
            return 38
    elif state == 29:
        if notTerminal == "LD":
            return 42
        elif notTerminal == "OPRD":
            return 43
    elif state == 31:
        if notTerminal == "ES":
            return 31
        elif notTerminal == "CMD":
            return 32
        elif notTerminal == "COND":
            return 33
        elif notTerminal == "CABECALHO":
            return  13
        elif notTerminal == "CORPO":
            return 46
    elif state == 32:
        if notTerminal == "ES":
            return 31
        elif notTerminal == "CMD":
            return 32
        elif notTerminal == "COND":
            return 33
        elif notTerminal == "CABECALHO":
            return  13
        elif notTerminal == "CORPO":
            return 47
    elif state == 33:
        if notTerminal == "ES":
            return 31
        elif notTerminal == "CMD":
            return 32
        elif notTerminal == "COND":
            return 33
        elif notTerminal == "CABECALHO":
            return  13
        elif notTerminal == "CORPO":
            return 48
    elif state == 33:
        if notTerminal == "OPRD":
            return 50
        elif notTerminal == "EXP_R":
            return 49
    elif state == 53:
        if notTerminal == "OPRD":
            return 56
    elif state == 55:
        if notTerminal == "OPRD":
            return 58