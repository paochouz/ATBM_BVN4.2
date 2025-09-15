def mahoa(plaintext, k):
    ciphertext = ""
    for x in plaintext:
        if x.isalpha():
            base = ord('A') if x.isupper() else ord('a')
            c = (ord(x) - base + k) % 26 + base
            ciphertext += chr(c)
        else:
            ciphertext += x 
    return ciphertext

plaintext = "NguyenLeBaoChau"
k = 19
ciphertext = mahoa(plaintext, k)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
