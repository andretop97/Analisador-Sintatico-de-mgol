from analisadorLexico.analisador_lexico import LexicalAnalyzer
from analisadorSintatico.goto import goto
from analisadorSintatico.action import action
from util.grammar import rules


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

            actionResult = action(state, self.symbols[token]["token"])
            if actionResult[0] == "s":
                stack.append(actionResult[1])
                token += 1


            elif actionResult[0] == "r":
                indice = actionResult[1] - 1
                for i in range(len(rules[indice][1])):
                    stack.pop()
                state = stack[-1]
                stack.append(goto(state, rules[indice][0]))
                print("regra ", indice + 1 , " : ", rules[indice][0], "->", *rules[indice][1])

            elif actionResult[0] == "ACC":
                print("regra  1  : ", rules[0][0], "->", *rules[0][1])
                break
            else:
                print("chama uma rotina de redução de erro")
                break
