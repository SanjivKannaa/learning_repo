while True:
    from cryptography.fernet import Fernet
      
    # we will be encryting the below string.
    message = input("enter : ")
      
    # generate a key for encryptio and decryption
    # You can use fernet to generate 
    # the key or use random key generator
    # here I'm using fernet to generate key
    import pickle

    
    key = Fernet.generate_key()
      
    # Instance the Fernet class with the key
      
    fernet = Fernet(key)
      
    # then use the Fernet class instance 
    # to encrypt the string string must must 
    # be encoded to byte string before encryption
    encMessage = fernet.encrypt(message.encode())
    print('key : ', key)
    print("original string: ", message)
    print("encrypted string: ", encMessage)
      
    # decrypt the encrypted string with the 
    # Fernet instance of the key,
    # that was used for encrypting the string
    # encoded byte string is returned by decrypt method,
    # so decode it to string with decode methos
    decMessage = fernet.decrypt(encMessage).decode()



    print("decrypted string: ", decMessage)
'''

import os
from cryptography.fernet import Fernet
key = Fernet.generate_key()
print('key', key)
f = Fernet(key)
print('f', f)
token = f.encrypt(b'password')
print('token', token)
'''



def encry(data):
    f = open(file, "rb")
    key = pickle.load(f)
    f.close()
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decry(data):
    f = open(file, "rb")
    key = pickle.load(f)
    f.close()
    fernet = Fernet(key)
    return fernet.decrypt(data).decode()