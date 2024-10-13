is_member = True
age = 11

if is_member:
    if age >= 15:
        print("Tienes acceso, por ser miembro y tener 15 o más años")
    else:
        print("No tienes acceso ya que eres miembro, pero menor de 15 años")
else:
    print("No tienes acceso, porque no eres miembro")