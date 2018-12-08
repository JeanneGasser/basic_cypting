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
    
    def char_encrypt(self, char, rotation):
        #Get the letter position from the ascii code, then rotate to the new wanted letter
        #%26=> If we move past 26 by adding our new rotation, keep the result between 1-26
        #First calculate the new letter position: 
        new_letter_pos = (ord(char)-96 + rotation)%26
        #/!\Issue when new_letter_pos = 0 => should give 26 not 0
        #Workaround: 
        if new_letter_pos !=0:
            return chr(new_letter_pos + 96)
        else:
            return chr(26 + 96 )

        
    def cesar_encrypt(self, text,rotation):
        
        #Text Cleaning
        text = unidecode.unidecode(text.lower().strip())
        
        token = toknizer.tokenize(text)
        
        return " ".join(
                ["".join([self.char_encrypt(l,rotation) if l.isalpha() else l for l in word])
                        for word in token if word not in punctuation])
#User input and class output


print("Bienvenue, avec ce programme vous allez pouvoir chiffrer ou déchiffrer du texte. \n \
      Chiffrement : lettres = position numérique dans l'alphabet")

textfile = input("Veuillez entrer votre texte ou un nom de fichier texte (.txt) avec le chemin \n \n")
what_to_do = input("Voulez vous décrypter ou encrypter \n \n")
how_to_do = input("Utilisez le chiffrement numérique ou Cesar(rotation de lettres)? \n \n")

#IF GIVEN A TEXTFILE
if ".txt" in textfile:
    
    try: 
        txt = open(textfile,"r").read()
        
    
        if unidecode.unidecode(what_to_do.lower().strip())=="encrypter":
            
            
            if unidecode.unidecode(how_to_do.lower().strip())=="classique" or \
               unidecode.unidecode(how_to_do.lower().strip())== "numerique":
        
                open(textfile.split(".")[0] + "_crypted.txt","w").write(EncryptDecrypt().encrypt(txt))
                print("Fichier encrypté et enregistré")
                
            elif unidecode.unidecode(how_to_do.lower().strip())=="cesar" or \
                 unidecode.unidecode(how_to_do.lower().strip())== "rotation":

                rot = input("Veuillez entrer la valeur de rotation pour encrypter le texte: \n \n")
                open(textfile.split(".")[0] + "_crypted.txt","w").write(EncryptDecrypt().cesarcrypt(txt,int(rot)))
                print("Fichier encrypté et enregistré")
                
            else: 
                print("Merci d'entrer une méthode valide: Classique ou César")
                
    
        elif unidecode.unidecode(what_to_do.lower().strip())=="decrypter":
            
            if unidecode.unidecode(how_to_do.lower().strip())=="classique" or \
               unidecode.unidecode(how_to_do.lower().strip())== "numerique":
            
                open(textfile.split(".")[0] + "_decrypted.txt","w").write(EncryptDecrypt().decrypt(txt))
                print("Fichier decrypté et enregistré")
                
            elif unidecode.unidecode(how_to_do.lower().strip())=="cesar" or\
                 unidecode.unidecode(how_to_do.lower().strip())== "numerique":

                rot = input("Veuillez entrer la valeur de rotation pour décrypter le texte (valeur négative) \n \n")
                open(textfile.split(".")[0] + "_decrypted.txt","w").write(EncryptDecrypt().cesarcrypt(txt,int(rot)))
                print("Fichier decrypté et enregistré")
            
            else: 
                print("Merci d'entrer une méthode valide: Classique ou César ")
                    
        else: 
            print("Veuillez entrer une commande valide: Encrypter ou Decrypter")
        
    except:
        print ("Veuillez donner un fichier .txt valide, avec le chemin.")

#Classic Text
else:
        
    if what_to_do.lower().strip()=="encrypter":
                
        if unidecode.unidecode(how_to_do.lower().strip())=="classique" or\
           unidecode.unidecode(how_to_do.lower().strip())== "numerique":

            print(EncryptDecrypt().encrypt(textfile))
        
        elif unidecode.unidecode(how_to_do.lower().strip()) == "cesar" or\
             unidecode.unidecode(how_to_do.lower().strip())== "rotation":

            
            rot = input("Veuillez entrer la valeur de rotation pour encrypter le texte: \n \n")
            
            print(EncryptDecrypt().cesar_encrypt(textfile,int(rot)))
        else: 
            print("Merci d'entrer une méthode valide: Classique ou César ")
        
        
    elif unidecode.unidecode(what_to_do.lower().strip())=="decrypter":
        
        if unidecode.unidecode(how_to_do.lower().strip())=="classique" or\
           unidecode.unidecode(how_to_do.lower().strip())== "numerique":
            
            print(EncryptDecrypt().decrypt(textfile))
        
        elif unidecode.unidecode(how_to_do.lower().strip()) == "cesar" or\
             unidecode.unidecode(how_to_do.lower().strip())== "rotation":
            
            rot = input("Veuillez entrer la valeur de rotation pour décrypter le texte (valeur d'encryptage mais négative): \n \n")
            
            print(EncryptDecrypt().cesar_encrypt(textfile,int(rot)))
        else: 
            
            print("Merci d'entrer une méthode valide: Classique ou César ")
                    
    else: 
        print("Veuillez entrer une commande valide: Encrypter ou Decrypter")

        













































