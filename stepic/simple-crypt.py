from simplecrypt import encrypt, decrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
# # passwords = ["9XB8nsIqRfYeswC", "4sEhUGLEZti9BiN", "bDjmT0NcIW8nzhb", "ZN6QQoMOO1ZQLUY", "RVrF2qdMpoq6Lib", "tnnX7HH3vJ9Hiji", "C24TJYYkqekv40l", "B2ropluPaMAitzE", "DRezNUVnr2zC0CP", "XCNmpTvvZb1n3mX"]
# for password in passwords:
#     print(simplecrypt.decrypt(password, encrypted))
# password = "9XB8nsIqRfYeswC"
# decrypted = decrypt('9XB8nsIqRfYeswC', encrypted)
# print(decrypted)
#ciphertext = "9XB8nsIqRfYeswC"
pswd = "RVrF2qdMpoq6Lib"
#enc = encrypt(pswd, ciphertext)
plaintext = decrypt(pswd, encrypted)
print(plaintext)
