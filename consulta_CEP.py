import requests
from collections import namedtuple

Endereco = namedtuple('Endereco', ['uf', 'bairro', 'localidade'])


def consultar_cep(cep: str) -> Endereco:
    titulo = 'Consulta CEP'
    print('-=-' * 17)
    print(f'\033[0;30;41m{titulo.center(50, "-")}\033[m')
    print('-=-' * 17)
    print()

    # cep = input('Digite o CEP para consulta: ')
    cep = cep.replace('-', '')
    if len(cep) != 8:
        print('Quantidade de dígitos inválido!')
        exit()
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if response.json().get('erro'):
        raise ValueError('Cep inválido!')

    retorno = response.json()
    return Endereco(uf=retorno['uf'], bairro=retorno['bairro'], localidade=retorno['localidade'])


if __name__ == '__main__':
    print(consultar_cep(cep=input('Digite o CEP para consulta: ')))

