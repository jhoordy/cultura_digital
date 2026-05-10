import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Cargar dataset
def cargar_datos(ruta):
    return pd.read_csv(ruta)

# Eliminar valores nulos
def eliminar_nulos(df):
    return df.dropna()

# Eliminar duplicados
def eliminar_duplicados(df):
    return df.drop_duplicates()

# Normalizar columnas numéricas
def normalizar_datos(df, columnas):
    scaler = MinMaxScaler()
    df[columnas] = scaler.fit_transform(df[columnas])
    return df

# Codificar variables categóricas
def codificar_variables(df):
    return pd.get_dummies(df)

print("Preprocesamiento completado correctamente")

print("Preprocesamiento completado")