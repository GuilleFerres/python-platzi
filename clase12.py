numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:
    print("Aquí i es igual a: ", i + 1)

for i in range(3, 10):
    print(i)
fruits = ["manzana", "pera", "uva", "naranja", "tomate"]
for fruit in fruits:
    if fruit == "naranja":
        print("Naranja encontrada!")

x = 0
while x < 5:
    if x == 3:
        break
    print(x)
   
    x += 1
for i in numbers:
    if i == 3:
        continue
    print("Aquí i es igual a: ", i)