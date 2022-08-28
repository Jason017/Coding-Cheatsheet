### Binary to Decimal 
def binaryToDecimal(binary):
    decimal, i = 0, 0
    while(binary != 0):
        rem = binary % 10
        decimal = decimal + rem * pow(2, i)
        binary //= 10
        i += 1
    return decimal


### Decimal to Binary 
# Recursively
def decimalToBinary1(decimal):
    if decimal == 0:
        return 0
    else:
        return decimal % 2 + 10 * decimalToBinary1(decimal // 2)

# With built-in functions
def decimalToBinary2(decimal):
    return bin(decimal)[2:]

# Iteratively
def decimalToBinary3(decimal):
    if decimal == 0:
        return 0

    binary = 0
    pow = 0
    temp = decimal 
    
    while(temp > 0):
        binary = ((temp%2)*(10**pow)) + binary
        temp = int(temp/2)
        pow += 1
    return binary


### Decimal to a negative base int array
# https://github.com/Jason017/SWE-Interview-Question-Collection/blob/main/HRT/Solution.py
# https://en.wikipedia.org/wiki/Negative_base#Python
def decimalToBaseNeg(decimal, negBase):
    if decimal == 0:
        return [0]
    else:
        digits = []
        while decimal != 0:
            decimal, rem = divmod(decimal, negBase)
            if rem < 0:
                decimal += 1
                rem -= negBase
            digits.append(rem)
    return digits


x = 11
print(f'{x} in decimal: ', decimalToBinary1(x))
print(f'{x} in decimal: ', decimalToBinary2(x))

num = 10011010010
y = 1234
print(f'{num} in decimal: ', binaryToDecimal(num))
print(f'{y} in decimal: ', decimalToBinary1(y))
print(f'{y} in decimal: ', decimalToBinary2(y))
print(f'{y} in decimal: ', decimalToBinary3(y))

print(decimalToBaseNeg(5730, -2))

