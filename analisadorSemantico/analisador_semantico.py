class SemanticAnalyzer:
    def __init__(self):
        self.pilha = []
        self.Tx = 0

    def stackShift(self, token):
        self.pilha.append(token)

    def analyzer(self, rule, tokens):
        if rule == 5:
            print("LV -> varfim ;")
            # Imprimir três linhas brancas no arquivo objeto;
        elif rule == 6:
            print("D -> id TIPO ;")

            for token in tokens:
                print(token)
            print("\n\n")
            # id.tipo <- TIPO.tipo
            # imprimir(TIPO.tipo id.lexema)
        elif rule == 7:
            print("TIPO -> inteiro")
            TIPO = self.pilha.pop()
            self.pilha.append({'lexema': 'TIPO', 'token': 'TIPO', 'tipo': TIPO["tipo"], 'line': 3, 'column': 9})
            for token in self.pilha:
                print(token)
            print("\n\n")
            # TIPO.tipo <- inteiro.tipo
        elif rule == 8:
            print("TIPO -> real")
            # TIPO.tipo <- real.tipo
        elif rule == 9:
            print("TIPO -> literal")
            # TIPO.tipo <- literal.tipo
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
        elif rule == 12:
            print("ES -> escreva ARG;")
            # Gerar código para o comando escreva no arquivo objeto.
            # Imprimir ( printf(“ARG.lexema”); )
        elif rule == 13:
            print("ARG -> literal")
            # ARG.atributos <- literal.atributos (Copiar todos os atributos de literal para os atributos de ARG).
        elif rule == 14:
            print("ARG -> num")
            # ARG.atributos <- num.atributos (Copiar todos os atributos de literal para os atributos de ARG)
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
        elif rule == 19:
            print("LD -> OPRD")
            # LD.atributos <- OPRD.atributos (Copiar todos os atributos de OPRD para os atributos de LD).
        elif rule == 20:
            print("OPRD -> id")
            # Verificar	se	o	identificador	está	declarado.
            # Se sim, então:
            #   OPRD.atributos	<- id.atributos
            # Caso contrário emitir “Erro: Variável não declarada”.
        elif rule == 21:
            print("OPRD -> num")
            # OPRD.atributos	<- num.atributos (Copiar todos os atributos de num para os atributos de OPRD).
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
