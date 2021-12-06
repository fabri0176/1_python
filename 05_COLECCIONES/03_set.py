planetas = {"Marte", "Venus", "Jupiter"}

print(planetas)

print('Número de planetas es:', len(planetas))

print('Marte está en la colección SET?', 'SI' if 'Marte' in planetas else 'NO')

# ELIMINAR UN ELEMENTO remove genera error si no existe el indice, discard elimina, si no existe el indce no genera error

planetas.discard('Saturno')
