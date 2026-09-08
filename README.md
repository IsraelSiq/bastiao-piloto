# bastiao-piloto

Projeto-piloto FastAPI usado para desenvolver e testar o Bastiao Explorer e Builder.

## Stack

- Python 3.11+
- FastAPI
- Uvicorn
- pytest
- ruff

## Rodar localmente

```bash
# Clonar
git clone git@github.com:IsraelSiq/bastiao-piloto.git
cd bastiao-piloto

# Ambiente virtual
python -m venv .venv
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Rodar a API
uvicorn src.main:app --reload
```

A API fica em: `http://127.0.0.1:8000`

Endpoints:

- `GET /` – mensagem de boas-vindas.
- `GET /health` – saude da API.

## Testes

```bash
pytest
```

## Lint

```bash
ruff check src tests
```

## Docker (opcional)

```bash
docker build -t bastiao-piloto .
docker run -p 8000:8000 bastiao-piloto
```
