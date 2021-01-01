def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3
    }
    

    for hola, chao in mi_diccionario.items():
        print(hola + " " + str(chao))


if __name__ == '__main__':
    run()