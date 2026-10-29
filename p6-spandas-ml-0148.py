import pandas as pd
import numpy as np

serie_amigos = ["Caleb", "Jazmin", "Farfan", "Yahir", "Dartell", "Iris", "Alexia"]
print("--+Serie de listado de amigos (NC:0148)+--")
amigos = pd.Series(serie_amigos)
print(amigos)

serie_billetes = [20, 50, 100, 200, 500, 1000]
print("--+Serie de listado del valor de billetes MX (NC:0148)+--")
billetes = pd.Series(serie_billetes)
print(billetes)

serie_billetes = [20, 50, 100, 200, 500, 1000]
serie_bletras = ["veinte", "Cincuenta", "Cien", "Doscientos", "Quinientos", "Mil"]
print("--+Serie de listado de nombres y de los valores de billetes MX (NC:0148)+--")
tablabilletes = pd.Series(serie_bletras, serie_billetes)
print(tablabilletes)

# Diccionario DataFrame
# Diccionario del valor de las monedas y su respectivo nombre 
print("--+Datos de diccionario a DataFrame en Pandas (NC:0148)+--")
dicc_monedas = {
    "serie_billetes": [20, 50, 100, 200, 500, 1000],
    "serie_bletras": ["veinte", "Cincuenta", "Cien", "Doscientos", "Quinientos", "Mil"]
}

tabla_billetes = pd.DataFrame(dicc_monedas, index = ["A","B","C","D","E","F"])
print(tabla_billetes)
print("Casa de cambio de Arath Valenzuela (NC:0148)")