
# requires Python 2.7.9 (instead i use Python 3.6.5) 
# install pycryptodome instead of PyCrypto (pip3 install pycryptodome)

import base64
import argparse
import glob
import itertools
import sys
import os
import logging
import shutil
import struct
import mmap # Memory-mapped file support
import binascii
# import Crypto # pycryptodome

# from Crypto import Random
# from Crypto.Cipher import PKCS1_OAEP
# from Crypto.Cipher import PKCS1_OAEP, AES
# from Crypto.PublicKey import RSA
# from Crypto.Hash import SHA256

"""example"""
# print(sys.argv[0])
# print("number of argument:", len(sys.argv))
# print("the arguments are: ", str(sys.argv))
"""type
python cipher.py a b
cipher.py
number of argument: 3
the arguments are: ['cipher.py', 'a', 'b']
"""
cfg = {
	# The place all of the code lives
	'magic'  : "EOZT",
	'key_offset' : 0x10,
	'key_size'   : 0x100,	
	'nonce_offset' : 0x110,	
	'nonce_size'   : 0xC,	
	'tag_offset' : 0x11C,
	'tag_size'   : 0x10,	
	'log_offset' : 0x130,	
	'log_size'   : 0xA0,
}

#sys.argv = ["cipher_test.py", "RSA_private_key_PEM", "OCIMEM_0x14692730.bin"]
sys.argv = ["cipher_test.py", "RSA_private_key_PEM", "hello.txt"]
#sys.argv = ["cipher_test.py", "RSA_private_key_PEM", "OCIMEM.bin"]

if(len(sys.argv)) != 3:
	print("cipher_test.py <RSA_private_key_PEM> <OCIMEM_dump.bin>")

fo = open(sys.argv[2], 'rb')
s = mmap.mmap(fo.fileno(), 0, access=mmap.ACCESS_READ)
# if s.find(b'EOZT') != -1:
#     print('true')
#offset = s.find(bytes(cfg['magic'], 'utf-8')) # Python 3
offset = s.find(bytes(cfg['magic'])) # Python 2
if offset != -1:
	print("Found magic offset = ", hex(offset))
"""read from offset (value in offset included)"""
fo.seek(offset) 
print(fo.readline())
print("test = " + ":".join("{}".format(c) for c in range(0,10)))
