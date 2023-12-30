import re
from validate_docbr import CPF


def validate_cpf(numero_cpf):
        cpf = CPF()
        return cpf.validate(numero_cpf)
    
def validate_celular(celular):
    '''Verifica se o celular é válido xx xxxxx-xxxx'''
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo,celular)
    return resposta
    
def validate_rg(rg):
    return len(rg) == 9
    
def validate_nome(nome):    
    return nome.isalpha()