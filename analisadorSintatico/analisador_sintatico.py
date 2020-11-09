from analisadorLexico.analisador_lexico import *
from util.goto import goto
from util.action import action


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
            print(stack)
            print(self.symbols[token]["token"])
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
                if actionResult[0] == "Err": #tratamento geral para identificar os erros

                    if str(actionResult[1]) == "5": #Faltou início
                        self.symbols.insert(token,{"lexema": "inicio" , "token": "inicio" , "tipo": "", "line": 1, "column": 0})
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha ", self.symbols[token]["line"], "\n\n")

                    elif str(actionResult[1]) == "6": #Faltou varinício
                        self.symbols.insert(token,{"lexema": "varinicio" , "token": "varinicio" , "tipo": "", "line": self.symbols[token-1]["line"], "column": self.symbols[token - 1]["column"]})
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"entre as linhas", self.symbols[token-1]["line"], " e ", self.symbols[token+1]["line"], self.symbols[token - 1]["column"], "\n\n")

                    elif str(actionResult[1]) == "7": #Falta ponto e vírgula
                        self.symbols.insert(token,{"lexema": ";" , "token": "PT_V" , "tipo": "" , "line": self.symbols[token-1]["line"], "column": self.symbols[token - 1]["column"] })
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")

                    elif str(actionResult[1]) == "8": #Ponto e vírgula inesperado
                        self.symbols.pop(token)
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")

                    elif str(actionResult[1]) == "9": #Token inesperado
                        self.symbols.pop(token)
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")

                    elif str(actionResult[1]) == "10": #Faltou fechar parentes
                        self.symbols.insert(token,{"lexema": ")" , "token": "FC_P" , "tipo": "" , "line": self.symbols[token-1]["line"], "column": self.symbols[token - 1]["column"] })
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")

                    elif str(actionResult[1]) == "11": #Faltou operador de atribuição
                        stack.append(29)
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")

                    elif str(actionResult[1]) == "12":
                        stack.append(45)
                        token+=1
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")

                    elif str(actionResult[1]) == "13": 
                        self.symbols.insert(token,{"lexema": "entao" , "token": "entao" , "tipo": "", "line": self.symbols[token-1]["line"], "column": self.symbols[token - 1]["column"] })
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")

                    elif str(actionResult[1]) == "14": 
                        stack.append(55)
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")

                    elif str(actionResult[1]) == "15": 
                        stack.append(40)
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")

                    elif str(actionResult[1]) == "16":
                        stack.append(45)
                        token+=1
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")
                        

                    elif str(actionResult[1]) == "17": #Comparação invalida
                        stack.append(55)
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")

                    elif str(actionResult[1]) == "18": #Faltou varfim
                        self.symbols.insert(token,{"lexema": "varfim" , "token": "varfim" , "tipo": "", "line": self.symbols[token-1]["line"], "column": self.symbols[token - 1]["column"] })
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")

                    elif str(actionResult[1]) == "19": #
                        stack.append(23)
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")

                    elif str(actionResult[1]) == "20": #
                        stack.pop()
                        token+=1
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")

                    elif str(actionResult[1]) == "21": #
                        stack.pop()
                        self.symbols.pop(token)
                        if self.symbols[token]["lexema"] == ";":
                            self.symbols.pop(token)
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")


                    elif str(actionResult[1]) == "22": #Faltou abrir parentes
                        self.symbols.insert(token,{"lexema": "(" , "token": "AB_P" , "tipo": "", "line": self.symbols[token-1]["line"], "column": self.symbols[token - 1]["column"] })
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")


                    elif str(actionResult[1]) == "23":
                        i=1
                        while (i<5):
                            if self.symbols[token+i]["token"] == "varfim":
                                print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")
                                stack.pop()
                                stack.pop()
                                stack.pop()
                                token += i #O ideal é pular até chegar no próximo id a ser declarado como variável. Tente ver qtos faltam até o ; e pule
                                if self.symbols[token+i]["lexema"] == "lit" or self.symbols[token+i]["lexema"] == "real" or self.symbols[token+i]["lexema"] == "inteiro":
                                    self.symbols.pop(token+i)
                                if self.symbols[token+i]["lexema"] == ";":
                                    self.symbols.pop(token+i)
                            i+=1
                        if i>5:
                            print("\n\n", Dicionario_de_erros["18"], "\n\n")

                    elif str(actionResult[1]) == "24":
                        stack.append(44)
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])], "na linha", self.symbols[token - 1]["line"], " e coluna ", self.symbols[token - 1]["column"], "\n\n")

                    elif str(actionResult[1]) == "25":
                        for i in range(len(rules[19][1])):
                            stack.pop()
                        state = stack[-1]
                        stack.append(goto(state, rules[19][0]))

                    # elif str(actionResult[1]) == "25":
                    #     stack.append(44)
                    #     print("\n\n", Dicionario_de_erros[str(actionResult[1])], "na linha", self.symbols[token - 1]["line"], " e coluna ", self.symbols[token - 1]["column"], "\n\n")


                    # elif str(actionResult[1]) == "24":
                    #     i=1
                    #     while (i<6):
                    #         if self.symbols[token+i]["token"] == "entao":
                    #             print("\n\n", Dicionario_de_erros[str(actionResult[1])], "\n\n")
                    #
                    #             token += i #O ideal é pular até chegar no próximo entao a ser declarado como variável. Tente ver qtos faltam até o ; e pule
                    #             if self.symbols[token+i]["lexema"] == "lit" or self.symbols[token+i]["lexema"] == "real" or self.symbols[token+i]["lexema"] == "inteiro":
                    #                 self.symbols.pop(token+i)
                    #             if self.symbols[token+i]["lexema"] == ";":
                    #                 self.symbols.pop(token+i)
                    #         i+=1
                    #     if i>5:
                    #         print("\n\n", Dicionario_de_erros["18"], "\n\n")

                    else:
                        print("\n\nERRO NÃO TRATADO ", Dicionario_de_erros[str(actionResult[1])], "\n\n")
                        stack.pop()
                        token+=1
                else:
                    print(state, self.symbols[token]["token"])
                    return