import os


class SemanticAnalyzer:
    def __init__(self):
        self.tx = 0
        self.resetFile()

    def analyzer(self, indiceRule, stackSymbols):
        # Imprimir três linhas brancas no arquivo objeto;
        if indiceRule == 5:  # feito
            # print("LV -> varfim ;")
            self.writeFile("\n\n\n")

        elif indiceRule == 6:
            # id.tipo <- TIPO.tipo
            # imprimir(TIPO.tipo id.lexema)
            # print("D -> id TIPO ;")
            print(stackSymbols[-2]["tipo"], stackSymbols[-3]["lexema"])

            stackSymbols[-3]["tipo"] = stackSymbols[-2]["tipo"]

            return

            for statckzinho in stackSymbols:
                print(statckzinho)

        elif indiceRule == 7:  # feito
            # TIPO.tipo <- inteiro.tipo
            # print("TIPO -> inteiro")
            TIPO = stackSymbols.pop()
            stackSymbols.append({'lexema': 'TIPO', 'token': 'TIPO',
                                 'tipo': TIPO["tipo"], 'line': TIPO["line"], 'column': TIPO["column"]})

        elif indiceRule == 8:  # feito
            # TIPO.tipo <- real.tipo
            # print("TIPO -> real")
            TIPO = stackSymbols.pop()
            stackSymbols.append({'lexema': 'TIPO', 'token': 'TIPO',
                                 'tipo': TIPO["tipo"], 'line': 3, 'column': 9})

        elif indiceRule == 9:  # feito
            # TIPO.tipo <- literal.tipo
            # print("TIPO -> literal")
            TIPO = stackSymbols.pop()
            stackSymbols.append({'lexema': 'TIPO', 'token': 'TIPO',
                                 'tipo': TIPO["tipo"], 'line': 3, 'column': 9})

        elif indiceRule == 11:
            print("ES -> leia id;")
            # Verificar se o campo tipo do indentificador esta preenchido indicando a
            # declaração do identificador (execução da regra semântica de número 6).

            # Se sim, então:
            #   Se id.tipo = literal Imprimir ( scanf(“%s”, id.lexema); )
            #   Se id.tipo = inteiro Imprimir ( scanf(“%d”, &id.lexema); )
            #   Se id.tipo = real Imprimir ( scanf(“%lf”, &id.lexema); )
            # Caso Contrário:
            #   Emitir na tela “Erro: Variável não declarada”.

            # stackSymbols.pop()
            # id=stackSymbols.pop()
            # stackSymbols.pop()

            # print("ID ===== ", id)

            # if id["tipo"] != "":
            #     if id["tipo"] == "string":
            #          self.writeFile('scanf("%' + 'lf"), &{}\n'.format(id["lexema"]) + ");")

            # for statckzinho in stackSymbols:
            #     print(statckzinho)

        elif indiceRule == 12:  # feito
            # Gerar código para o comando escreva no arquivo objeto.
            # Imprimir ( printf(“ARG.lexema”); )
            # print("ES -> escreva ARG;")
            ARG = stackSymbols[-2]
            self.writeFile("printf({})\n".format(ARG["lexema"]))

        elif indiceRule == 13:  # feito
            # ARG.atributos <- literal.atributos (Copiar todos os atributos de literal para os atributos de ARG).
            # print("ARG -> literal")
            ARG = stackSymbols.pop()
            stackSymbols.append({'lexema': ARG["lexema"], 'token': ARG["token"],
                                 'tipo': ARG["tipo"], 'line': ARG["line"], 'column': ARG["column"]})

        elif indiceRule == 14:  # feito
            # ARG.atributos <- num.atributos (Copiar todos os atributos de literal para os atributos de ARG)
            # print("ARG -> num")
            ARG = stackSymbols.pop()
            stackSymbols.append({'lexema': ARG["lexema"], 'token': ARG["token"],
                                 'tipo': ARG["tipo"], 'line': ARG["line"], 'column': ARG["column"]})

        elif indiceRule == 15:
            # Verificar se o identificador foi declarado (execução da regra semântica de número 6).
            # Se sim, então:
            #   ARG.atributos <- id.atributos (copia todos os atributos de id para os de ARG).
            # Caso Contrário:
            #   Emitir na tela “Erro: Variável não declarada”.
            print("ARG -> id")

        elif indiceRule == 17:
            # Verificar se id foi declarado (execução da regra semântica de número 6). Se sim, então:
            #   Realizar verificação do tipo entre os operandos id e LD (ou seja, se ambos são do mesmo tipo).
            #   Se sim, então:
            #       Imprimir (id.lexema rcb.tipo LD.lexema) no arquivo objeto.
            #   Caso contrário emitir:”Erro: Tipos diferentes para atribuição”.
            # Caso contrário emitir “Erro: Variável não declarada”.
            print("CMD -> id rcb LD")

        elif indiceRule == 18:
            # Verificar se tipo dos operandos são equivalentes e diferentes de literal.
            # Se sim, então:
            #   Gerar uma variável numérica temporária Tx, em que x é um número gerado sequencialmente.
            #   LD.lexema <- Tx
            #   Imprimir (Tx = OPRD.lexema opm.tipo OPRD.lexema) no arquivo objeto.
            # Caso contrário emitir “Erro: Operandos com tipos incompatíveis”.
            print("LD -> OPRD opm OPRD")

        elif indiceRule == 19:  # feito
            # LD.atributos <- OPRD.atributos (Copiar todos os atributos de OPRD para os atributos de LD).
            # print("LD -> OPRD")
            LD = stackSymbols.pop()
            stackSymbols.append({'lexema': LD["lexema"], 'token': LD["token"],
                                 'tipo': LD["tipo"], 'line': LD["line"], 'column': LD["column"]})

        elif indiceRule == 20:
            print("OPRD -> id")
            # Verificar	se	o	identificador	está	declarado.
            # Se sim, então:
            #   OPRD.atributos	<- id.atributos
            # Caso contrário emitir “Erro: Variável não declarada”.

        elif indiceRule == 21:  # feito
            # OPRD.atributos	<- num.atributos (Copiar todos os atributos de num para os atributos de OPRD).
            # print("OPRD -> num")
            OPRD = stackSymbols.pop()
            stackSymbols.append({'lexema': OPRD["lexema"], 'token': OPRD["token"],
                                 'tipo': OPRD["tipo"], 'line': OPRD["line"], 'column': OPRD["column"]})

        elif indiceRule == 23:  # feita
            # Imprimir ( } ) no arquivo objeto.
            # print("COND -> CABECALHO CORPO")
            self.writeFile("}\n")

        elif indiceRule == 24:
            # Imprimir ( if ( EXP_R.lexema ) { ) no arquivo objeto.
            print("CABECALHO -> se ( EXP_R ) entao")
            EXP_R = "batata"
            aux = "if ( {} ) ".format(EXP_R) + "{\n"
            self.writeFile(aux)

        elif indiceRule == 25:
            print("EXP_R -> OPRD opr OPRD")
            # Verificar se os tipos de dados de OPRD são iguais ou equivalentes para a realização de comparação relacional.
            # Se sim, então:
            #   Gerar uma variável booleana temporária Tx, em que x é um número gerado sequencialmente.
            #   EXP_R.lexema <- Tx
            #   Imprimir (Tx = OPRD.lexema opr.tipo OPRD.lexema) no arquivo objeto.
            # Caso contrário emitir “Erro: Operandos com tipos incompatíveis”.

            # if OPRD1.tipo == OPRD2.tipo:
            #     tx = self.tx
            #     stackSymbols.append({'lexema': OPRD opr OPRD, 'token': "EXP_R", 'tipo': "")
            #     self.writeFile("T{} = {} {} {}".format(tx,OPRD1.lexema , opr.tipo , OPRD2.lexema))
            #     self.tx += 1
            # else:
            #     print("Err: Operandos com tipos incompatíveis")

    def resetFile(self):
        try:
            os.remove("codigo_objeto.c")
        except:
            pass

    def writeFile(self, line):
        with open("codigo_objeto.c", 'a') as f:
            f.write(line)
