## Encryption

* pycrypto

```
import string
import random

from Crypto.Cipher import AES

print(AES.block_size)
print(string.ascii_letters)

key = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)
print(key)

iv = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)
print(iv)

text = 'Hello Python!!!'

cipher = AES.new(key, AES.MODE_CBC, iv)
padding_length = AES.block_size - len(text) % AES.block_size
text += chr(padding_length) * padding_length
cipher_text = cipher.encrypt(text)
print(cipher_text)

cipher2 = AES.new(key, AES.MODE_CBC, iv)
decrypted_text = cipher2.decrypt(cipher_text)
print(decrypted_text[:-1])
```
```
16
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
ijlolfvwAMeqJoLT
TnrmFkTGPbwnPIim
b'\x99bl\xf3H\xe8;f\xabm~%;\xc5\xc1\x94'
b'Hello Python!!!'
```

* hashlib

```
import hashlib

print(hashlib.sha256(b'ab').hexdigest())
print(hashlib.sha256(b'aa').hexdigest())

name = 'user1'
password = '123456'

db = {}

def get_digest(password):
    password = bytes(password, 'utf-8')
    digest = hashlib.sha256(password).hexdigest()
    return digest

db[name] = get_digest(password)
print(db)

def islogin(username, password):
    return get_digest(password) == db[username]

print(islogin(name, password))
```

```
fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603
961b6dd3ede3cb8ecbaacbd68de040cd78eb2ed5889130cceb4c49268ea4d506
{'user1': '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'}
True
```

