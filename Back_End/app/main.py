from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

# Importar routers
from app.routers import auth, users, productos, categorias

app = FastAPI(
    title="MiRed IPS API",
    description="API para gestión de usuarios y productos",
    version="1.0.0"
)

# Configurar CORS - PERMITIR TODOS LOS ORÍGENES (para desarrollo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes en desarrollo
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos los headers
)

# También puedes especificar orígenes específicos:
# allow_origins=["http://localhost:4200", "http://127.0.0.1:4200"],

# Registrar routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(productos.router)
app.include_router(categorias.router)


@app.get("/")
def root():
    return {
        "message": "API funcionando",
        "version": "1.0.0",
        "status": "online"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}