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

    #Como volvere a usar la cadena invertida en la siguiente funcion no lo invierto
    #NewNum=NewNum[::-1]#como empiezo del ultimo al primero, invierto la cadena

    return NewNum

#Conversion de decimal a su complemento a 2
def Complemento_a_2(Num,nbits):
    #Convierto el numero a binario con nbits de longitud
    NewNum=ToBinary(Num,nbits)

    #Creo una lista para modificar cada indice del numero en binario
    Newlist=list(NewNum)

    #Invierto los numeros del numero en binario
    #Si es 0 lo cambio a 1
    #Si es 1 lo cambio a 0
    for i in range(len(Newlist)):
        if Newlist[i]=='0':
            Newlist[i]='1'
        else:
            Newlist[i]='0'

    #Ahora efectuamos la suma
    #Sumamos 00....01
    #Declaro un indice para poder efectuar la suma
    i=0
    #El bucle se repetira hasta encontrar el primer 0
    while Newlist[i]!='0':
        Newlist[i]='0'
        i=i+1

    #Despues de haber salido del bucle
    #En el indice que obtuve se pondra el 1
    Newlist[i]='1'

    #Depues de haber trabajado la lista lo cambiamos a un string
    NewN=''.join(Newlist)
    NewN = NewN[::-1]
    return NewN

if __name__ == "__main__":
    print("La conversion de 20 con longitud de 8bits en su complemento a 2 es:")
    print(Complemento_a_2(20,8))