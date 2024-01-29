cpf_lista = [5788661706, 11501643797, 23392206709]

cpf_soma = 0
multi = 0

cpf = str(cpf_lista[0])

if len(cpf) < 11:
    multi = 9
else:
    multi = 10

for n in cpf[:-2]:
    cpf_conv = int(n)
    cpf_soma += cpf_conv * multi

    print(n)
