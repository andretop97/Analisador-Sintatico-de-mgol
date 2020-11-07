from analisadorLexico.analisador_lexico import LexicalAnalyzer


class syntacticAnalyzer:
    def __init__(self):
        self.symbols = LexicalAnalyzer()

    def analyzer(self):
        a = "symbol"
        s = "state"
        print("du hast")
        while True:
            if self.action[s, a] == "shift t":
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
