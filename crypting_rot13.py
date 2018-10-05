# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:33:40 2018

@author: jeann
"""
print("import packages")
from nltk import RegexpTokenizer
toknizer = RegexpTokenizer(r'''\w'|\w+|[^\w\s]''')
from string import punctuation
import unidecode
print("Construction de la classe ")
class EncryptDecryptRotx:
    """
    Encrypt/decrypt a text by rotating the letter to the +x position in the alphabet
    """
    def __init__(self,rotation = None):
        
        self.rotation = rotation
        
    def char_encrypt(self,char):
        #Get the letter position from the ascii code, then rotate to the new wanted letter
        #%26=> If we move past 26 by adding our new rotation, keep the result between 1-26
        return chr((ord(char)-96 +self.rotation)%26+96)
        
    def encrypt(self, text):
        
        text = unidecode.unidecode(text.lower().strip())
        
        token = toknizer.tokenize(text)
        
        return " ".join(
                ["".join([self.char_encrypt(l) if l.isalpha() else l for l in word])
                        for word in token if word not in punctuation])
    
    
    
    
print("Lancement du programme...")

print("Si vous souhaitez décrypter un texte, entrez juste la valeur de rotation en négatif")
rotation = input("Veuillez entrer la valeur de rotation pour le cryptage:\n")
text = input("Veuillez entrer le texte à (dé)chiffrer: \n")
try:
    print(EncryptDecryptRotx(int(rotation)).encrypt(text))
except ValueError:
    print("ERREUR ! \n Entrez un nombre valide comme rotation svp")