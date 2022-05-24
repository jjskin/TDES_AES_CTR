from Crypto.Cipher import AES
from Crypto.Cipher import DES3
from secrets import token_bytes
import datetime

key = token_bytes(24)

def TDESEncrypt(read):
    reszta = 24 - len(read)%24
    read = read + b' '*reszta
    cipherT = DES3.new(key, DES3.MODE_ECB)
    pDES3 = cipherT.encrypt(read)
    return pDES3

def AESEncrypt(read):
    reszta = 32 - len(read)%32
    read = read + b' '*reszta
    cipher = AES.new(key, AES.MODE_ECB)
    pAES = cipher.encrypt(read)
    return pAES
    
#Input file--------------------------------------------------------------------------------------#
input = open("0.bit", "rb")
read = input.read()
#------------------------------------------------------------------------------------------------#


#AES kodowanie-----------------------------------------------------------------------------------#
startAESE = datetime.datetime.now()
outBytesAES = AESEncrypt(read)
durationAESE = datetime.datetime.now() - startAESE

outByte = open('outputBytesAES_ECB.bit', 'wb')
outByte.write(outBytesAES)
outByte.close()
#------------------------------------------------------------------------------------------------#


#3DES kodowanie----------------------------------------------------------------------------------#
startTDesE = datetime.datetime.now()
outBytes3DES = TDESEncrypt(read)
durationTDesE = datetime.datetime.now() - startTDesE

outByte2 = open('outputBytes3DES_ECB.bit', 'wb')
outByte2.write(outBytes3DES)
outByte2.close()
#------------------------------------------------------------------------------------------------#

input.close()