def binaryToDecimal(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary //= 10
        i += 1
    return decimal

def decimalToBinary1(num):
    if num == 0:
        return 0
    else:
        return num % 2 + 10 * decimalToBinary(num // 2)

def decimalToBinary(n):
    return bin(n)[2:]

num = 10011010010
x = 1234
print(f'{num} in decimal: ', binaryToDecimal(num))
print(f'{x} in decimal: ', decimalToBinary(x))



