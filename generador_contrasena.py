import random

def generar_contrasena():
    mayusculas = ["A", "B", "C"]
    minusculas = ["a", "b", "c"]
    simbolos = ["!", "@", "#"]
    numeros = [1,2,3,4,5,6,7,8,9,0]

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena2 = []

    for i in range(15):
        caracter_random = str(random.choice(caracteres))
        contrasena2.append(caracter_random)
    
    contrasena2 = "".join(contrasena2)
    return contrasena2

def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena)

if __name__ == '__main__':
    run()