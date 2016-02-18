#Jia Yu
#CS1122
#HW 03

import binascii

def toBinary (x):
    ret = bin(x)
    return ret[2:]

def toHexadecimal(x):
    ret = hex(int(x,2))
    return ret

def toASCII(x):
    ret = ""
    for val in x:
        ret = ret + (str (binascii.unhexlify(val))[2])
    return ret 

def toDecimal(x):
    num = str(x)
    ret = 0
    for i in range (len(num)-1,-1,-1):
        ret += int (num[i]) * (8**(len(num) - 1 - i))
    return ret
        
def main():
    print("The binary of 26 is", toBinary(26))
    print("The binary of 57 is", toBinary(57))
    print("The binary of 123 is", toBinary(123))
    print("The binary of 85 is", toBinary(85))
    print("The binary of 38 is", toBinary(38))

    lst1 = ["48", "65", "6c", "6c", "6f", "20", "57", "6f", "72", "6c", "64"]
    lst2 = ["41", "53", "43", "49", "49", "20", "77", "68", "61", "74", "20", "79", "6f", "75", "20", "64", "69", "64", "20", "74", "68", "65", "72", "65"]
    lst3 = ["39", "41", "4d", "20", "69", "73", "20", "74", "6f", "6f", "20", "65", "61", "72", "6c", "79", "20", "66", "6f", "72", "20", "63", "6c", "61", "73", "73"]
    lst4 = ["43", "6f", "6d", "70", "75", "74", "65", "72", "73", "20", "61", "72", "65", "20", "6d", "61", "67", "69", "63"]
    lst5 = ["57", "68", "61", "74", "20", "74", "68", "65", "20", "68", "65", "78", "3f"]

    print("The ASCII value of lst1 is",toASCII(lst1))
    print("The ASCII value of lst2 is",toASCII(lst2))
    print("The ASCII value of lst3 is",toASCII(lst3))
    print("The ASCII value of lst4 is",toASCII(lst4))
    print("The ASCII value of lst5 is",toASCII(lst5))

    str1 = "10101010"
    str2 = "00001011101011101101111010101101"
    str3 = "11001010111111101111101011001110"
    str4 = "10111110111011111101000000001101"
    str5 = "11111111111111111001000001100010"

    print("The hexadecimal value of str1 is", toHexadecimal(str1))
    print("The hexadecimal value of str2 is", toHexadecimal(str2))
    print("The hexadecimal value of str3 is", toHexadecimal(str3))
    print("The hexadecimal value of str4 is", toHexadecimal(str4))
    print("The hexadecimal value of str5 is", toHexadecimal(str5))

    print("The decimal value of octal 63 is", toDecimal(63))
    print("The decimal value of octal 10 is", toDecimal(10))
    print("The decimal value of octal 42 is", toDecimal(42))
    print("The decimal value of octal 77 is", toDecimal(77))
    print("The decimal value of octal 113 is", toDecimal(113))

main()
