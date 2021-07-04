import hashlib
plaintext= input("Enter the string to be encrypted")
result = hashlib.md5(plaintext.encode())
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())
