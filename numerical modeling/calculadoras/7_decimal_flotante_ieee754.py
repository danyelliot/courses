def FraccionToBinary(num, precicion):
    k=1
    r_k=num
    N=''
    ind=0
    while(r_k!=0 and ind<precicion):
        if(2*r_k>=1):
            d_k=1
            N=N+str(d_k)

        else:
            d_k=0
            N = N + str(d_k)
        r_k=2*r_k-d_k
        ind += 1
    return N

def ToBinary(num):
    N_0=num
    N=''
    while N_0!=0:
        if N_0 % 2 !=0 :
            ak=1
        else :
            ak=0

        N_0=(N_0-ak)/2
        N=N+str(ak)#concateno el ak que obtengo en cada iteracion
    N=N[::-1]#como empiezo del ultimo al primero, invierto la cadena
    return N

def PuntoFlotante(num):
    #el signo por defecto es 0
    signo = 0
    #en caso el numero sea menor que 0 el signo sera 1
    if (num < 0):
        signo = 1

    #convertimos el numero en positivo despues de haber defininido
    #el bit del signo
    num=abs(num)

    #obtenemos la parte entera del numero usando la funcion "int()"
    #y lo transformamos a binario
    PEntera=ToBinary(int(num))

    #obtenemos el indice para la parte entera cuando
    #encontramos el primer '1' de izquierda a derecha
    ind = PEntera.index('1')

    #Convertimos a binario la parte fraccionaria con precision 23
    PFraccionaBinario = FraccionToBinary(num - int(num), 23-(len(PEntera) - ind - 1))


    #Ahora normalizamos el numero flotanten dejando el ultimo digito
    #el cual se llama bit escondido
    #Despues de normalizar tenemos que contar cuantas comas se corrieron
    #Despues el exponente que obtenemos de lo anterior se le suma 2^(8-1)-1
    Exponente=(len(PEntera)-ind-1)+127
    #Despues de lo anterior onvertimos a binario el exponenete que obtuvimos
    ExponenteaBinario=ToBinary(Exponente)

    #Para la mantisa concatenamos la parte entera desde el indice 1
    #ya que el indice 0 bendria a ser el bit escondido
    #lo concatenamos con la parte fraccionaria en binario
    mantisa = PEntera[ind + 1:] + PFraccionaBinario
    #Ahora rellenamos con 0 si fuera necesario hasta una precicison de 23 la mantisa
    mantisa =  ('0' * (23 - len(mantisa))) + mantisa

    return signo, ExponenteaBinario, mantisa

if __name__ == "__main__":
    signo, exponente, mantisa=PuntoFlotante(-31.125)
    print("La conversion IEEE754 de presision simple de -31.125 es:")
    print(str(signo)+'|'+exponente+'|'+mantisa)