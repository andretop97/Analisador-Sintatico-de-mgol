numeros = ["0","1","2","3","4","5","6","7","8","9"]
letras = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","x","X","y","Y","z","Z"]
outros_simbolos = [".", '"', "*", "{", "}", "<", ">", "=", "+", "-", "/", "\\", "(", ")", ";", ":", "_"," "]
alphabet = numeros + letras + outros_simbolos
estados =["s0","s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11","s12","s13","s14","s15","s16","s17","s18","s19"]
valid_states = ["s1", "s3", "s6", "s9", "s10", "s13", "s14", "s15", "s16", "s17", "s18", "s19", "s20", "s21", "s22","s23", "s24"]
initialState = ["s0","Estado inicial"]

rules = [
["P'", ["P"]],
["P", ["inicio", "V", "A"]],
["V",["varinicio", "LV"]],
["LV", ["D", "LV"]],
["LV", ["varinicio", ";"]],
["D", ["id", "TIPO", ";"]],
["TIPO", ["int"]],
["TIPO", ["real"]],
["TIPO", ["lit"]],
["A", ["ES", "A"]],
["ES", ["leia", "id", ";"]],
["ES", ["escreva", "ARG", ";"]],
["ARG", ["literal"]],
["ARG", ["num"]],
["ARG", ["id"]],
["A", ["CMD", "A"]],
["CMD", ["id", "rcb", "LD", ";"]],
["LD", ["OPRD", "opm", "OPRD"]],
["LD", ["OPRD"]],
["OPRD", ["id"]],
["OPRD", ["num"]],
["A", ["COND", "A"]],
["COND", ["CABEÇALHO", "CORPO"]],
["CABEÇALHO", ["se", "(", "EXP_R", ")", "então"]],
["EXP_R", ["OPRD", "opr", "OPRD"]],
["CORPO", ["ES", "CORPO"]],
["CORPO", ["CMD", "CORPO"]],
["CORPO", ["COND", "CORPO"]],
["CORPO", ["fimse"]],
["A", ["fim"]]
]
