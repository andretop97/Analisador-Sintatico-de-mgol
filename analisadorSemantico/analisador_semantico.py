import os
class SemanticAnalyzer:
    def __init__(self):
        self.stack = []
        self.tx = 0
        self.resetFile()
        self.Buffer = ""
        self.indentation = 1


    def stackShift(self, token):
        self.stack.append(token)

    def analyzer(self, indiceRule, lenRightRule):

        if indiceRule == 2:
            header = "#include<stdio.h> \ntypedef char literal[256]; \nvoid main(void) { \n\t/*----Variaveis temporarias----*/\n"
            for x in range(self.tx):
                header += "{}int T{};\n".format(self.indentation * "\t", x)
            header += "{}/*------------------------------*/\n".format(self.indentation * "\t")
            self.Buffer = header + self.Buffer
            self.writeBuffer("}")
            self.writeFile()
            

        # Imprimir três linhas brancas no arquivo objeto;
        elif indiceRule == 5: #feito
            # print("LV -> varfim ;")
            self.writeBuffer("\n\n\n")
            varfim = self.stack.pop()
            self.stack.append({'lexema': "LV", 'token': varfim["token"], 'tipo': varfim["tipo"], 'line': varfim["line"], 'column': varfim["line"]})
            
        elif indiceRule == 6: #feita
            # id.tipo <- TIPO.tipo
            # imprimir(TIPO.tipo id.lexema)
            # print("D -> id TIPO ;")
            # print(self.stack[-2]["tipo"], self.stack[-3]["lexema"])

            self.stack[-3]["tipo"]=self.stack[-2]["tipo"]
            self.writeBuffer("{}{} {} ;\n".format(self.indentation * "\t",self.stack[-2]["tipo"], self.stack[-3]["lexema"]))
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

            PT_V = self.stack.pop()
            id = self.stack.pop()
            self.stack.pop()
            self.stack.append({'lexema': "ES", 'token': "", 'tipo': "", 'line': id["line"], 'column': id["column"]})

            if id["tipo"] != "":
                if id["tipo"] == "literal":
                    self.writeBuffer('{}scanf("%s", {}'.format(self.indentation * "\t", id["lexema"]) + ");\n")
                elif id["tipo"] == "int":
                    self.writeBuffer('{}scanf("%d", &{}'.format(self.indentation * "\t", id["lexema"]) + ");\n")
                elif id["tipo"] == "double":
                    self.writeBuffer('{}scanf("%lf", &{}'.format(self.indentation * "\t", id["lexema"]) + ");\n")
            else:
                print("Erro Semântico na linha {}: Variável não declarada".format( PT_V["line"]))
        elif indiceRule == 12: #feito
            # Gerar código para o comando escreva no arquivo objeto.
            # Imprimir ( printf(“ARG.lexema”); )
            # print("ES -> escreva ARG;")

            self.stack.pop()
            ARG = self.stack.pop()
            self.stack.pop()
            if ARG["tipo"] == 'literal':
                self.writeBuffer('{}printf("%s", {});\n'.format(self.indentation * "\t", ARG["lexema"]))
            elif ARG["tipo"] == 'int':
                self.writeBuffer('{}printf("%d", {});\n'.format(self.indentation * "\t", ARG["lexema"]))
            elif ARG["tipo"] == 'double':
                self.writeBuffer('{}printf("%lf", {});\n'.format(self.indentation * "\t", ARG["lexema"]))
            else:
                self.writeBuffer('{}printf({});\n'.format(self.indentation * "\t", ARG["lexema"]))
            self.stack.append({'lexema': "ES", 'token': "", 'tipo': "", 'line': ARG["line"], 'column': ARG['column']})

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
                print("Erro Semântico na linha {}: Variável não declarada".format(id['line']))
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
                    self.writeBuffer("{}{} {} {};\n".format(self.indentation * "\t", id["lexema"], rcb["tipo"], LD["lexema"]))
                    self.stack.append({'lexema': "CMD", 'token': "Num", 'tipo': id['tipo'], 'line': id['line'], 'column': id['column']})
                elif id["tipo"] == 'double' and LD["tipo"] == 'int':
                    self.writeBuffer("{}{} {} {};\n".format(self.indentation * "\t", id["lexema"], rcb["tipo"], LD["lexema"]))
                    self.stack.append({'lexema': "CMD", 'token': "Num", 'tipo': id['tipo'], 'line': id['line'], 'column': id['column']})
                else:
                    self.stack.append({'lexema': "CMD", 'token': "Num", 'tipo': id['tipo'], 'line': id['line'], 'column': id['column']})
                    print("Erro Semântico na linha {}: Tipos diferentes para atribuição".format(rcb["line"]))
            else:
                self.stack.append({'lexema': "CMD", 'token': "Num", 'tipo': id['tipo'], 'line': id['line'], 'column': id['column']})
                print("Erro Semântico na linha {}: Variável não declarada".format(rcb["line"]))

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
                self.writeBuffer("{}T{} = {} {} {};\n".format(self.indentation * "\t", tx, OPRD1["lexema"], opm["tipo"], OPRD2["lexema"])),
                self.stack.append({'lexema': "T{}".format(tx), 'token': "", 'tipo': OPRD1["tipo"], 'line': OPRD1["line"], 'column': OPRD1["column"]})
                self.tx += 1
            elif OPRD1["tipo"] == "" or OPRD2["tipo"] == "":
                self.stack.append({'lexema': "LD", 'token': "", 'tipo': OPRD1["tipo"], 'line': OPRD1["line"], 'column': OPRD1["column"]})
            else:
                print("Erro Semêntico na linha {}: Operandos com tipos incompatíveis".format(opm['line']))
                self.stack.append({'lexema': "LD", 'token': "", 'tipo': OPRD1["tipo"], 'line': OPRD1["line"], 'column': OPRD1["column"]})

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
                self.stack.append(id)

        elif indiceRule == 21: #feito
            # OPRD.atributos	<- num.atributos (Copiar todos os atributos de num para os atributos de OPRD).
            # print("OPRD -> num")

            OPRD = self.stack.pop()
            self.stack.append(OPRD)

        elif indiceRule == 23: #feita
            # Imprimir ( } ) no arquivo objeto.
            # print("COND -> CABECALHO CORPO")
            CABECALHO = self.stack.pop()
            CORPO = self.stack.pop()
            self.indentation -= 1
            string = "{}".format(self.indentation * "\t") + "}\n"
            self.writeBuffer(string)
            self.stack.append({'lexema': "COND", 'token': "", 'tipo': "", 'line': CABECALHO["line"], 'column': CABECALHO["column"]})

        elif indiceRule == 24: #feito
            # Imprimir ( if ( EXP_R.lexema ) { ) no arquivo objeto.
            # print("CABECALHO -> se ( EXP_R ) entao")

            self.stack.pop()
            self.stack.pop()
            EXP_R = self.stack.pop()
            self.stack.pop()
            self.stack.pop()
            string = "{}if ( {} )\n {}".format(self.indentation * "\t", EXP_R["lexema"], self.indentation * "\t") + "{\n"
            self.indentation += 1
            self.writeBuffer(string)
            self.stack.append({'lexema': "CABECALHO", 'token': "", 'tipo': "", 'line': EXP_R["line"], 'column': EXP_R["column"]})

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

            if OPRD1["tipo"] != '' and OPRD2["tipo"] != "":
                if (OPRD1["tipo"] ==  "int" or OPRD1["tipo"] == 'double') and (OPRD2["tipo"] ==  "int" or OPRD2["tipo"] == 'double'):
                    tx = self.tx
                    self.stack.append({'lexema': "T{}".format(tx), 'token': "boolean", 'tipo': "boolean", 'line': OPRD1["line"], 'column': OPRD1["column"]})
                    self.writeBuffer("{}T{} = {} {} {};\n".format(self.indentation * "\t", tx, OPRD1["lexema"], opr["tipo"], OPRD2["lexema"]))
                    self.tx += 1
                else:
                    self.stack.append({'lexema': "EXP_R", 'token': "boolean", 'tipo': "boolean", 'line': OPRD1["line"], 'column': OPRD1["column"]})
                    print("Erro Semêntico na linha {}: Operandos com tipos incompatíveis".format(opr['line']))

            else:
                print("Erro Semântico na linha {}: Variável não declarada".format(opr["line"]))


    def resetFile(self):
        try:
            os.remove("codigo_objeto.c")
        except:
            pass

    def writeBuffer(self, line):
        self.Buffer += line


    def writeFile(self):
        with open("codigo_objeto.c", 'a') as f:
            f.write(self.Buffer)