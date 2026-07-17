# Catálogo de Libros — API con Almacenamiento Ligero (Ejemplo de Clase)

> **Para el profesor:** Este es un ejemplo simplificado para trabajar en clase que introduce los mismos conceptos del proyecto Directorio de Proveedores — TinyDB, validación con Pydantic, seeders y endpoints con filtros — usando un dominio cotidiano. Es intencionalmente más corto para poder construirse en directo durante la sesión.

_These instructions are also available in [English](./README.md)._

---

## 🎯 El reto

### Nota de alcance

Este ejemplo está acotado para una sesión en vivo en el aula. Mantiene el mismo stack y patrones centrales que el proyecto oficial del estudiante en esta carpeta pero omite requisitos secundarios; ver la nota para instructores arriba. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.


Una pequeña biblioteca comunitaria lleva el registro de sus libros en un archivo de texto. Te han pedido que lo reemplaces con una pequeña API FastAPI + TinyDB + Pydantic que arranque con datos precargados y rechace cualquier entrada inválida antes de que llegue a la base de datos.

---

## 💻 Qué tienes que construir

### Modelo de datos

Define un modelo Pydantic `Book` con los siguientes campos:

| Campo    | Tipo  | Restricciones                                               |
| -------- | ----- | ----------------------------------------------------------- |
| `title`  | `str` | obligatorio                                                 |
| `author` | `str` | obligatorio                                                 |
| `genre`  | `str` | solo: `"fiction"`, `"non-fiction"`, `"mystery"`, `"sci-fi"` |
| `pages`  | `int` | debe ser mayor que 0                                        |
| `status` | `str` | solo: `"available"`, `"checked_out"`                        |

Usa un `Enum` o un validador de campo Pydantic para aplicar las restricciones de `genre` y `status`. Pydantic debe rechazar valores inválidos con `422` antes de que cualquier dato llegue a TinyDB.

### Seeder

Crea un script `seed.py` que cargue estos cuatro libros en TinyDB al arrancar:

```python
[
    {"title": "The Pragmatic Programmer", "author": "Hunt & Thomas",  "genre": "non-fiction", "pages": 352, "status": "available"},
    {"title": "Dune",                     "author": "Frank Herbert",  "genre": "sci-fi",      "pages": 412, "status": "available"},
    {"title": "The Big Sleep",            "author": "Raymond Chandler","genre": "mystery",    "pages": 231, "status": "checked_out"},
    {"title": "Nineteen Eighty-Four",     "author": "George Orwell",  "genre": "fiction",     "pages": 328, "status": "available"},
]
```

- Ejecutar el seeder dos veces no debe crear registros duplicados.
- Imprime el número de registros insertados al finalizar.

### Endpoints

| Método   | Ruta                 | Descripción                                                                      |
| -------- | -------------------- | -------------------------------------------------------------------------------- |
| `POST`   | `/books`             | Registra un libro nuevo. Devuelve el libro creado con su ID de TinyDB.           |
| `GET`    | `/books`             | Lista todos los libros. Acepta parámetros opcionales `?genre=` y `?status=`.     |
| `GET`    | `/books/{id}`        | Devuelve un libro por su ID. Devuelve `404` si no existe.                        |
| `PATCH`  | `/books/{id}/status` | Cambia el estado a `available` o `checked_out`. Rechaza otros valores con `422`. |
| `DELETE` | `/books/{id}`        | Elimina un libro. Devuelve `404` si no existe.                                   |

---

## ✅ Conceptos clave a verificar

- [ ] Valores de `genre` fuera del conjunto permitido devuelven `422`.
- [ ] `pages` con valor cero o negativo devuelve `422`.
- [ ] Valores de `status` fuera del conjunto permitido devuelven `422`.
- [ ] `GET /books?genre=mystery` devuelve solo los libros de misterio.
- [ ] `GET /books?status=available` devuelve solo los libros disponibles.
- [ ] Ejecutar el seeder una segunda vez no genera duplicados.
- [ ] Los datos persisten al reiniciar el servidor.

---

## 💡 Preguntas para la discusión

1. ¿Por qué usar TinyDB en lugar de una base de datos SQL completa para un proyecto como este?
2. ¿En qué punto exacto detiene Pydantic una solicitud inválida — antes o después de TinyDB?
3. ¿Qué habría que cambiar para migrar esto a PostgreSQL más adelante?
