import pyfiglet
titulo = pyfiglet.figlet_format("Calculadora simple")


# =======================================================================


def sum(opp):
    try:
        num1 = int(input("Primer número a " + opp + ": "))
        num2 = int(input("Segundo número a " + opp + ": "))
    except ValueError:
        print("No es un número")

    result = num1 + num2
    result = str(result)

    print("El restultado es: " + result)


# =======================================================================


def res(opp):
    try:
        num1 = int(input("Primer número a " + opp + ": "))
        num2 = int(input("Segundo número a " + opp + ": "))
    except ValueError:
        print("No es un número")

    result = num1 - num2
    result = str(result)

    print("El restultado es: " + result)


# =======================================================================


def mult(opp):
    try:
        num1 = int(input("Primer número a " + opp + ": "))
        num2 = int(input("Segundo número a " + opp + ": "))
    except ValueError:
        print("No es un número")

    result = num1 * num2
    result = str(result)

    print("El restultado es: " + result)


# =======================================================================


def div(opp):
    try:
        num1 = int(input("Primer número a " + opp + ": "))
        num2 = int(input("Segundo número a " + opp + ": "))
    except ValueError:
        print("No es un número")

    result = num1 / num2
    result = str(result)

    print("El restultado es: " + result)


# =======================================================================


def main():
    print(titulo)
    opc = """
    ¿Que operacion quieres realizar?
    
    1. Suma.
    2. Resta.
    3. Multiplicación.
    4. Division:
    
    Elige una opción: """
    opc = int(input(opc))

    try:
        if opc == 1:
            sum("sumar")
        elif opc == 2:
            res("restar")
        elif opc == 3:
            mult("multiplicar")
        elif opc == 4:
            div("dividir")

    except ValueError:
        print("Orden erronea. Por favor intente con otra")


if __name__ == '__main__':
    main()
