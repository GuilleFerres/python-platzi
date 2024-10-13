to_do = ["Dirigirnos al hotel", 
         "Ir a almorzar", 
         "VIsitar un museo", 
         "Volver al hotel"]
print(to_do)
numbers = [1, 2, 3, 4, "cinco"]
print(type(numbers))
mix = ["uno", 2, 3.14, True, [1,2,3]]
print(len(mix))
print("El primer elemento es", mix[0])
print("El último elemento es", mix[-1])
string = "Hola mundo"
print("El primer elemento es", string[0])
print("El último elemento es", string[-1])
print(mix[0:2])
print(mix[:2]) # devuelve desde la posición 0 hasta la 2
print(mix[2:]) # devuelve desde la posición 2 hasta el final
print(mix[2:-2]) # devuelve la de en medio
mix.append(False)
print(mix)
mix.append(["a", "b"])
print(mix)
mix.insert(1,["a", "b"]) # Añade en la posición uno el array
print(mix)
print(mix.index(["a", "b"])) # Devuelve la primera posición del elemento
numbers = [1, 2, 100, 90.45, 3, 4, 5]
print("Mayor", max(numbers))
print("Menor", min(numbers))
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
del numbers
print(numbers)
