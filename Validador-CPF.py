# Este programa irá validar se um CPF é valido ou não.
cpf_lista = ['05788661706', '11501643797', '23392206709']

cpf_soma = 0
multi = 10

# Converte o CPF para numero (int) para que possamos somar
cpf = (cpf_lista[0])

# Calculo do primeiro digito
while multi >= 2:
    cpf_soma += cpf[0] * multi
    multi -= 1

# Calculo para o primeiro digito.
for n in cpf[:-2]:
    cpf_conv = int(n)
    cpf_soma += cpf_conv * multi
    multi += -1

    print(multi)

