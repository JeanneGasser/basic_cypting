# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:56:32 2018

@author: jeann
"""

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


print("Bienvenue, avec ce programme vous allez pouvoir chiffrer ou déchiffrer du texte. \n \
      Chiffrement : lettres = position numérique dans l'alphabet")
textfile = input("Veuillez entrer votre texte ou un nom de fichier texte avec le chemin \n")
if ".txt" in textfile:
    
    txt = open(textfile,"r").read()
    
    what_to_do = input("Voulez vous décrypter ou encrypter \n \n")

    if unidecode.unidecode(what_to_do.lower().strip())=="encrypter":
           
        open(textfile.split(".")[0] + "_crypted.txt","w").write(EncryptDecrypt().encrypt(txt))
        print("Fichier encrypté et enregistré")
            
    
    elif unidecode.unidecode(what_to_do.lower().strip())=="decrypter":
    
        open(textfile.split(".")[0] + "_decrypted.txt","w").write(EncryptDecrypt().decrypt(txt))
        print("Fichier décrypté et enregistré")
    
    else: 
        print("Veuillez entrer une commande valide: Encrypter ou Decrypter")
else:
    
    what_to_do = input("Voulez vous décrypter ou encrypter \n \n")
    
    if what_to_do.lower().strip()=="encrypter":
        
        print(EncryptDecrypt().encrypt(textfile))
        
    elif unidecode.unidecode(what_to_do.lower().strip())=="decrypter":
        
        print(EncryptDecrypt().decrypt(textfile))
        
    else: 
        print("Veuillez entrer une commande valide: Encrypter ou Decrypter")
        