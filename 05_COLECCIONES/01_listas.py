familia = ['Katherine', 'Nestor', 'Marina', 'Anabell', 'Jeison']


print(familia[-2])
print(familia[:4])
print("--------------------------------------")


familia.append('Luis Angel')
familia.remove('Jeison')

del familia[0]

for integrante in familia:
    print(integrante)

print(familia)


familia.clear()

print(familia)
