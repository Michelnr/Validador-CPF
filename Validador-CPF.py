# Este programa irá validar se um CPF é valido ou não utilizando um algoritmo específico.
# teste

cpf_lista = [5788661706, 11501643797, 23392206709]

cpf_soma = 0
multi = 0

# Converte o CPF para texto (str) para que possamos fatiar
cpf = str(cpf_lista[0])

# Acertando o multiplicador caso o CPF inicie com 0
if len(cpf) < 11:
    multi = 9
else:
   multi = 10

# Calculo para o primeiro digito.
for n in cpf[:-2]:
    cpf_conv = int(n)
    cpf_soma += cpf_conv * multi
    multi += -1

    print(multi)
