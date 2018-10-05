# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:33:40 2018

@author: jeann
"""
#Package import
from nltk import RegexpTokenizer
toknizer = RegexpTokenizer(r'''\w'|\w+|[^\w\s]''')
from string import punctuation
import unidecode

#Class construction
class EncryptDecrypt:
    """
    For each letter return the numerical position in alphabet
    Or for each number return the corresponding letter
    """
    def encrypt(self, text):
        
        #Remove accent, caps and excess white space 
        text = unidecode.unidecode(text.lower().strip())
        
        token = toknizer.tokenize(text)
        #ord return ascii code of the letter. In order to have the alphabet position : -96
        return " ".join(
                ["-".join([str(ord(l)-96) for l in word if l.isalpha()])
                        for word in token if word not in punctuation])
    
    def decrypt(self, text):
        
        #chr gives the char attached to an ascii code. Since we're using letter position, need to add +96
        #Encrypted word given in format xx-xx-xx, hence the split. 
        to_decrypt =   [word.split("-") for word in text.split(" ")]
        return " ".join(
                [("".join([chr(int(l)+96) for l in word]))
                for word in to_decrypt])

#User input and class output
what_to_do = input("Voulez vous décrypter ou encrypter \n \n")

if what_to_do.lower().strip()=="encrypter":
    
    to_encrypt = input("Veuillez insérer votre texte à encrypter \n \n")
    print(EncryptDecrypt().encrypt(to_encrypt))
    
elif unidecode.unidecode(what_to_do.lower().strip())=="decrypter":
    
    to_decrypt = input("Veuillez insérer le texte à décrypter (lettres séparées de -) \n \n ")
    print(EncryptDecrypt().decrypt(to_decrypt))
    
else: 
    print("Veuillez entrer une commande valide: Encrypter ou Decrypter")



