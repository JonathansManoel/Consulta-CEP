from consulta_CEP import consultar_cep, Endereco
import responses
import pytest


@responses.activate
def test_consultar_cep():
    responses.add(
        responses.GET,
        'https://viacep.com.br/ws/01001000/json/',
        json={
            "cep": "01001-000",
            "logradouro": "Praça da Sé",
            "complemento": "lado ímpar",
            "bairro": "Sé",
            "localidade": "São Paulo",
            "uf": "SP",
            "ibge": "3550308",
            "gia": "1004",
            "ddd": "11",
            "siafi": "7107"
        },
    )

    result = consultar_cep('01001000')

    assert Endereco(uf='SP', bairro='Sé', localidade='São Paulo') == result


@responses.activate
def test_consultar_cep_invalido():
    responses.add(
        responses.GET,
        'https://viacep.com.br/ws/12312312/json/',
        status=400
    )

    with pytest.raises(ValueError):
        consultar_cep('12312312')
