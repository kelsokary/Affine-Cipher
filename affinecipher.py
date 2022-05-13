import sys
import string


lower = string.ascii_lowercase # lowercase letters
upper = string.ascii_uppercase # uppercase letters
m = len(lower)

calcenc = lambda c, a, b: (a * c + b) % m # encryption function for a single letter
calcdec = lambda c, a, b: (keyinverse(a, m) * (c - b)) % m # decryption function for a single letter

# calculates the modular multiplicative inverse a^-1
def keyinverse(a, m) :
    for i in range(m) :
        if (a * i % m == 1) :
            return i
    return -1;

def encryption(p, a, b) :
    c = ""
    for i in p :
        if i.isalpha() :
            if i in lower :
                c += lower[calcenc(lower.index(i), a, b)]
            else :
                c += upper[calcenc(upper.index(i), a, b)]
        else :
            c += i
    return c

def decryption(c, a, b) :
    p = ""
    for i in c :
        if i.isalpha() :
            if i in lower :
                p += lower[calcdec(lower.index(i), a, b)]
            else :
                p += upper[calcdec(upper.index(i), a, b)]
        else :
            p += i
    return p

def gcd(a, b):
    # Everything divides 0
    if (a == 0 or b == 0): return 0
    # base case
    if (a == b): return a
    # a is greater
    if (a > b):
        return gcd(a - b, b)
    # b is greater
    return gcd(a, b - a)

def isCoprime(a, b):
    if (gcd(a, b) == 1):
        return True;
    else:
        return False;

if __name__ == "__main__" :

    if len(sys.argv) < 5 :

        print("Usage: python3 affinecipher.py <type> <string> <a> <b>")
        print('''
        - type    : {enc: encryption, dec: decryption}
        - string  : the text you want to enrypt or decrypt
        - a       : the first operand of the key
        - b       : the second operand of the key
    ''')

        print("Note: make sure you add double quotes in case the string has whitespaces")
        exit()
    
    args= [i for i in sys.argv]
    try :
        a = int(args[3])
        b = int(args[4])
    
    except :
        print('Error: Operands must be numbers not strings')
        exit()

    if not isCoprime(a, m):
        print('Warning: Operand "a = ' + str(a) + '" is not coprime with "m = ' + str(m) + '"')

    if args[1] == "enc" :
        print(encryption(args[2], a, b))
    elif args[1] == "dec" :
        print(decryption(args[2], a, b))
    else :
        print("Error: Unvalid type of operation")
