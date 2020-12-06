from analisadorLexico.analisador_lexico import *
from analisadorSemantico.analisador_semantico import SemanticAnalyzer

from analisadorSintatico.analisador_sintatico import syntacticAnalyzer

semantic = SemanticAnalyzer()
sintatico = syntacticAnalyzer(semantic)
sintatico.analyzer()
