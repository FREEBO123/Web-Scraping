import requests
import pandas as pd
from bs4 import BeautifulSoup

# ruta del sitio web del banco central
url = "https://si3.bcentral.cl/Siete/ES/Siete/Cuadro/CAP_EI/MN_EI11/EI_CREC_TRI"

# Detectando la Tabla
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.get_text())
tabla = soup.find("table")
filas = tabla.find_all("tr")

for fila in filas:
    celdas = fila.find_all(["th", "td"])

    datos = [
        celda.get_text(strip=True)
        for celda in celdas
    ]

datos = []

for fila in filas:
    celdas = fila.find_all(["th", "td"])

    datos.append([
        celda.get_text(strip=True)
        for celda in celdas
    ])

# Conversion a Dataframe
df = pd.DataFrame(datos)

# Exportacion a Excel
df.to_excel("datos.xlsx", index=False)

print(df)