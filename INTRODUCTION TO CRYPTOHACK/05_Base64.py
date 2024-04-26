import base64

crypt = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'


key = bytes.fromhex(crypt)
key = base64.b64encode(key)

print(key)