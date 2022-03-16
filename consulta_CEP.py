import requests

def consulta_cep():
    titulo = 'Consulta CEP'
    print('-=-' * 17)
    print(f'\033[0;30;41m{titulo.center(50, "-")}\033[m')
    print('-=-' * 17)
    print()

    cep = input('Digite o CEP para consulta: ')

    if len(cep) != 8:
        print('Quantidade de dígitos inválido!')
        exit()

    r = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    address = r.json()

    if 'erro' not in address:
        print('-=- CEP ENCONTRADO -=-')
        print(f'CEP: {address["cep"]}')
        print(f'Logradouro: {address["logradouro"]}')
        print(f'Complemento: {address["complemento"]}')
        print(f'Bairro: {address["bairro"]}')
        print(f'Cidade: {address["localidade"]}')
        print(f'Estado: {address["uf"]}')
    else:
        print(f'{cep}: CEP inválido.')
    print('-=-' * 11)
    reinicio = int(input('Deseja realizar uma nova consulta?\nEscolha uma das opções a seguir:\n[ 1 ] Sim\n[ 2 ] Sair'''))
    if reinicio == 1:
        consulta_cep()
    else:
        print('Finalizada Consulta!')

if __name__ == '__main__':
    consulta_cep()