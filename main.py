from analisadorLexico.analisador_lexico import LexicalAnalyzer
from analisadorLexico.funcao_de_transicao import Dicionario_de_erros

if __name__ == "__main__":
    lexicalAnalyzer = LexicalAnalyzer()
    lexicalAnalyzer.analyzer("programa_fonte.txt")


print("\nTabela de símbolos")
for item in lexicalAnalyzer.symbleTable.symbol:
    print(lexicalAnalyzer.symbleTable.symbol[item])

print("\nErros")
for erro in lexicalAnalyzer.errors:
    print("Erro: " , erro[0] , " na linha: " , erro[1] , " e coluna: " , erro[2], Dicionario_de_erros[erro[3]])

print("\nTudo")
for symbol in lexicalAnalyzer.symbols:
    #print(symbol)
    print("lexema: " , symbol["lexema"] , " token: " , symbol["token"] , " tipo: " , symbol["tipo"])

# from analisadorSintatico.analisador_sintatico import syntacticAnalyzer
# lexicalAnalyzer = syntacticAnalyzer()
# lexicalAnalyzer.teste.analyzer("programa_fonte.txt")
# print()


# print("\nTabela de símbolos")
# for item in lexicalAnalyzer.teste.symbleTable.symbol:
#     print(lexicalAnalyzer.teste.symbleTable.symbol[item])