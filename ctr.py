from Crypto import Random
from Crypto.Util import Counter
from Crypto.Cipher import AES
from Crypto.Cipher import DES3
from secrets import token_bytes

key = token_bytes(24)

def AESencrypt(data):
    cipher = AES.new(key, AES.MODE_CTR)
    return cipher.encrypt(data), cipher.nonce

def TDESencrypt(data):
    cipher = DES3.new(key, DES3.MODE_CTR, nonce=token_bytes(1))
    return cipher.encrypt(data)

#Input file--------------------------------------------------------------------------------------#
input = open("0.bit", "rb")
read = input.read()
#------------------------------------------------------------------------------------------------#
'''
#AES kodowanie-----------------------------------------------------------------------------------#
outputByteAES, nonce = AESencrypt(read)
outByte = open('outputBytesAES.bit', 'wb')
outByte.write(outputByteAES)
outByte.close()
#------------------------------------------------------------------------------------------------#
'''
#3DES kodowanie-----------------------------------------------------------------------------------#
outputByteTDES = TDESencrypt(read)
outByte = open('outputBytes3DES.bit', 'wb')
outByte.write(outputByteTDES)
outByte.close()
#------------------------------------------------------------------------------------------------#


input.close()