def oddEvenGenerator(type, limit):
    if type == "odd":
        initial_value = 1
    else:
        initial_value = 2
    while initial_value < limit:
        yield initial_value
        initial_value += 2

for value in oddEvenGenerator("odd", 10):
    print("Impares", value)

for value in oddEvenGenerator("even", 10):
    print("Pares", value)

