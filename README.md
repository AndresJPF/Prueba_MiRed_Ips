# **MiRed IPS - Sistema de Gestión**

Sistema completo de gestión de usuarios y productos para MiRed IPS, desarrollado como prueba técnica para la posición de Practicante Full Stack.

## **📋 Tabla de Contenidos**

- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos Previos](#requisitos-previos)
- [Instalación y Configuración](#instalación-y-configuración)
  - [Backend (FastAPI)](#backend-fastapi)
  - [Frontend (Angular)](#frontend-angular)
  - [Base de Datos](#base-de-datos)
- [Ejecución del Proyecto](#ejecución-del-proyecto)
- [Credenciales de Prueba](#credenciales-de-prueba)
- [Documentación de la API](#documentación-de-la-api)
- [Colección de Postman](#colección-de-postman)
- [Funcionalidades Implementadas](#funcionalidades-implementadas)
- [Estructura de la Base de Datos](#estructura-de-la-base-de-datos)
- [Solución de Problemas](#solución-de-problemas)
- [Mejoras Futuras](#mejoras-futuras)

---

## **🚀 Tecnologías Utilizadas**

### **Backend**
- **Python 3.12** - Lenguaje de programación
- **FastAPI** - Framework web moderno y rápido
- **SQLAlchemy** - ORM para Python
- **PyMySQL** - Conector para MySQL
- **Python-JOSE** - Manejo de JWT
- **Passlib** - Hashing de contraseñas (bcrypt)
- **Uvicorn** - Servidor ASGI
- **Python-dotenv** - Manejo de variables de entorno

### **Frontend**
- **Angular 18** - Framework frontend
- **TypeScript** - Lenguaje tipado
- **RxJS** - Programación reactiva
- **CSS3** - Estilos puros (sin frameworks externos)

### **Base de Datos**
- **MySQL 8.0** - Sistema gestor de bases de datos relacional

---

## **📁 Estructura del Proyecto**

```
Prueba_MiRed_Ips/
├── Back_End/                     # Backend FastAPI
│   ├── app/
│   │   ├── core/                 # Configuración central
│   │   │   ├── config.py         # Variables de entorno
│   │   │   ├── database.py       # Conexión a BD
│   │   │   ├── security.py       # JWT y hashing
│   │   │   └── dependencies.py   # Dependencias inyectables
│   │   ├── models/               # Modelos SQLAlchemy
│   │   │   ├── user.py
│   │   │   ├── producto.py
│   │   │   └── categoria.py
│   │   ├── schemas/              # Schemas Pydantic
│   │   │   ├── auth.py
│   │   │   ├── user.py
│   │   │   ├── producto.py
│   │   │   └── categoria.py
│   │   ├── repositories/         # Capa de acceso a datos
│   │   ├── services/             # Lógica de negocio
│   │   ├── routers/              # Endpoints de la API
│   │   └── main.py               # Punto de entrada
│   ├── .env                      # Variables de entorno
│   └── requirements.txt          # Dependencias Python
│
├── Front_End/                    # Frontend Angular
│   ├── src/
│   │   ├── app/
│   │   │   ├── core/             # Servicios y utilidades
│   │   │   │   ├── guards/       # Protección de rutas
│   │   │   │   ├── interceptors/ # Interceptor JWT
│   │   │   │   ├── services/     # Servicios API
│   │   │   │   └── models/       # Interfaces TypeScript
│   │   │   ├── modules/          # Módulos funcionales
│   │   │   │   ├── auth/         # Login/Register
│   │   │   │   ├── users/        # CRUD usuarios
│   │   │   │   ├── products/     # CRUD productos
│   │   │   │   └── shared/       # Componentes compartidos
│   │   │   └── app-routing.module.ts
│   │   ├── environments/         # Configuración por entorno
│   │   └── styles.css
│   ├── angular.json
│   └── package.json
│
└── database/
    ├── schema.sql                # Estructura de BD
    └── seeder.sql                # Datos de prueba
```

---

## **🔧 Requisitos Previos**

Antes de comenzar, asegúrate de tener instalado:

### **Software Necesario**
- **Python 3.12 o superior**
- **Node.js 18 o superior** (para Angular)
- **Angular CLI 18** (`npm install -g @angular/cli@18`)
- **MySQL 8.0 o superior**
- **Git** (para clonar el repositorio)

### **Verificar Instalaciones**
```bash
# Verificar Python
python --version

# Verificar Node.js
node --version

# Verificar Angular CLI
ng version

# Verificar MySQL
mysql --version
```

---

## **📥 Instalación y Configuración**

### **1. Clonar el Repositorio**

```bash
git clone https://github.com/tu-usuario/Prueba_MiRed_Ips.git
cd Prueba_MiRed_Ips
```

### **2. Configurar Base de Datos**

#### **2.1 Crear la Base de Datos**
```sql
-- Conectar a MySQL
mysql -u root -p

-- Ejecutar el script de creación
source database/schema.sql;
```

#### **2.2 Cargar Datos de Prueba**
```sql
-- Cargar datos de ejemplo
source database/seeder.sql;
```

**Credenciales de prueba:**
- **Admin**: admin@miredips.com / password123
- **Empleado**: maria.gonzalez@miredips.com / password123

### **3. Configurar Backend (FastAPI)**

#### **3.1 Crear y Activar Entorno Virtual**
```bash
cd Back_End

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\Scripts\activate
```

#### **3.2 Instalar Dependencias**
```bash
pip install -r requirements.txt
```

#### **3.3 Configurar Variables de Entorno**
Crear archivo `.env` en la raíz de `Back_End`:

```env
# Base de Datos
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/mired_ips

# Seguridad JWT
SECRET_KEY=clave-secreta-de-desarrollo-cambiar-en-produccion
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Entorno
ENVIRONMENT=development
```

**Nota:** Reemplaza `root:password` con tus credenciales de MySQL.

### **4. Configurar Frontend (Angular)**

#### **4.1 Instalar Dependencias**
```bash
cd Front_End
npm install
```

#### **4.2 Configurar Variables de Entorno**
Editar `src/environments/environment.ts`:

```typescript
export const environment = {
  production: false,
  apiUrl: 'http://localhost:8000'  // URL del backend
};
```

---

## **🚀 Ejecución del Proyecto**

### **1. Iniciar Backend**

```bash
# Asegurarse de estar en la carpeta Back_End
cd Back_End

# Activar entorno virtual (si no está activo)
source venv/bin/activate

# Iniciar servidor
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**El servidor estará disponible en:** http://localhost:8000

**Documentación automática:**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### **2. Iniciar Frontend**

```bash
# Abrir nueva terminal
cd Front_End

# Iniciar servidor de desarrollo
ng serve --open
```

**La aplicación estará disponible en:** http://localhost:4200

### **3. Verificar Funcionamiento**

1. **Backend Health Check**: http://localhost:8000
   - Deberías ver: `{"message":"API funcionando","version":"1.0.0","status":"online"}`

2. **Frontend**: http://localhost:4200
   - Deberías ver la pantalla de login

---

## **🔐 Credenciales de Prueba**

### **Usuarios de Prueba**

| Email | Contraseña | Rol |
|-------|-----------|-----|
| admin@miredips.com | password123 | Administrador |
| carlos.rodriguez@miredips.com | password123 | Administrador |
| maria.gonzalez@miredips.com | password123 | Empleado |
| juan.perez@miredips.com | password123 | Empleado |
| ana.martinez@miredips.com | password123 | Empleado |
| luis.fernandez@miredips.com | password123 | Empleado |
| laura.sanchez@miredips.com | password123 | Empleado |

### **Datos de Prueba**
- **Categorías**: 10 categorías (Medicamentos, Equipos Médicos, etc.)
- **Productos**: 49 productos activos e inactivos

---

## **📚 Documentación de la API**

### **Endpoints Disponibles**

#### **Autenticación**
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| POST | `/auth/register` | Registrar nuevo usuario | No |
| POST | `/auth/login` | Iniciar sesión (retorna JWT) | No |
| POST | `/auth/logout` | Cerrar sesión | Sí |
| GET | `/auth/me` | Obtener usuario actual | Sí |

#### **Usuarios**
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| GET | `/users?page=1&page_size=10` | Listar usuarios (paginado) | Sí |
| GET | `/users/{id}` | Obtener usuario por ID | Sí |
| POST | `/users` | Crear usuario | Sí |
| PUT | `/users/{id}` | Actualizar usuario | Sí |
| DELETE | `/users/{id}` | Eliminar usuario (soft delete) | Sí |

#### **Productos**
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| GET | `/productos?page=1&page_size=10&categoria_id=1&estado=activo` | Listar productos (paginado + filtros) | Sí |
| GET | `/productos/{id}` | Obtener producto por ID | Sí |
| POST | `/productos` | Crear producto | Sí |
| PUT | `/productos/{id}` | Actualizar producto | Sí |
| DELETE | `/productos/{id}` | Eliminar producto (soft delete) | Sí |

#### **Categorías**
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| GET | `/categorias` | Listar todas las categorías | Sí |
| GET | `/categorias/{id}` | Obtener categoría por ID | Sí |
| POST | `/categorias` | Crear categoría | Sí |
| PUT | `/categorias/{id}` | Actualizar categoría | Sí |
| DELETE | `/categorias/{id}` | Eliminar categoría | Sí |

### **Ejemplos de Uso**

#### **Login**
```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@miredips.com","password":"password123"}'
```

**Respuesta:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### **Listar Productos (con autenticación)**
```bash
curl -X GET "http://localhost:8000/productos?page=1&page_size=10&categoria_id=1&estado=activo" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Respuesta:**
```json
{
  "data": [
    {
      "id": 1,
      "codigo": "MED-001",
      "nombre": "Acetaminofén 500mg x 30 comp",
      "categoria_id": 1,
      "descripcion": "Analgésico y antipirético de uso común",
      "precio": 8500.00,
      "stock": 250,
      "estado": "activo"
    }
  ],
  "total": 49,
  "page": 1,
  "page_size": 10
}
```

---

## **📦 Colección de Postman**

### **Importar Colección**

1. **Descargar la colección**: [Descargar Colección Postman](https://github.com/tu-usuario/Prueba_MiRed_Ips/blob/main/collection/Postman_Collection.json)

2. **Importar en Postman**:
   - Abrir Postman
   - Clic en "Import"
   - Seleccionar el archivo JSON descargado

3. **Configurar Variables de Entorno**:
   ```json
   {
     "base_url": "http://localhost:8000",
     "token": ""
   }
   ```

### **Endpoints Incluidos en la Colección**

- **Auth**: Register, Login, Logout, Me
- **Users**: List, Create, Get, Update, Delete
- **Products**: List, Create, Get, Update, Delete
- **Categories**: List, Create, Get, Update, Delete

---

## **✨ Funcionalidades Implementadas**

### **Backend**
- ✅ Autenticación JWT con expiración
- ✅ CRUD completo de usuarios
- ✅ CRUD completo de productos
- ✅ CRUD de categorías
- ✅ Paginación en listados
- ✅ Filtros en productos (categoría, estado)
- ✅ Soft Delete (eliminación lógica)
- ✅ Validaciones con Pydantic Schemas
- ✅ Manejo centralizado de errores
- ✅ Documentación automática (Swagger)
- ✅ CORS configurado
- ✅ Variables de entorno

### **Frontend**
- ✅ Login/Register con validaciones
- ✅ Protección de rutas (AuthGuard)
- ✅ Interceptor para tokens JWT
- ✅ CRUD de usuarios (paginado)
- ✅ CRUD de productos (paginado + filtros)
- ✅ Componentes reutilizables
- ✅ Estados de carga
- ✅ Manejo de errores visual
- ✅ Diseño responsivo
- ✅ Mensajes de éxito/error

### **Base de Datos**
- ✅ Modelo relacional normalizado
- ✅ Índices estratégicos
- ✅ Soft Delete
- ✅ Relaciones (categoría-producto)
- ✅ Datos de prueba completos

---

## **🗄️ Estructura de la Base de Datos**

### **Diagrama Entidad-Relación**

```
┌─────────────┐          ┌─────────────┐
│    users    │          │  categorias │
├─────────────┤          ├─────────────┤
│ id (PK)     │          │ id (PK)     │
│ name        │          │ nombre      │
│ email (UK)  │          │ descripcion │
│ password    │          └─────────────┘
│ role        │                │
│ created_at  │                │ 1
│ updated_at  │                │
│ deleted_at  │                │
└─────────────┘                │
                               │
                               │ N
┌─────────────┐          ┌────▼─────────────┐
│  productos  │◄─────────│                  │
├─────────────┤  FK      │   categoria_id   │
│ id (PK)     │          └──────────────────┘
│ codigo (UK) │
│ nombre      │
│ categoria_id│
│ descripcion │
│ precio      │
│ stock       │
│ estado      │
│ created_at  │
│ updated_at  │
│ deleted_at  │
└─────────────┘
```

### **Índices Implementados**
```sql
CREATE INDEX idx_users_role ON users(role);
CREATE INDEX idx_productos_categoria ON productos(categoria_id);
CREATE INDEX idx_productos_estado ON productos(estado);
CREATE INDEX idx_productos_nombre ON productos(nombre);
```

---

## **🔧 Solución de Problemas**

### **Error: El backend no inicia**
```bash
# Verificar que todas las dependencias están instaladas
pip install -r requirements.txt

# Verificar la configuración de .env
cat .env

# Verificar que MySQL está corriendo
sudo systemctl status mysql
```

### **Error: CORS**
```bash
# Verificar que CORS está configurado en main.py
# Debe tener:
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
```

### **Error: Token inválido**
```bash
# El token expira después de 60 minutos
# Volver a hacer login para obtener nuevo token
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@miredips.com","password":"password123"}'
```

### **Error: El frontend no conecta con el backend**
```bash
# Verificar que el backend está corriendo
curl http://localhost:8000

# Verificar la URL de la API en environment.ts
# Debe ser: apiUrl: 'http://localhost:8000'

# Verificar CORS en el backend
```

### **Error: MySQL Connection**
```bash
# Verificar que MySQL está corriendo
sudo systemctl start mysql

# Verificar credenciales en .env
# DATABASE_URL=mysql+pymysql://usuario:password@localhost:3306/mired_ips

# Crear la base de datos si no existe
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS mired_ips;"
```

---

## **🚀 Mejoras Futuras**

### **Backend**
- Implementación de pruebas automatizadas (Pytest)
- Rate limiting para prevenir ataques
- Logging avanzado
- Caché con Redis
- WebSockets para notificaciones en tiempo real
- Microservicios para módulos específicos
- Implementación de roles y permisos detallados

### **Frontend**
- Implementación de pruebas unitarias (Jasmine/Karma)
- State management (NgRx o Akita)
- Lazy loading de módulos
- PWA (Progressive Web App)
- Internacionalización (i18n)
- Módulo de reportes y estadísticas
- Dashboard con gráficos

### **Base de Datos**
- Particionamiento de tablas grandes
- Replicación para alta disponibilidad
- Backup automatizado
- Migraciones versionadas
- Auditoría de cambios

### **Seguridad**
- HTTPS con certificados SSL
- Rate limiting por IP
- 2FA (Autenticación de dos factores)
- Refresh tokens
- Blacklist de tokens

---

## **📝 Notas Adicionales**

### **Evaluación**
Este proyecto fue desarrollado como parte de la prueba técnica para el puesto de **Practicante Full Stack** en **MiRed IPS**, demostrando competencias en:

1. **Backend**: FastAPI, SQLAlchemy, JWT, MySQL
2. **Frontend**: Angular 18, TypeScript, CSS
3. **Arquitectura**: Patrones de diseño, separación de responsabilidades
4. **Calidad**: Código limpio, buenas prácticas, documentación

### **Contacto**
- **Autor**: [Andres Palacio]
- **Email**: [aandrespalacio29@gmail.com]
- **GitHub**: [https://github.com/AndresJPF/]

---

## **📄 Licencia**

Este proyecto es de uso exclusivo para la evaluación técnica de MiRed IPS.

---

## **👨‍💻 Scripts Útiles**

### **Backend**
```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar en desarrollo
uvicorn app.main:app --reload

# Ejecutar en producción
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4

# Ejecutar con Gunicorn (Linux)
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### **Frontend**
```bash
# Instalar dependencias
npm install

# Ejecutar en desarrollo
ng serve --open

# Construir para producción
ng build

# Ejecutar tests
ng test

# Ejecutar linting
ng lint
```

### **Base de Datos**
```bash
# Crear base de datos
mysql -u root -p < database/schema.sql

# Cargar datos de prueba
mysql -u root -p < database/seeder.sql

# Exportar base de datos
mysqldump -u root -p mired_ips > backup.sql
```

---

**¡Gracias por revisar este proyecto!** 🎉

Para cualquier pregunta o problema, no dudes en contactarme.
