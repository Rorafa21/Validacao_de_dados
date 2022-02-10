class Cpf():

    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_valido(documento):
            self.cpf = documento
        else:
            raise ValueError ("CPF invalido!!")

    def __str__(self):
        return self.cpf_formatado()

    def cpf_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def cpf_formatado(self):
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]
        return (f"{fatia_um}.{fatia_dois}.{fatia_tres}.{fatia_quatro}")