from cpf_cnpj import CpfCnpj

exemplo_cnpj = "35379838000112"
exemplo_cpf = "49589179851"
documento = CpfCnpj(exemplo_cpf, 'cpf')
#documento = CpfCnpj(exemplo_cpf, 'cnpj')
print(documento)
