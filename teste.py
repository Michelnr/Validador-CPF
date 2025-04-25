def digitos(cpf, cont = 10):
    cpf = int(cpf)
    soma = 0
    digito = 0
    for digito in cpf:
        soma += digito * cont
        cont -= 1
    digito = soma % 11

    return digito

cpf_lista = '05788661706'

digitos(cpf_lista[0:9])
print(cpf_lista[0:9])