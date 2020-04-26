from .caesar import Caesar
from nmcipher.cli import Parser

def encrypt_func(key, symbols, message):
    cipher = Caesar(key, symbols)
    print(message)
    print(cipher.encrypt(message))

def decrypt_func(key, symbols, message):
    cipher = Caesar(key, symbols)
    print(message)
    print(cipher.decrypt(message))

def hack_func(method, symbols, message):
    if method != "brute":
        raise NotImplementedException("Caesar class only supports brute-force method")
    for key in range(len(symbols)):
        cipher = Caesar(key, symbols)
        print(f"With key = {key}:")
        print(f"\tOutput: {cipher.decrypt(message)}")


if __name__ == '__main__':
    Parser(encrypt_func, decrypt_func, hack_func)()
