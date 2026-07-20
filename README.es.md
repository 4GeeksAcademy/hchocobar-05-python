# Ejemplo en Clase — Asegurando una API de Intercambio de Plantas

## El Escenario

### Nota de alcance

Una pequeña comunidad tiene un backend FastAPI para listar y reclamar plantas que los miembros quieren intercambiar. Ahora mismo cualquier petición — incluyendo crear, editar y eliminar listados — es completamente pública. Antes de que salga la siguiente versión, el mantenedor necesita asegurar la API: solo los miembros autenticados pueden publicar o gestionar listados.

---

## Stack Tecnológico

| Capa             | Herramienta                              |
| ---------------- | ---------------------------------------- |
| Framework        | FastAPI                                  |
| Auth             | JWT (`python-jose`) + bcrypt (`passlib`) |
| Esquema de token | `OAuth2PasswordBearer`                   |
| Base de datos    | TinyDB (solo modelos de auth)            |
| Configuración    | `.env` + `python-dotenv`                 |

Instalar las dependencias de auth:

```bash
uv add "python-jose[cryptography]" "passlib[bcrypt]"
```

---

## Modelo de Datos

### Tabla de usuarios (TinyDB)

| Columna           | Tipo     | Notas                                           |
| ----------------- | -------- | ----------------------------------------------- |
| `id`              | str/uuid | clave primaria                                  |
| `email`           | str      | único, requerido                                |
| `hashed_password` | str      | nunca guardar texto plano                       |
| `is_active`       | bool     | por defecto `True`                              |
| `role`            | str      | `admin`, `manager` o `user`; por defecto `user` |
| `created_at`      | datetime | automático                                      |

### Tabla de perfiles (TinyDB)

| Columna   | Tipo | Notas                                |
| --------- | ---- | ------------------------------------ |
| `id`      | str  | clave primaria                       |
| `user_id` | str  | enlace uno a uno con `User.id`       |
| `name`    | str  | nombre visible — **no** va en `User` |
| `phone`   | str  | dato de contacto                     |
| `address` | str  | dato de contacto                     |

---

## Qué Construir

### CRUD de usuarios (`/users`)

- [ ] `POST /users` — registrar un nuevo usuario y crear el perfil vinculado. Hashear la contraseña con `bcrypt` antes de guardar. **Pública** (no requiere token).
- [ ] `GET /users` — listar todos los usuarios. **Protegida**.
- [ ] `GET /users/{id}` — obtener un usuario. **Protegida**.
- [ ] `PUT /users/{id}` — actualizar campos de credenciales como el email. **Protegida** — solo el propio usuario.
- [ ] `DELETE /users/{id}` — eliminar un usuario y su perfil vinculado. **Protegida** — solo el propio usuario.

### Endpoints de perfil (`/profiles`)

- [ ] `GET /profiles/me` — devuelve el perfil del miembro autenticado. **Protegida**.
- [ ] `PUT /profiles/me` — actualiza `name`, `phone` y `address`. **Protegida**.

### Endpoints de auth (`/auth`)

- [ ] `POST /auth/login` — acepta `email` + `password`. Valida credenciales; si son correctas, devuelve un token JWT de acceso firmado.
- [ ] `GET /auth/me` — devuelve el email más los datos del perfil vinculado. **Protegida**.

### Token y dependencia

- [ ] Crear una dependencia `get_current_user` que:
  1. Lee la cabecera `Authorization: Bearer <token>`.
  2. Decodifica y valida el JWT (firma + expiración).
  3. Recupera el usuario de la base de datos.
  4. Lanza `HTTPException(401)` si algo falla.
- [ ] Guardar la clave de firma JWT en `.env` como `SECRET_KEY`. Nunca hardcodearla.
- [ ] Guardar la expiración del token en `.env` como `ACCESS_TOKEN_EXPIRE_MINUTES`.

### Protección de rutas

- [ ] Aplicar `get_current_user` como argumento `Depends(...)` en cada ruta que no deba ser pública.
- [ ] Devolver `401 Unauthorized` para tokens ausentes o inválidos.
- [ ] Devolver `403 Forbidden` cuando un usuario válido intenta modificar el registro de otro usuario.

---

## Modelo Mental: Cómo Funciona JWT en FastAPI

```
1. Cliente → POST /auth/login  { email, password }
2. Servidor valida hash de contraseña → firma JWT → devuelve token
3. Cliente guarda el token

4. Cliente → GET /auth/me
   Headers: Authorization: Bearer <token>
5. Dependencia get_current_user decodifica JWT → recupera usuario → lo pasa a la ruta
6. La ruta devuelve los datos del usuario

7. Cliente → GET /auth/me (token expirado o ausente)
   Servidor → 401 Unauthorized
```

---

## Lista de Verificación Manual

Trabajar estos pasos en la UI de `/docs` de FastAPI:

- [ ] Registrar un nuevo usuario → confirmar que la contraseña no es visible en la respuesta.
- [ ] Hacer login → copiar el token devuelto.
- [ ] Hacer clic en "Authorize" en `/docs`, pegar el token → llamar a `GET /auth/me` → ver el perfil.
- [ ] Llamar a `GET /users` **sin** token → confirmar que se recibe `401`.
- [ ] Esperar a que el token expire (o configurar manualmente 1 minuto de expiración para clase) → llamar a una ruta protegida → confirmar `401`.

---

## Conceptos Clave a Trabajar en Clase

| Concepto                                  | Dónde aparece                                       |
| ----------------------------------------- | --------------------------------------------------- |
| Hash de contraseñas                       | `passlib.hash.bcrypt.hash()` en el registro         |
| Estructura JWT (header.payload.signature) | Creación de token con `python-jose`                 |
| `OAuth2PasswordBearer`                    | Extracción del token de la cabecera `Authorization` |
| `Depends()` de FastAPI                    | `get_current_user` inyectado en las rutas           |
| Variables de entorno para secretos        | `SECRET_KEY` en `.env`                              |
| `401` vs `403`                            | Token ausente vs. usuario incorrecto                |

---

## Preguntas para Debate

1. ¿Por qué hacemos hash de las contraseñas en lugar de cifrarlas? ¿Cuál es la diferencia práctica cuando se vulnera una base de datos?
2. La dependencia `get_current_user` lanza un `401` si el token ha expirado. ¿Debería el cliente poder renovar el token automáticamente, y cómo funcionaría un patrón de refresh token?
3. Por ahora, `GET /users` devuelve todos los usuarios a cualquier usuario autenticado. ¿Es eso apropiado? ¿Qué cambiarías si quisieras que solo los administradores vieran la lista completa?
