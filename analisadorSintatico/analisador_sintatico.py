from analisadorLexico.analisador_lexico import LexicalAnalyzer


class syntacticAnalyzer:
    def __init__(self):
        self.symbols = self.getLexicalSymbols()

    def getLexicalSymbols(self):
        lexicalAnalyzer = LexicalAnalyzer()
        lexicalAnalyzer.analyzer("programa_fonte.txt")
        return lexicalAnalyzer.symbols


    def analyzer(self):
        a = 0
        s = "state"
        while True:
            if self.action[s, self.symbols[a]] == "shift t":
                print("empilha a do indice t")

            ##proximo simbolo da entrada
            elif self.action[s, a] == "reduce":

                print("empilha simbolos B da pilha")
                print("faz o estado t ser o topo da pilha")
                print("empilha GOTO[ t , A ]")
                print("imprime A -> B")
            elif self.action[s, a] == "accept":
                break
            else:
                print("chama uma rotina de redução de erro")

    def action(self, state, Symbol):
        return ['shift', 'reduce', 'accept', 'error']

    def goto(self, t, A):
        print("batata")


if __name__ == "__main__":
    batata = syntacticAnalyzer()
    print(batata.batata)
