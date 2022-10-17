#Conversion de base 10 a binario con precicion de nbits
def ToBinary(Num, nbits):
    #asignamos el N₀
    N_0=Num
    NewNum=''
    #si el numero es impar el aₖ es 1 caso contrario es 0
    while N_0!=0:
        if N_0 % 2 !=0 :
            ak=1
        else :
            ak=0
        N_0=(N_0-ak)/2 #en la sgte iteracion el numero Nₖ es la mitad del anterior(Nₖ₋₁)
        NewNum=NewNum+str(ak)#concateno el ak que obtengo en cada iteracion

    while len(NewNum)<nbits: #concateno los 0 restantes para completar la longitud de nbits
        NewNum+=str(0)
    NewNum=NewNum[::-1]#como empiezo del ultimo al primero, invierto la cadena
    return NewNum

#Diccionario de las conversiones en base hexadecimal
HexadecimalCharacter = {'0': 0, '1': 1, '2': 2, '3': 3,
                        '4': 4, '5': 5, '6': 6, '7': 7,
                        '8': 8, '9': 9, 'a': 10, 'b': 11,
                        'c': 12, 'd': 13, 'e': 14, 'f': 15}

#Invierto las claves de la tabla anterior
HexadecimalCharacterInver = dict((v, k) for k, v in HexadecimalCharacter.items())

#Conversion de hexadecimal a decimal
def HexadecimalToDecimal(num:str):
    #Base 16
    beta=16

    #Pongo en minusculas el numero para no tener inconvenientes
    num = num.lower()

    #Creamos el indice que es el tamño de la cadena - 1
    i = len(num) - 1

    #Inicialisamos el b₀ con el primer caracter de la cadena
    #No olvidar que siempre se trabajara con el diccionario de carcteres
    b_0 = HexadecimalCharacter[num[0]]

    #Descomponemos el numero
    for n in range(i):
        b_0 = (HexadecimalCharacter[num[n+1]]) + (beta * b_0)
    return b_0



#Conversion de Decimal a Hexadecimal
def DecimalToHexadecimal(num):
    #Inicializamos la cadena vacia
    hexadecimal=''
    #Aplicamos un metodo conocido para conversion de bases
    #Sin olvidar que simpre se trabaja con el diccionario de caracteres
    #En este caso se trabaja con el diccionario invertido
    while (num > 0):
        resto = num % 16
        hexadecimal = HexadecimalCharacterInver[resto] + hexadecimal
        num = num // 16
    return hexadecimal



#Conversion de Hexadecimal a binario
def HexadecimalToBinario(num:str):
    #Inicialisamos convirtiendo el numero en una lista
    #Con el fin de poder modificar cada indice
    numlist=list(num)

    #Para cada indice de la lista tenemos que convetirlo a
    #Binario con precicion 4
    for i in range(len(numlist)):
        numlist[i]=ToBinary(HexadecimalCharacter[numlist[i]],4)

    #Despues de haber convertido cada indice a binario lo juntamos
    #Creando una nueva cadena
    Newnum = ''.join(numlist)
    return Newnum
if __name__ == "__main__":
    print("La conversion de fb3d a base 10 es:")
    print(HexadecimalToDecimal('fb3d'))
    print("La conversion de 64317 a base hexadecimal es:")
    print(DecimalToHexadecimal(64317))
    print("La conversion de f12 en base hexadecimanl a binario es:")
    print(HexadecimalToBinario('f12'))