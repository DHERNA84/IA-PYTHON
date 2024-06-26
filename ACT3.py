import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Definimos el número de viajes
num_viajes = 10

# Generamos estaciones de inicio y fin aleatorias
estaciones_inicio = np.random.randint(1, 8, num_viajes)  # Aseguramos que estaciones_inicio sea siempre menor que 8
estaciones_fin = np.random.randint(estaciones_inicio+1, 9, num_viajes)

# Calculamos la duración del viaje en minutos (10 minutos por cada estación que el tren debe pasar)
duracion = (estaciones_fin - estaciones_inicio + 1) * 10

# Calculamos las horas de inicio y fin
hora_inicio = 8 * 60 + np.arange(num_viajes) * 15  # 8:00 AM en minutos, incrementando en 15 minutos para cada viaje
hora_fin = hora_inicio + duracion

# Generamos la capacidad del tren aleatoria entre 80 y 120
capacidad_tren = np.random.randint(80, 121, num_viajes)

# Creamos un DataFrame de pandas con los datos
df = pd.DataFrame({
    'Estacion_Inicio': estaciones_inicio,
    'Estacion_Fin': estaciones_fin,
    'Hora_Inicio': [str(h // 60).zfill(2) + ':' + str(h % 60).zfill(2) for h in hora_inicio],
    'Hora_Fin': [str(h // 60).zfill(2) + ':' + str(h % 60).zfill(2) for h in hora_fin],
    'Duracion': duracion,
    'Capacidad_Tren': capacidad_tren,
    'Pasajeros': np.random.randint(0, capacidad_tren + 1)  # Número de pasajeros aleatorio entre 0 y la capacidad del tren
})

# Guardamos el DataFrame en un archivo CSV
df.to_csv('datos_transporte.csv', index=False)

# Dividimos los datos en conjuntos de entrenamiento y prueba
X = df.drop(['Pasajeros', 'Hora_Inicio', 'Hora_Fin'], axis=1)
y = df['Pasajeros']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos una instancia de la clase LinearRegression
modelo = LinearRegression()

# Entrenamos el modelo utilizando los datos de entrenamiento
modelo.fit(X_train, y_train)

# Hacemos predicciones utilizando los datos de prueba
y_pred = modelo.predict(X_test)
