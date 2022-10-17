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

if __name__ == "__main__":
    print("La conversion de 56 con longitud de 8bits es:")
    print(ToBinary(1357,9))