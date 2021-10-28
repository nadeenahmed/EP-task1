Hex = input()
binary = str()
for i in Hex:
    if i == '0':
        binary += '0000'
    elif i == '1':
        binary += '0001'
    elif i == '2':
        binary += '0010'
    elif i == '3':
        binary += '0011'
    elif i == '4':
        binary += '0100'
    elif i == '5':
        binary += '0101'
    elif i == '6':
        binary += '0110'
    elif i == '7':
        binary += '0111'
    elif i == '8':
        binary += '1000'
    elif i == '9':
        binary += '1001'
    elif i == 'A':
        binary += '1010'
    elif i == 'B':
        binary += '1011'
    elif i == 'C':
        binary += '1100'
    elif i == 'D':
        binary += '1101'
    elif i == 'E':
        binary += '1110'
    elif i == 'F':
        binary += '1111'

print(binary)
