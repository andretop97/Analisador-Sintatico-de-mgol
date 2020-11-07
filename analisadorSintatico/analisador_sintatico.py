from analisadorLexico.analisador_lexico import LexicalAnalyzer
from analisadorSintatico.goto import goto
from analisadorSintatico.action import action


class syntacticAnalyzer:
    def __init__(self):
        self.symbols = self.getLexicalSymbols()

    def getLexicalSymbols(self):
        lexicalAnalyzer = LexicalAnalyzer()
        lexicalAnalyzer.analyzer("programa_fonte.txt")
        return lexicalAnalyzer.symbols


    def analyzer(self):
        token = 0
        stack = [0]
        while True:
            state = stack[-1]
            action = action(state, self.symbols[token])
            if action[0] == "s":
                stack.append(action[1])
                token += 1

            elif action[0] == "r":
                for i in range("tamanho da derivação da gramatica"):
                    stack.pop()
                state = stack[-1]
                goto(state, self.symbols[token])
                print("empilha GOTO[ t , A ]")
                print("imprime A -> B")
            elif action[0] == "ACC":
                break
            else:
                print("chama uma rotina de redução de erro")