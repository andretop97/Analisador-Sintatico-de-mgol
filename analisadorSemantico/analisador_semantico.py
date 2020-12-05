class SemanticAnalyzer:
    def __init__(self):
        self.Tx = 0

    def analyzer(self, rule, tokens):
        if(rule == 5):
            print("LV -> varfim")
            #Imprimir três linhas brancas no arquivo objeto;
        if(rule == 6):
            print("D -> id TIPO ;")
            #id.tipo <- TIPO.tipo
            #imprimir(TIPO.tipo id.lexema)
        if(rule == 7):
            print("TIPO -> inteiro")
            # TIPO.tipo <- inteiro.tipo
        if (rule == 8):
            print("TIPO -> real")
            # TIPO.tipo <- real.tipo
        if (rule == 9):
            print("TIPO -> literal")
            # TIPO.tipo <- literal.tipo
        if (rule == 11):
            print("ES -> leia id;")
            #Verificar se o campo tipo do indentificador esta preenchido indicando a
            #declaração do identificador (execução da regra semântica de número 6).
            #Se sim, então:
            #   Se id.tipo = literal Imprimir ( scanf(“%s”, id.lexema); )
            #   Se id.tipo = inteiro Imprimir ( scanf(“%d”, &id.lexema); )
            #   Se id.tipo = real Imprimir ( scanf(“%lf”, &id.lexema); )
            #Caso Contrário:
            #   Emitir na tela “Erro: Variável não declarada”.
        if (rule == 12):
            print("ES -> escreva ARG;")
            #Gerar código para o comando escreva no arquivo objeto.
            #Imprimir ( printf(“ARG.lexema”); )
        if (rule == 13):
            print("ARG -> literal")
            #ARG.atributos ß literal.atributos (Copiar todos os atributos de literal para os atributos de ARG).
        if (rule == 14):
            print()
        if (rule == 15):
            print()
        if (rule == 17):
            print()
        if (rule == 18):
            print()
        if (rule == 19):
            print()
        if (rule == 20):
            print()
        if (rule == 21):
            print()
        if (rule == 23):
            print()
        if (rule == 24):
            print()
        if (rule == 25):
            print()
        for token in tokens:
            print(token)
        print("\n\n")