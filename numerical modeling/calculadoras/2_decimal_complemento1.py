def dec_bin(num): # dec -> bin

    binario = ''
    if(num == 0):
        binario = '0'
    while num > 0:
        binario = str(num % 2) + binario
        num = num // 2
    return binario

def empaquetado(num,N) : #funcion para empaquetar el numero binario
    
    # pow(2,7) = 128
    if num<=pow(2,7):
        
        while len(N)<8:
            N = str(0) + N
        
    # pow(2,15) = 32768
    elif num>pow(2,7) and num<=pow(2,15):

        while len(N)<16:
            N = str(0) + N

    # pow(2,31) = 2147483648
    elif num>pow(2,15) and num<pow(2,31):

        while len(N)<32:
            N = str(0) + N

    return N


def complemento(N) : # funcion para calcular el complemento a 1

    newN = ''
    for i in N:
        if i=='0':
            newN+='1'
        else :
            newN+='0'
    return newN

def calculadora(num):

    N = dec_bin(abs(num))

    # Para poner un numero en complemento a 1 debemos tener en cuenta que el numero binario 
    # deberá estar empaquetado, esto es con un formato fijo de 8, 16 o 32 bits según sea necesario su tamaño.
    # Ese seria el numero en positivo , para conseguir el numero en negativo, debemos pasar todos los dígitos binarios 
    # a su opuesto.
    # ref. binario.org

    N = empaquetado(abs(num),N)


    if (num>=0):
         print(complemento(N))
    else :
        print(N)


if __name__ == "__main__":

    n = int(input("Ingrese un numero: "))
    calculadora(n)
