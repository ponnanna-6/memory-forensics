import sys
import string

def xor(s):

	a = ''.join(chr(ord(i)^3) for i in s)
	return a

def decoder(x):	
	return x.encode("base64")	
	
	
print(xor("jm`wex3m0\k7oe"))	
print(decoder("slmmbmmb"))
#print(decoder(xor("am1gd2V4M20wXGs3b2U")))
