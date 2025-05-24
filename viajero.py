import itertools

# Distancias entre ciudades (matriz simétrica)
distancias = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Enumerar todas las permutaciones posibles (menos la ciudad de inicio fija)
ciudades = [0, 1, 2, 3]
permutaciones = itertools.permutations(ciudades[1:])  # Fijamos ciudad 0 como inicio

distancia_minima = float('inf')
mejor_ruta = []

for perm in permutaciones:
    ruta = [0] + list(perm) + [0]  # ida y vuelta
    distancia = sum(distancias[ruta[i]][ruta[i+1]] for i in range(len(ruta) - 1))
    if distancia < distancia_minima:
        distancia_minima = distancia
        mejor_ruta = ruta

print(f"Mejor ruta: {mejor_ruta}")
print(f"Distancia total: {distancia_minima}")
