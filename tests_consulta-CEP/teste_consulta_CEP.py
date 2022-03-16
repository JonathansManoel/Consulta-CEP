from consulta_CEP import consulta_cep
import pytest

@pytest.fixture
def resp(r):
    resp = r.get(consulta_cep)
    return resp

def test_consulta_cep_status_code(resp):
    assert resp.status_code == 200
