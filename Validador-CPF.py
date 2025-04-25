# Este programa irá validar se um CPF é valido ou não.
cpf_lista = '28001238938' #['05788661706', '11501643797', '23392206709']

def digitos(cpf, cont = 10):
    soma = 0
    digito = 0
    cpf = int(cpf)
    for digito in cpf:
        soma += digito * cont
        cont -= 1
    digito = soma % 11

    return digito

for cpf in cpf_lista:
    if cpf[0] == "0":
        cpf = cpf[0:8]
        digitos(cpf, cont = 9)
    else:
        cpf = cpf[0:9]
        digitos(cpf)