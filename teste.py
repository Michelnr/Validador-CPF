# Este programa irá validar se um CPF é valido ou não.
cpf_lista = '28001238938' #['05788661706', '11501643797', '23392206709']

def digitos(cpf, cont = 10):
    soma = 0
    fat = 0
    while cont > 2:
        digito = cpf[fat]
        soma += digito * cont
        cont -= 1
    digito_cpf = soma % 11

    return digito_cpf

cpf_lista = int(cpf_lista)
digitos(cpf_lista)