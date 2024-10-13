valid_options = ["piedra", "papel", "tijera"]
player_one = input("Turno jugador 1: ")
formatter_player1 = player_one.lower().strip()

if formatter_player1 not in valid_options:
    print("Jugador uno, eso no es un dato válido, vuelva a introducir un dato válido.")
    player_one = input("Turno jugador 1: ")
    formatter_player1 = player_one.lower().strip()

player_two = input("Turno jugador 2: ")
formatter_player2 = player_two.lower().strip()

if formatter_player2 not in valid_options:
    print("Jugador dos, eso no es un dato válido, vuelva a introducir un dato válido.")
    player_two = input("Turno jugador 2: ")
    formatter_player2 = player_two.lower().strip()
    
if formatter_player1 == formatter_player2:
    print("Empate. Vuelvan a introducir sus opciones")
    player_one = input("Turno jugador 1: ")
    formatter_player1 = player_one.lower().strip()
    player_two = input("Turno jugador 2: ")
    formatter_player2 = player_two.lower().strip()
elif formatter_player1 == "piedra" and formatter_player2 == "tijera" or formatter_player1 == "tijera" and formatter_player2 == "papel" or formatter_player1 == "papel" and formatter_player2 == "piedra":
    print("Gana el juegador 1")
else:
    print("Gana el jugador 2")
