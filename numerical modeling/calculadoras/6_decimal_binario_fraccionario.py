
def decimal_binario(num):
    
    binario = ''
    if(num == 0):
        binario = '0'
    while num > 0:
        binario = str(num % 2) + binario
        num = num // 2
    return binario

def frac_binario(num):
    
    binario = ''
    while num > 0:
        num = num * 2
        if num >= 1:
            binario = binario + '1'
            num = num - 1
        else:
            binario = binario + '0'
    return binario



if __name__ == "__main__":

    num_str = input("Introduce el número: ")

    num = num_str.split(".")

    print(decimal_binario(int(num[0])) + "." + frac_binario(float("0." + num[1])))

