import random
carcon = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
loncon = int(input('Escriba la longitud de la contraseña: '))
contrasena = ""

for i in range(loncon):
    contrasena += random.choice(carcon)

print(f'tu contraseña es {contrasena}')
