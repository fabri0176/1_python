def listarTerminos(**terminos):
    for index, value in terminos.items():
        print(f'{index}: {value}')


listarTerminos(Cali='Ciudad de Colombia, capital del departamento valle del cauca')