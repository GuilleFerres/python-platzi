numbers = {1: "uno", 2: "dos", 3: "tres"}
print(numbers[2])
information = {"nombre": "Guille",
                "apellido": "Ferres",
                "altura": 1.75,
                "edad": 36  
              }
print(information)
del information["edad"]
print(information)
claves = information.keys()
print(claves)
# print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {
             "Guille": {"nombre": "Guille",
                "apellido": "Ferres",
                "altura": 1.75,
                "edad": 36  
              },
              "Paloma": {"nombre": "Paloma",
                "apellido": "Ortega",
                "altura": 1.60,
                "edad": 34  
              }
            }
print(contacts["Guille"])