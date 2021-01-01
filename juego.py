import random

def run():
    numero_aleatorio = random.randint(1,100)
    numero_elejido = int(input("elige un número del 1 al 100: "))

    while numero_elejido != numero_aleatorio:
        if numero_elejido < numero_aleatorio:
            print("elige un número más grande")
        else:
            print("elige un número más pequeño")
        numero_elejido = int(input("elige otro número: "))
    print("ganaste")


if __name__ == '__main__':
    run()