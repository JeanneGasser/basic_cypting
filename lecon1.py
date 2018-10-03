# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:33:40 2018

@author: jeann
"""
from nltk import RegexpTokenizer
toknizer = RegexpTokenizer(r'''\w'|\w+|[^\w\s]''')
from string import punctuation
import unidecode
#A FAIRE: normalisation du texte: lower, strip, retrait accent
#Prise en charge de la ponctuation? Possible? 
class EncryptDecrypt:
    """
    For each letter return the numerical position in alphabet
    Or for each number return the corresponding letter
    """
    def encrypt(self, text):
        
        text = unidecode.unidecode(text.lower().strip())
        
        token = toknizer.tokenize(text)
        
        return " ".join(["-".join([str(ord(l)-96) for l in word if word not in punctuation ]) for word in token])
    
    def decrypt(self, text):
        
        to_decrypt =   [word.split("-") for word in text.split(" ")]
        return " ".join([("".join([chr(int(l)+96) for l in word])) for word in to_decrypt])

EncryptDecrypt().encrypt(" this is a test")
EncryptDecrypt().decrypt()
#A FAIRE: Unidecode pour retirer les accents de raw input
what_to_do = input("Voulez vous décrypter ou encrypter \n \n")

if what_to_do.lower().strip()== "encrypter":
    
    to_encrypt = input("Veuillez insérer votre texte à encrypter \n \n")
    print(EncryptDecrypt().encrypt(to_encrypt))
    
elif what_to_do.lower().strip() == "decrypter":
    
    to_decrypt = input("Veuillez insérer le texte à décrypter (lettres séparées de -) \n \n ")
    print(EncryptDecrypt().decrypt(to_decrypt))

