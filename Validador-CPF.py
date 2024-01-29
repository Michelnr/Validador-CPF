cpf_lista = [5788661706, 11501643797, 23392206709]

cpf = str(cpf_lista[0])

cpf_soma = 0
multi = 10

for n in cpf:
    cpf_conv = int(n)
    if len(cpf) < 11:
        multi = 9
    cpf_soma += cpf_conv
    print(cpf_soma)
