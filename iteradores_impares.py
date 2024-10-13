# Crear un iterador para los números impares

# Límite
limit = 10

# Crear iterador
odd_iter = iter(range(1, limit + 1, 2))
# range(start, stop, step)
# start: por donde empieza
# stop: donde para limit+1 = 10
# step: numero de posiciones que avanza

# Usar el iterador
for num in odd_iter:
    print(num)