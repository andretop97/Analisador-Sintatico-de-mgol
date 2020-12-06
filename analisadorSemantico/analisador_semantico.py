import os
class SemanticAnalyzer:
    def __init__(self):
        self.stack = []
        self.tx = 0
        self.resetFile()


    def stackShift(self, token):
        self.stack.append(token)

    def analyzer(self, indiceRule, lenRightRule):

        if indiceRule == 2:

            self.writeFile("}")

        # Imprimir três linhas brancas no arquivo objeto;
        elif indiceRule == 5: #feito
            # print("LV -> varfim ;")
            self.writeFile("\n\n\n")
            self.stack.pop()
            self.stack.append({'lexema': "LV", 'token': "", 'tipo': ""})
            
        elif indiceRule == 6: #feita
            # id.tipo <- TIPO.tipo
            # imprimir(TIPO.tipo id.lexema)
            # print("D -> id TIPO ;")
            # print(self.stack[-2]["tipo"], self.stack[-3]["lexema"])

            self.stack[-3]["tipo"]=self.stack[-2]["tipo"]

            self.stack.pop()
            self.stack.pop()

        elif indiceRule == 7: #feito
            # TIPO.tipo <- inteiro.tipo
            # print("TIPO -> inteiro")
            TIPO = self.stack.pop()
            self.stack.append({'lexema': 'TIPO', 'token': 'TIPO', 'tipo': TIPO["tipo"], 'line': TIPO["line"], 'column': TIPO["column"]})

            
        elif indiceRule == 8: #feito
            # TIPO.tipo <- real.tipo
            # print("TIPO -> real")
            TIPO = self.stack.pop()
            self.stack.append({'lexema': 'TIPO', 'token': 'TIPO', 'tipo': TIPO["tipo"], 'line': TIPO["line"], 'column': TIPO["column"]})
            
        elif indiceRule == 9: #feito
            # TIPO.tipo <- literal.tipo
            # print("TIPO -> literal")
            TIPO = self.stack.pop()
            self.stack.append({'lexema': 'TIPO', 'token': 'TIPO', 'tipo': TIPO["tipo"], 'line': TIPO["line"], 'column': TIPO["column"]})
            
        elif indiceRule == 11: #feito
            # print("ES -> leia id;")
            # Verificar se o campo tipo do indentificador esta preenchido indicando a
            # declaração do identificador (execução da regra semântica de número 6).

            # Se sim, então:
            #   Se id.tipo = literal Imprimir ( scanf(“%s”, id.lexema); )
            #   Se id.tipo = inteiro Imprimir ( scanf(“%d”, &id.lexema); )
            #   Se id.tipo = real Imprimir ( scanf(“%lf”, &id.lexema); )
            # Caso Contrário:
            #   Emitir na tela “Erro: Variável não declarada”.

            self.stack.pop()
            id = self.stack.pop()
            self.stack.pop()
            self.stack.append({'lexema': "ES", 'token': "", 'tipo': ""})

            if id["tipo"] != "":
                if id["tipo"] == "literal":
                    self.writeFile('scanf("%s", {}'.format(id["lexema"]) + ");\n")
                elif id["tipo"] == "int":
                    self.writeFile('scanf("%d", &{}'.format(id["lexema"]) + ");\n")
                elif id["tipo"] == "double":
                    self.writeFile('scanf("%lf", &{}'.format(id["lexema"]) + ");\n")
            else:
                print("Erro: Variável não declarada")
        elif indiceRule == 12: #feito
            # Gerar código para o comando escreva no arquivo objeto.
            # Imprimir ( printf(“ARG.lexema”); )
            # print("ES -> escreva ARG;")

            self.stack.pop()
            ARG = self.stack.pop()
            self.stack.pop()
            self.writeFile("printf({})\n".format(ARG["lexema"]))
            self.stack.append({'lexema': "ES", 'token': "", 'tipo': ""})

        elif indiceRule == 13: #feito
            # ARG.atributos <- literal.atributos (Copiar todos os atributos de literal para os atributos de ARG).
            # print("ARG -> literal")
            ARG = self.stack.pop()
            self.stack.append(ARG)
            
        elif indiceRule == 14: #feito
            # ARG.atributos <- num.atributos (Copiar todos os atributos de literal para os atributos de ARG)
            # print("ARG -> num")
            ARG = self.stack.pop()
            self.stack.append(ARG)

        elif indiceRule == 15: #feito
            # Verificar se o identificador foi declarado (execução da regra semântica de número 6).
            # Se sim, então:
            #   ARG.atributos <- id.atributos (copia todos os atributos de id para os de ARG).
            # Caso Contrário:
            #   Emitir na tela “Erro: Variável não declarada”.
            # print("ARG -> id")
            id = self.stack.pop()
            if(id["tipo"] != ""):
                self.stack.append(id)
            else:
                print("Erro: Variável não declarada")
                self.stack.append(id)

        elif indiceRule == 17: #feito
            # Verificar se id foi declarado (execução da regra semântica de número 6). Se sim, então:
            #   Realizar verificação do tipo entre os operandos id e LD (ou seja, se ambos são do mesmo tipo).
            #   Se sim, então:
            #       Imprimir (id.lexema rcb.tipo LD.lexema) no arquivo objeto.
            #   Caso contrário emitir:”Erro: Tipos diferentes para atribuição”.
            # Caso contrário emitir “Erro: Variável não declarada”.
            # print("CMD -> id rcb LD;")

            self.stack.pop()
            LD = self.stack.pop()
            rcb = self.stack.pop()
            id = self.stack.pop()

            if id["tipo"] != "" and LD["tipo"] != "":
                if id["tipo"] == LD["tipo"]:
                    self.writeFile("{} {} {}\n".format(id["lexema"], rcb["tipo"], LD["lexema"]))
                    self.stack.append({'lexema': "CMD", 'token': "Num", 'tipo': id['tipo']})
                elif id["tipo"] == 'double' and LD["tipo"] == 'int':
                    self.writeFile("{} {} {}\n".format(id["lexema"], rcb["tipo"], LD["lexema"]))
                    self.stack.append({'lexema': "CMD", 'token': "Num", 'tipo': id['tipo']})
                else:
                    self.stack.append({'lexema': "CMD", 'token': "Num", 'tipo': id['tipo']})
                    print("Erro: Tipos diferentes para atribuição")
            else:
                self.stack.append({'lexema': "CMD", 'token': "Num", 'tipo': id['tipo']})
                print("Erro: Variável não declarada")


        elif indiceRule == 18: #feito
            # Verificar se tipo dos operandos são equivalentes e diferentes de literal.
            # Se sim, então:
            #   Gerar uma variável numérica temporária Tx, em que x é um número gerado sequencialmente.
            #   LD.lexema <- Tx
            #   Imprimir (Tx = OPRD.lexema opm.tipo OPRD.lexema) no arquivo objeto.
            # Caso contrário emitir “Erro: Operandos com tipos incompatíveis”.
            # print("LD -> OPRD opm OPRD")

            OPRD2 = self.stack.pop()
            opm = self.stack.pop()
            OPRD1 = self.stack.pop()

            if OPRD1["tipo"] != "literal" and OPRD2["tipo"] != "literal" and OPRD1["tipo"] == OPRD2["tipo"]:
                tx = self.tx
                self.writeFile("T{} = {} {} {}\n".format(tx, OPRD1["lexema"], opm["tipo"], OPRD2["lexema"])),
                self.stack.append({'lexema': "T{}".format(tx), 'token': "", 'tipo': OPRD1["tipo"]})
                self.tx += 1
            elif  OPRD1["tipo"] == "" or OPRD2["tipo"] == "":
                self.stack.append({'lexema': "LD", 'token': "", 'tipo': OPRD1["tipo"]})
            else:
                print("Erro: Operandos com tipos incompatíveis")
                self.stack.append({'lexema': "LD", 'token': "", 'tipo': OPRD1["tipo"]})

        elif indiceRule == 19: #feito
            # LD.atributos <- OPRD.atributos (Copiar todos os atributos de OPRD para os atributos de LD).
            # print("LD -> OPRD")
            LD = self.stack.pop()
            self.stack.append(LD)

        elif indiceRule == 20: #feito
            # Verificar	se	o	identificador	está	declarado.
            # Se sim, então:
            #   OPRD.atributos	<- id.atributos
            # Caso contrário emitir “Erro: Variável não declarada”.
            # print("OPRD -> id")

            id = self.stack.pop()

            if id["tipo"] != "":
                self.stack.append(id)
            else:
                print("Erro: Variável não declarada")
                self.stack.append(id)

        elif indiceRule == 21: #feito
            # OPRD.atributos	<- num.atributos (Copiar todos os atributos de num para os atributos de OPRD).
            # print("OPRD -> num")

            OPRD = self.stack.pop()
            self.stack.append(OPRD)

        elif indiceRule == 23: #feita
            # Imprimir ( } ) no arquivo objeto.
            # print("COND -> CABECALHO CORPO")
            self.stack.pop()
            self.stack.pop()
            self.writeFile("}\n")
            self.stack.append({'lexema': "COND", 'token': "", 'tipo': ""})

        elif indiceRule == 24: #feito
            # Imprimir ( if ( EXP_R.lexema ) { ) no arquivo objeto.
            # print("CABECALHO -> se ( EXP_R ) entao")

            self.stack.pop()
            self.stack.pop()
            EXP_R = self.stack.pop()
            self.stack.pop()
            self.stack.pop()
            aux = "if ( {} ) ".format(EXP_R["lexema"]) + "{\n"
            self.writeFile(aux)
            self.stack.append({'lexema': "CABECALHO", 'token': "", 'tipo': ""})

        elif indiceRule == 25: #feito
            # Verificar se os tipos de dados de OPRD são iguais ou equivalentes para a realização de comparação relacional.
            # Se sim, então:
            #   Gerar uma variável booleana temporária Tx, em que x é um número gerado sequencialmente.
            #   EXP_R.lexema <- Tx
            #   Imprimir (Tx = OPRD.lexema opr.tipo OPRD.lexema) no arquivo objeto.
            # Caso contrário emitir “Erro: Operandos com tipos incompatíveis”.
            # print("EXP_R -> OPRD opr OPRD")

            OPRD2 = self.stack.pop()
            opr = self.stack.pop()
            OPRD1 = self.stack.pop()

            if True:
                tx = self.tx
                self.stack.append({'lexema': "T{}".format(tx), 'token': "boolean", 'tipo': "boolean"})
                self.writeFile("T{} = {} {} {}\n".format(tx, OPRD1["lexema"], opr["tipo"], OPRD2["lexema"]))
                self.tx += 1

    def resetFile(self):
        try:
            os.remove("codigo_objeto.c")
        except:
            pass

    def writeFile(self, line):
        with open("codigo_objeto.c", 'a') as f:
            f.write(line)
