from cpf_cnpj import Documento

exemplo_cnpj = "35379838000112"
exemplo_cpf = "49589179851"
documento = Documento.cria_documento(exemplo_cnpj)
#documento = Documento(exemplo_cpf)
print(documento)
