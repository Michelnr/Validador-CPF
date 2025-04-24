# Este programa irá validar se um CPF é valido ou não.
cpf_lista = ['05788661706', '11501643797', '23392206709']

def digitos(digito):
    cont = 10
    soma = 0
    digito = 0
    for digito in primeiro_digito:
        soma += digito * cont
    digito = soma % 11

    return digito

for cpf in cpf_lista:
    digitos(cpf)