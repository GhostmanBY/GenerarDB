# GenerarDB

Una clase wrapper para SQLite que proporciona operaciones comunes de base de datos. Esta clase simplifica el proceso de crear tablas, insertar datos, modificar registros y realizar consultas con protección integrada contra inyección SQL.

## Características

- Crear nuevas bases de datos SQLite y tablas
- Insertar registros con soporte dinámico de columnas
- Actualizar registros existentes
- Eliminar registros
- Realizar consultas flexibles con cláusulas WHERE
- Protección integrada contra inyección SQL
- Soporte todos los tipo de datos, sin crear limitaciones
## Instalación

1. Asegúrate de tener Python 3.x instalado
2. El módulo usa solo librerías integradas de Python (`sqlite3` y `re`), por lo que no requiere instalación adicional
3. Copia el archivo `GenerarDB.py` a tu directorio de proyecto

## Uso

### Inicializar Conexión a Base de Datos

```python
from Generar_DB import DB_Panel

# Crear una nueva base de datos o conectar a una existente
db = DB_Panel("mi_base_datos")
```

### Crear una Nueva Tabla

```python
# Crear tabla con columnas específicas
db.Crear_tabla_nueva("Stock", 
    Nombre="TEXT",
    Precio="REAL",
    Cantidad="INTEGER"
)
```

### Insertar Datos

```python
# Insertar un único registro
db.Ingresar("Stock",
    Nombre="Fideos",
    Precio=500,
    Cantidad=50
)

# Insertar múltiples registros
productos = [
    {"Nombre": "Arroz", "Precio": 400, "Cantidad": 100},
    {"Nombre": "Aceite", "Precio": 1200, "Cantidad": 30}
]

for producto in productos:
    db.Ingresar("Stock", **producto)
```

### Consultar Datos

```python
# Consulta básica (todos los registros)
resultados = db.Consultar("Stock")

# Consulta con condiciones
# Nota: Los valores deben estar entre comillas simples
resultados = db.Consultar("Stock", 
    Agregado="WHERE Precio > '500'"
)

# Consulta con múltiples condiciones
resultados = db.Consultar("Stock", 
    Agregado="WHERE Nombre LIKE '%a%' AND Precio > '300' AND Cantidad < '100'"
)
```

### Modificar Registros

```python
# Modificar un registro específico
db.Modificar("Stock", "Arroz", "Cantidad", 80)
```

### Eliminar Registros

```python
# Eliminar un registro por ID
db.Eliminar("Stock", 1)
```

## Consideraciones Importantes

1. **Seguridad**: 
   - La clase incluye validaciones para prevenir inyección SQL
   - Los nombres de tablas y columnas son validados
   - Los valores en las consultas deben estar entre comillas simples

2. **Consultas**:
   - En las cláusulas WHERE, los valores deben estar entre comillas simples
   - Ejemplo: `WHERE Precio > '500'` (correcto)
   - Ejemplo: `WHERE Precio > 500` (incorrecto)
   
## Ejemplo Completo

```python
from Generar_DB import DB_Panel

# Crear conexión
db = DB_Panel("Stock")

# Crear tabla
db.Crear_tabla_nueva("Stock", 
    Nombre="TEXT",
    Precio="REAL",
    Cantidad="INTEGER"
)

# Insertar producto
db.Ingresar("Stock",
    Nombre="Fideos",
    Precio=500,
    Cantidad=50
)

# Consultar productos
resultados = db.Consultar("Stock", 
    Agregado="WHERE Precio > '300'"
)

# Modificar cantidad
db.Modificar("Stock", "Fideos", "Cantidad", 40)
```

## Limitaciones

- Solo soporta bases de datos SQLite
- Las consultas complejas están limitadas a operaciones básicas WHERE
- No soporta JOINs u operaciones más complejas de SQL

## Contribuciones

Si deseas contribuir al proyecto, puedes:

1. Reportar errores
2. Sugerir nuevas características
3. Enviar pull requests con mejoras

## Licencia

Este proyecto está disponible como código abierto bajo la licencia MIT.
