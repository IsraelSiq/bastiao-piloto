from fastapi import FastAPI

app = FastAPI(title="bastiao-piloto")


@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao bastiao-piloto!"}


@app.get("/health")
def health():
    return {"status": "ok"}
