menu = """
Bienvenidos al conversor de monedas ❤
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos Mexicanos
"""
def convertir(pais, valor):
    pesos = input("¿Cuántos pesos " + pais + " tienes?")
    pesos = float(pesos)
    dolares = pesos / int(valor)
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")

opcion = int(input(menu))

if opcion == 1:    
    convertir("colombianos", 3875)
elif opcion == 2:    
    convertir("argentinos", 65)
elif opcion == 3:    
    convertir("mexicanos", 24)
else:
    print("ingrese una opción correcta")
