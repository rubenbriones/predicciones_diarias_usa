# predicciones_diarias_usa
Predicciones diarias de las principales acciones americanas y su posterior análisis con python, viendo como influyen ciertos parámetros como grado de confianza en la predicción, gap de apertura, comportamiento durante los primeros 15min...

Ejemplos de los gráficos generados para detectar 'alpha':
- Las curvas graficadas son el 'kernel density estimated' para las predicciones alcistas (verde) y las bajistas (rojo).
- A parte de poder ver visualmente en donde las estimaciones son random (curvas muy superpuestas), y de cuando las estimaciones están generando algún tipo de 'alpha' (curvas no superpuestas), también se utiliza la librería Scipy para calcular de manera matemática las integrales de las curvas para luego calcular la intersección de ambas, y así tener un valor numérico que nos indique cuánto se superponen exactamente dichas curvas.
![](https://github.com/rubenbriones/predicciones_diarias_usa/blob/master/An%C3%A1lisis%20gr%C3%A1ficos%20generados/todo/pred%20por%20tipo%2001%2015min.png)
![](https://github.com/rubenbriones/predicciones_diarias_usa/blob/master/An%C3%A1lisis%20gr%C3%A1ficos%20generados/todo/pred%20por%20suma%20direcciones%2001%2015min.png)
![](https://github.com/rubenbriones/predicciones_diarias_usa/blob/master/An%C3%A1lisis%20gr%C3%A1ficos%20generados/todo/pred%20por%20gap%2002%2060min.png)

