import os
from dotenv import load_dotenv

# Carga las variables definidas en el archivo .env
load_dotenv()


class Settings:
    # Datos de conexión a la base de datos MySQL
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:password@localhost:3306/mired_ips"
    )

    # Datos para generar y validar los tokens JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "clave-secreta-de-desarrollo")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
    DB_NAME: str = os.getenv("DB_NAME", "mired_ips")


settings = Settings()