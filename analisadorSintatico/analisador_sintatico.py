from analisadorLexico.analisador_lexico import *
from util.goto import goto
from util.action import action
from analisadorSemantico.analisador_semantico import SemanticAnalyzer


class syntacticAnalyzer:

    def __init__(self):
        self.symbols = self.getLexicalSymbols()
        self.semanticAnalyzer = SemanticAnalyzer()

    def getLexicalSymbols(self):
        lexicalAnalyzer = LexicalAnalyzer()
        lexicalAnalyzer.analyzer("programa_fonte.txt")
        return lexicalAnalyzer.symbols

    def analyzer(self):
        token = 0
        stack = [0]
        while True:
            # print(stack)
            # print(self.symbols[token]["token"])
            state = stack[-1]
            actionResult = action(state, self.symbols[token]["token"])
            if actionResult[0] == "s":
                stack.append(actionResult[1])
                self.semanticAnalyzer.stackShift(self.symbols[token])
                token += 1

            elif actionResult[0] == "r":
                indice = actionResult[1] - 1
                for i in range(len(rules[indice][1])):
                    stack.pop()
                state = stack[-1]
                stack.append(goto(state, rules[indice][0]))

                # print("regra ", indice + 1 , " : ", rules[indice][0], "->", *rules[indice][1])
                self.semanticAnalyzer.analyzer(indice + 1, self.symbols[token - len(rules[indice][1]):token])

            elif actionResult[0] == "ACC":
                # print("regra  1  : ", rules[0][0], "->", *rules[0][1])
                break
            else:

                if self.symbols[token]["token"] in Dicionario_de_erros:

                    if self.symbols[token]["token"] == "1":
                        self.symbols.insert(token,{"lexema": self.symbols[token]["lexema"] , "token": "id" , "tipo": "", "line": self.symbols[token]["line"], "column": self.symbols[token]["column"]})
                        self.symbols.pop(token+1)
                        print("\n\n", Dicionario_de_erros["1"], "\"", self.symbols[token]["lexema"], "\" " ,"na linha ", self.symbols[token]["line"], "\n\n")
                        if stack[-1] in [18, 54, 55]:
                            token+=1
                        elif stack[-1] in [29]:
                            stack.pop()
                            stack.pop()
                            stack.append(7)
                            token+=1

                    elif self.symbols[token]["token"] == "3":
                        self.symbols.insert(token,{"lexema": self.symbols[token]["lexema"] , "token": "Literal" , "tipo": "", "line": self.symbols[token]["line"], "column": self.symbols[token]["column"]})
                        self.symbols.pop(token+1)
                        print("\n\n", Dicionario_de_erros["3"], "\"", self.symbols[token]["lexema"], "\" " ,"na linha ", self.symbols[token]["line"], "\n\n")


                    elif self.symbols[token]["token"] == "4":
                        self.symbols.insert(token,{"lexema": self.symbols[token]["lexema"] , "token": "Comentário" , "tipo": "", "line": self.symbols[token]["line"], "column": self.symbols[token]["column"]})
                        self.symbols.pop(token+1)
                        print("\n\n", Dicionario_de_erros["4"], "\"", self.symbols[token]["lexema"], "\" " ,"na linha ", self.symbols[token]["line"], "\n\n")
                      
                
                
                
                elif self.symbols[token]["token"] == "Comentário":
                    token+=1   

                elif actionResult[0] == "Err": #tratamento geral para identificar os erros

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
                        #self.symbols.insert(token,{"lexema": ")" , "token": "FC_P" , "tipo": "" , "line": self.symbols[token-1]["line"], "column": self.symbols[token - 1]["column"] })
                        for i in range(len(rules[20][1])):
                            stack.pop()
                        state = stack[-1]
                        stack.append(goto(state, rules[20][0]))
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
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", int(self.symbols[token - 1]["line"])+1 ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")

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
                        for i in range(len(rules[5][1])):
                            stack.pop()
                        state = stack[-1]
                        stack.append(goto(state, rules[5][0]))
                        token+=1
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")

                    elif str(actionResult[1]) == "24":
                        stack.append(44)
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])], "na linha", self.symbols[token - 1]["line"], " e coluna ", self.symbols[token - 1]["column"], "\n\n")

                    elif str(actionResult[1]) == "25":
                        for i in range(len(rules[19][1])):
                            stack.pop()
                        state = stack[-1]
                        stack.append(goto(state, rules[19][0]))


                    elif str(actionResult[1]) == "26":
                        stack.append(45)
                        #token+=1
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")

                    elif str(actionResult[1]) == "27": #Faltou fim
                        self.symbols.insert(token, {"lexema": "fim" , "token": "fim" , "tipo": "", "line": self.symbols[token-1]["line"], "column": self.symbols[token - 1]["column"]})
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token-1]["line"], "\n\n")
                        if self.symbols[-2]["token"] == "Estado inicial":
                            self.symbols.pop(token+1)

                    elif str(actionResult[1]) == "28":
                        self.symbols.insert(token,{"lexema": ")" , "token": "FC_P" , "tipo": "", "line": self.symbols[token-1]["line"], "column": self.symbols[token - 1]["column"] })
                    
                    elif str(actionResult[1]) == "29": #Faltou fim
                        self.symbols.insert(token,{"lexema": "fimse" , "token": "fimse" , "tipo": "", "line": self.symbols[token-1]["line"], "column": self.symbols[token - 1]["column"] })
                        print("\n\n", Dicionario_de_erros[str(actionResult[1])],"na linha", self.symbols[token - 1]["line"] ," e coluna ",self.symbols[token - 1]["column"] , "\n\n")

                    


                    else:
                        print("\n\nERRO NÃO TRATADO ", Dicionario_de_erros[str(actionResult[1])], "\n\n")
                        stack.pop()
                        token+=1
                else:
                    print(state, self.symbols[token]["token"])
                    return