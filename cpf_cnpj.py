from validate_docbr import CPF, CNPJ

class CpfCnpj():
    #inicio definindo se o cpf é valido
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if self.tipo_documento == "cpf":
            if self.cpf_valido(documento):
                self.cpf = documento
            else:
                raise ValueError ("CPF invalido!!")
        elif self.tipo_documento == "cnpj":
            if self.cnpj_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ invalido!!")
        else:
            raise ValueError("Documento invalido!!")
    #cpf formatado
    def __str__(self):
        return self.cpf_formatado()
    def __str__(self):
        return self.cnpj_formatado()
    #validando tamanho cpf
    def cpf_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos invalida")
    #formatando cpf
    def cpf_formatado(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    #validando cnpj
    def cnpj_valido(self, cnpj):
        if len(cnpj) == 14:
            validador_cnpj = CNPJ()
            return validador_cnpj.validate((cnpj))
        else:
            raise ValueError ("Quantidade de gitios errado")
    def cnpj_formatado(self):
        mascara_cnpj = CNPJ
        return  mascara_cnpj.mask(self.cnpj)
