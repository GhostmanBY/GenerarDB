import os

from GenerarDB import DB_SQLite
# Instancia con la clase que crea la Base de Datos, a la cual se le pasa el nombre del archivo
DB = DB_SQLite("DB/Stock") 

# Crear tabla Stock
DB.Crear_tabla_nueva("Stock", Nombre="TEXT", Precio="REAL", Cantidad="INTEGER")

# Datos para poblar la base de datos
productos = [
    {"Nombre": "Fideos", "Precio": 500, "Cantidad": 50},
    {"Nombre": "Arroz", "Precio": 400, "Cantidad": 100},
    {"Nombre": "Aceite", "Precio": 1200, "Cantidad": 30},
    {"Nombre": "Sal", "Precio": 200, "Cantidad": 80},
    {"Nombre": "Azúcar", "Precio": 350, "Cantidad": 60},
    {"Nombre": "Harina", "Precio": 300, "Cantidad": 40},
    {"Nombre": "Leche", "Precio": 250, "Cantidad": 90},
    {"Nombre": "Huevos", "Precio": 700, "Cantidad": 20},
    {"Nombre": "Pan", "Precio": 150, "Cantidad": 150},
    {"Nombre": "Manteca", "Precio": 500, "Cantidad": 25},
    {"Nombre": "Café", "Precio": 900, "Cantidad": 15},
    {"Nombre": "Té", "Precio": 400, "Cantidad": 35},
    {"Nombre": "Yerba", "Precio": 800, "Cantidad": 50},
    {"Nombre": "Polenta", "Precio": 450, "Cantidad": 60},
    {"Nombre": "Galletitas", "Precio": 600, "Cantidad": 100},
    {"Nombre": "Queso", "Precio": 1500, "Cantidad": 10},
    {"Nombre": "Jamón", "Precio": 1800, "Cantidad": 5},
    {"Nombre": "Cerveza", "Precio": 200, "Cantidad": 300},
    {"Nombre": "Vino", "Precio": 1200, "Cantidad": 20},
    {"Nombre": "Gaseosa", "Precio": 250, "Cantidad": 200}
]

# Insertar datos en la tabla
for producto in productos:
    DB.Ingresar("Stock", **producto)

print("Base de datos inicializada con productos:")
resultado = DB.Consultar("Stock", Columna="*")
for fila in resultado:
    print(fila)

input("Presione Enter para realizar consultas de prueba...")
os.system("cls")

# Consultas de ejemplo
# Detalle todos los parametros despues de un operar estan con comillas simples, esto para que lo puedo tomar bien la funcion y dividir parametros de clausulas
print("Productos con precio mayor a 500:")
resultado = DB.Consultar("Stock", Agregado="WHERE Precio > '500'") # ej: el 500 esta entre comillas simples
for fila in resultado:
    print(fila)

print("\nProductos con cantidad menor a 50:")
resultado = DB.Consultar("Stock", Agregado="WHERE Cantidad < '50'")# ej: el 50 esta entre comillas simples
for fila in resultado:
    print(fila)

print("\nProductos cuyo nombre contiene la letra 'a':")
resultado = DB.Consultar("Stock", Agregado="WHERE Nombre LIKE '%a%' AND Precio > '300' AND Cantidad < '100'") # ej: aca tanto el %a%, el 300 y el 100 estan entre comillas simples
for fila in resultado:
    print(fila)

input("Para modificar el Stock de la Aceite, el Arroz y el Café. Presione enter")
os.system("cls")

# Metodo de Modificar
print("Se modificara el stock de la aceite, el arroz y el cafe")
DB.Modificar("Stock", "Aceite", "Cantidad", 15)
DB.Modificar("Stock", "Arroz", "Cantidad", 80)
DB.Modificar("Stock", "Café", "Cantidad", 5)

# Base de datos actualizada
resultado = DB.Consultar("Stock", Columna="*")
for fila in resultado:
    print(fila)

input("Para eliminar los productos Manteca, Azúcar y Jamón. Presione Enter")
os.system("cls")

#  Metodo de Eliminar
print("Se eliminaron los productos Manteca, Azúcar y Jamón")
DB.Eliminar("Stock", 10)
DB.Eliminar("Stock", 5)
DB.Eliminar("Stock", 17)

# Base de datos actualizada
resultado = DB.Consultar("Stock", Columna="*")
for fila in resultado:
    print(fila)