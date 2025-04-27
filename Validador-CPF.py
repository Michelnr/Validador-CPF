# Este programa irá validar se um CPF é valido ou não.
cpf_lista = ['28001238938', '05788661706', '11501643797', '23392206709']

# CPF é uma sequência de 11 dígitos, onde os dois últimos são dígitos verificadores
def validar_digitos(cpf, cont = 10):
    soma = 0
    for numero in cpf:
        soma += int(numero) * cont
        cont -= 1
    digito_cpf = soma % 11
    if digito_cpf == 0 or digito_cpf == 1:
        digito_cpf = 0
    else:
        digito_cpf = 11 - digito_cpf

    return digito_cpf

# Verifica se o CPF é válido
# CPF é válido se o primeiro dígito for igual ao décimo dígito e o segundo dígito for igual ao décimo primeiro dígito
for cpf in cpf_lista:
    primeiro_digito = validar_digitos(cpf[0:9])
    segundo_digito = validar_digitos(cpf[1:10])
    if primeiro_digito == int(cpf[9]) and segundo_digito == int(cpf[10]):
        print(f'O CPF {cpf} é válido.')
        if cpf[8] == "1": 
            print("Possíveis estados – DF, GO, MS, MT e TO\n")
        elif cpf[8] == "2":
            print ("Possíveis estados – AC, AM, AP, PA, RO e RR\n")
        elif cpf[8] == "3":
            print ("Possíveis estados – CE, MA e PI\n")
        elif cpf[8] == "4":
            print ("Possíveis estados – AL, PB, PE, RN\n")
        elif cpf[8] == "5":
            print ("Possíveis estados – BA e SE\n")
        elif cpf[8] == "6":
            print ("Possíveis estados – MG\n")
        elif cpf[8] == "7":
            print ("Possíveis estados – ES e RJ\n")
        elif cpf[8] == "8":
            print ("Possíveis estados – SP\n")
        elif cpf[8] == "9":
            print ("Possíveis estados – PR e SC\n")
        elif cpf[8] == "0":
            print ("Possíveis estados – RS\n")
    else:
        print(f'O CPF {cpf} é inválido.\n')