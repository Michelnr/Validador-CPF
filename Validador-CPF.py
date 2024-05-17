# Este programa irá validar se um CPF é valido ou não.
cpf_lista = ['05788661706', '11501643797', '23392206709']

cpf_soma = 0
multi = 10
CPF_Dig = 0

# Converte o CPF para numero (int) para que possamos somar
cpf = (cpf_lista[0])

# Calculo do primeiro digito
while multi >= 2:
    cpf_soma += cpf[CPF_Dig] * multi
    multi -= 1
    CPF_Dig += 1

CPF_Dig = 1

# Calculo do segundo digito.
while multi >= 2:
    cpf_soma += cpf[0] * multi
    multi -= 1
    CPF_Dig += 1
