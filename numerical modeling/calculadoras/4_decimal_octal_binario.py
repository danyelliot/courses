
def decimal_octal() : # funcion para convertir de decimal a octal
    num = int(input("Introduce un número decimal: "))
    octal = ''
    while num > 0:
        octal = str(num % 8) + octal
        num = num // 8
    print(octal)

def octal_decimal() : # funcion para convertir de octal a decimal
    num = input("Introduce un número octal: ")
    decimal = 0
    for i in range(len(num)):
        decimal += int(num[i]) * 8 ** (len(num) - i - 1)
    print(decimal)

def octal_binario() : # funcion para convertir de octal a binario
    num = input("Introduce un número octal: ")
    binario = ''
    for i in range(len(num)):
        if num[i] == '0':
            binario += '000'
        elif num[i] == '1':
            binario += '001'
        elif num[i] == '2':
            binario += '010'
        elif num[i] == '3':
            binario += '011'
        elif num[i] == '4':
            binario += '100'
        elif num[i] == '5':
            binario += '101'
        elif num[i] == '6':
            binario += '110'
        elif num[i] == '7':
            binario += '111'
    print(binario)

def binario_octal() : # funcion para convertir de binario a octal
    num = input("Introduce un número binario: ")
    octal = ''
    if len(num) % 3 == 1:
        num = '00' + num
    elif len(num) % 3 == 2:
        num = '0' + num
    
    for i in range(0, len(num), 3):
        if num[i:i+3] == '000':
            octal += '0'
        elif num[i:i+3] == '001':
            octal += '1'
        elif num[i:i+3] == '010':
            octal += '2'
        elif num[i:i+3] == '011':
            octal += '3'
        elif num[i:i+3] == '100':
            octal += '4'
        elif num[i:i+3] == '101':
            octal += '5'
        elif num[i:i+3] == '110':
            octal += '6'
        elif num[i:i+3] == '111':
            octal += '7'
    print(octal)



if __name__ == "__main__":

    print("1. Decimal a Octal")
    print("2. Octal a Decimal")
    print("3. Octal a Binario")
    print("4. Binario a Octal")
    print("5. Salir")

    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        decimal_octal()
    elif opcion == 2:
        octal_decimal()
    elif opcion == 3:
        octal_binario()
    elif opcion == 4:
        binario_octal()
    elif opcion == 5:
        print("Gracias por usar el programa")
    else:
        print("Opción no válida")


    