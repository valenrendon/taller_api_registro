
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import database
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # permite cualquier origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Usuario(BaseModel):
    email: str
    password: str

# Ruta para servir front.html
@app.get("/", response_class=HTMLResponse)
def home():
    with open("front.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/register")
def register(usuario: Usuario):
    database.usuarios.append(usuario.dict())
    return {"mensaje": "Usuario registrado", "usuario": usuario.dict()}

@app.post("/login")
def login(usuario: Usuario):

    for u in database.usuarios:
        if u["email"] == usuario.email and u["password"] == usuario.password:
            return {"mensaje": "Login exitoso"}

    return {"error": "Credenciales inválidas"}





