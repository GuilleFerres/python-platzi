def greet(name, last_name = "No tiene apellido"):
    print("Hola", name, last_name)

greet("Guille", "Ferres")
greet("Diego")
greet(last_name="Ferres", name="Guille")