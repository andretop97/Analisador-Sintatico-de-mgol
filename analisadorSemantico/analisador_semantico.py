import os
from analisadorLexico import *
class SemanticAnalyzer:
    def __init__(self):
        self.pilha = []
        self.Tx = 0
        self.resetFile()

    def stackShift(self, token):
        self.pilha.append(token)

    def analyzer(self, rule, tokens):
        # Imprimir três linhas brancas no arquivo objeto;
        if rule == 5: #feito
            print("LV -> varfim ;")
            self.writeFile("\n\n\n")
            
        elif rule == 6:
            # id.tipo <- TIPO.tipo
            # imprimir(TIPO.tipo id.lexema)
            print("D -> id TIPO ;")


            # for token in tokens:
            #     print(token)
            # print("\n\n")
            
        elif rule == 7: #feito
            # TIPO.tipo <- inteiro.tipo
            print("TIPO -> inteiro")
            TIPO = self.pilha.pop()
            self.pilha.append({'lexema': 'TIPO', 'token': 'TIPO', 'tipo': TIPO["tipo"], 'line': TIPO["line"], 'column': TIPO["column"]})

            
        elif rule == 8: #feito
            # TIPO.tipo <- real.tipo
            print("TIPO -> real")
            TIPO = self.pilha.pop()
            self.pilha.append({'lexema': 'TIPO', 'token': 'TIPO', 'tipo': TIPO["tipo"], 'line': 3, 'column': 9})
            
        elif rule == 9: #feito
            # TIPO.tipo <- literal.tipo
            print("TIPO -> literal")
            TIPO = self.pilha.pop()
            self.pilha.append({'lexema': 'TIPO', 'token': 'TIPO', 'tipo': TIPO["tipo"], 'line': 3, 'column': 9})
            
        elif rule == 11:
            print("ES -> leia id;")
            # Verificar se o campo tipo do indentificador esta preenchido indicando a
            # declaração do identificador (execução da regra semântica de número 6).
            # Se sim, então:
            #   Se id.tipo = literal Imprimir ( scanf(“%s”, id.lexema); )
            #   Se id.tipo = inteiro Imprimir ( scanf(“%d”, &id.lexema); )
            #   Se id.tipo = real Imprimir ( scanf(“%lf”, &id.lexema); )
            # Caso Contrário:
            #   Emitir na tela “Erro: Variável não declarada”.
        elif rule == 12: #feito
            # Gerar código para o comando escreva no arquivo objeto.
            # Imprimir ( printf(“ARG.lexema”); )
            #print(tokens)
            print("ES -> escreva ARG;")
            ARG = self.pilha[-2]
            self.writeFile("printf({})\n".format(ARG["lexema"]))

        elif rule == 13: #feito
            # ARG.atributos <- literal.atributos (Copiar todos os atributos de literal para os atributos de ARG).
            print("ARG -> literal")
            ARG = self.pilha.pop()
            self.pilha.append({'lexema': ARG["lexema"], 'token': ARG["token"], 'tipo': ARG["tipo"], 'line': ARG["line"], 'column': ARG["column"]})
            
        elif rule == 14: #feito
            # ARG.atributos <- num.atributos (Copiar todos os atributos de literal para os atributos de ARG)
            print("ARG -> num")
            ARG = self.pilha.pop()
            self.pilha.append({'lexema': ARG["lexema"], 'token': ARG["token"], 'tipo': ARG["tipo"], 'line': ARG["line"], 'column': ARG["column"]})

        elif rule == 15:
            print("ARG -> id")
            # Verificar se o identificador foi declarado (execução da regra semântica de número 6).
            # Se sim, então:
            #   ARG.atributos <- id.atributos (copia todos os atributos de id para os de ARG).
            # Caso Contrário:
            #   Emitir na tela “Erro: Variável não declarada”.
        elif rule == 17:
            print("CMD -> id rcb LD")
            # Verificar se id foi declarado (execução da regra semântica de número 6). Se sim, então:
            #   Realizar verificação do tipo entre os operandos id e LD (ou seja, se ambos são do mesmo tipo).
            #   Se sim, então:
            #       Imprimir (id.lexema rcb.tipo LD.lexema) no arquivo objeto.
            #   Caso contrário emitir:”Erro: Tipos diferentes para atribuição”.
            # Caso contrário emitir “Erro: Variável não declarada”.
        elif rule == 18:
            print("LD -> OPRD opm OPRD")
            # Verificar se tipo dos operandos são equivalentes e diferentes de literal.
            # Se sim, então:
            #   Gerar uma variável numérica temporária Tx, em que x é um número gerado sequencialmente.
            #   LD.lexema <- Tx
            #   Imprimir (Tx = OPRD.lexema opm.tipo OPRD.lexema) no arquivo objeto.
            # Caso contrário emitir “Erro: Operandos com tipos incompatíveis”.

        elif rule == 19: #feito
            # LD.atributos <- OPRD.atributos (Copiar todos os atributos de OPRD para os atributos de LD).
            print("LD -> OPRD")
            LD = self.pilha.pop()
            self.pilha.append({'lexema': LD["lexema"], 'token': LD["token"], 'tipo': LD["tipo"], 'line': LD["line"], 'column': LD["column"]})

        elif rule == 20:
            print("OPRD -> id")
            # Verificar	se	o	identificador	está	declarado.
            # Se sim, então:
            #   OPRD.atributos	<- id.atributos
            # Caso contrário emitir “Erro: Variável não declarada”.

        elif rule == 21: #feito
            # OPRD.atributos	<- num.atributos (Copiar todos os atributos de num para os atributos de OPRD).
            print("OPRD -> num")
            OPRD = self.pilha.pop()
            self.pilha.append({'lexema': OPRD["lexema"], 'token': OPRD["token"], 'tipo': OPRD["tipo"], 'line': OPRD["line"], 'column': OPRD["column"]})

            
        elif rule == 23:
            print("COND -> CABECALHO CORPO")
            # Imprimir ( } ) no arquivo objeto.
        elif rule == 24:
            print("CABECALHO -> se ( EXP_R ) entao")
            # Imprimir ( if ( EXP_R.lexema ) { ) no arquivo objeto.
        elif rule == 25:
            print("EXP_R -> OPRD opr OPRD")
            # Verificar se os tipos de dados de OPRD são iguais ou equivalentes para a realização de comparação relacional.
            # Se sim, então:
            #   Gerar uma variável booleana temporária Tx, em que x é um número gerado sequencialmente.
            #   EXP_R.lexema <- Tx
            #   Imprimir (Tx = OPRD.lexema opr.tipo OPRD.lexema) no arquivo objeto.
            # Caso contrário emitir “Erro: Operandos com tipos incompatíveis”.

        else:
            print(rule)

    def resetFile(self):
        try:
            os.remove("codigo_objeto.c")
        except:
            pass

    def writeFile(self, line):
        with open("codigo_objeto.c", 'a') as f:
            f.write(line)
