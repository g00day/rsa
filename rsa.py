# RSA encryption algorithm
from random import randint
from math import gcd

"""
    Receiver it is the class that represents the work of receiver of an int message - m(decoding, generating private&secret keys),
    whereas Encoder class provide all needed functions to encrypt this m to c
    ------------------------------------------------------------
    To get samples of using this algoritm you may see samples.py
"""

# Auxiliary functions
# They are needed in making p and q numbers
def get_prime(start, end):

    while True:

        num = randint(start, end)
        if is_prime(num):
            return num
        
def is_prime(num):

    if num < 2:
        return False

    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False

    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    return gcd(a, b) == 1


class Receiver:


    def __init__(self):
        self.__p = get_prime(10, 100)
        self.__q = get_prime(10, 100)
        self.__f_n = (self.__p-1)*(self.__q-1)
    
    def __set_e__(self):
        f_n = self.__f_n
        e = 65537

        while e != 3:
            if are_coprime(e, f_n):
                self.e = e
                return
            else:
                e -= 2 
    
    def __set_d__(self):
        f_n = self.__f_n
        e = self.e
        d = pow(e, -1, f_n)
        self.__d = d

    
    def __decode__(self, c):
        self.__set_d__()
        d = self.__d
        n = self.get_public_encryption_keys()[1]

        msg = pow(c, d, n)
        return msg
    
    def get_public_encryption_keys(self):

        n = self.__p * self.__q
        self.__set_e__()
        return self.e, n

    def get_decoded_msg(self, c):
        return self.__decode__(c)
    

    

class Encoder:

    def __init__(self, e, n, msg):
        self.msg = msg
        self.e = e
        self.n = n

    def __encode__(self):
        msg = self.msg
        n = self.n
        e = self.e

        self.__c = msg ** e % n  # c is encoded message

    def get_c(self):
        # This method at first sets c - encoded message
        # And then returns it
        self.__encode__()
        return self.__c

