from .caesar import Caesar
from nmcipher.cli import Parser

def encrypt_func(key, message, symbols):
    cipher = Caesar(key, symbols)
    print(message)
    print(cipher.encrypt(message))

def decrypt_func(key, message, symbols):
    cipher = Caesar(key, symbols)
    print(message)
    print(cipher.decrypt(message))

def hack_func(method, message, symbols):
    if method != "brute":
        raise NotImplementedError("Caesar class only supports brute-force method")
    for key in range(len(symbols)):
        cipher = Caesar(key, symbols)
        print(f"With key = {key}:")
        print(f"\tOutput: {cipher.decrypt(message)}")


if __name__ == '__main__':
    Parser(encrypt_func, decrypt_func, hack_func)()
