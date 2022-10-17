def frac_binario(num, precicion):
    
    binario = ''
    cifras = 0 
    while num > 0 and cifras < precicion:
        num = num * 2
        if num >= 1:
            binario = binario + '1'
            num = num - 1
        else:
            binario = binario + '0'
        cifras += 1
    return binario
    

def decimal_binario(num):

    binario = ''
    if(num == 0):
        binario = '0'
    while num > 0:
        binario = str(num % 2) + binario
        num = num // 2
    return binario

def PuntoFlotante(num):

    if (num > 0):
        signo = 0
    else : 
        signo = 1

    num=abs(num) #se toma el positivo

    num = str(num).split(".") #se separa la parte entera de la fraccionaria

    PEntera=decimal_binario(int(num[0])) #se convierte la parte entera a binario

    # indice para la parte entera , donde esta el primer 1
    ind = PEntera.index('1') + 1 

    # Pfraccionaria -> Binario ,  con precision 52 
    PFraccionaBinario = frac_binario(float("0." + num[1]), 52 - (len(PEntera) - ind ))

    #Normalizamos
    #Exponente sesgado
    #E = exp +  pow(2,n-1)-1    n = 11 
    # pow(2,10)-1 = 1023
    Exponente=(len(PEntera)- ind ) + 1023

    ExponenteBinario = decimal_binario(Exponente)

    # Mantisa se concatena la parte entera y la fraccionaria

    mantisa = PEntera[ind :] + PFraccionaBinario
    # Se llena con 0 , hasta una precicison de 52 la mantisa
    mantisa =  ('0' * (52 - len(mantisa))) + mantisa

    return (str(signo)), ExponenteBinario, mantisa
    

if __name__ == "__main__":

    num = float(input("Introduce el número: "))
    
    signo, exponente, mantisa = PuntoFlotante(num)
    print("\nConversión IEEE754 de presision doble de ",num," es:\n")
    print( signo+' | '+exponente+' | '+mantisa + '\n')