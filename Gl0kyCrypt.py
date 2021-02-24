#!/usr/bin/python3.9

from io import open
import os
from subprocess import PIPE, run
import time
import platform
import sys

def clearconsole():

    if platform.system() == "Linux":

        os.system("clear")

    if platform.system() == "Windows":

        os.system("cls")


def getpwd():

    if platform.system() == "Linux":

        return outcommand("pwd")

    if platform.system() == "Windows":

        return outcommand("echo %cd%")

def outcommand(command):

    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

def cesarenc(shift, text):
    
    encryption = "" 

    for c in text:
        
        if c.isupper(): 

            c_unicode = ord(c)
            c_index = ord(c) - ord("A")
            new_index = (c_index + shift) % 26 
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            encryption = encryption + new_character
            
        elif(ord(c) == 32):
            
            new_character = " "
            encryption = encryption + new_character
            
        elif c.islower():
            
            c_unicode = ord(c)
            c_index = ord(c) - ord("a")
            new_index = (c_index + shift) % 26
            new_unicode = new_index + ord("a")
            new_character = chr(new_unicode)
            encryption = encryption + new_character 
            
        elif(ord(c) > 47 and ord(c) < 58):
            
            tmp = int(c)
            new_character = (tmp + shift) % 9
            encryption = encryption + str(new_character)
            
    return encryption

def cesardec(shift, text):
    
    de_encryption = "" 

    for c in text:
        
        if c.isupper(): 

            c_unicode = ord(c)
            c_index = ord(c) - ord("A")
            new_index = (c_index - shift) % 26 
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            de_encryption = de_encryption + new_character
            
        elif(ord(c) == 32):
            
            new_character = " "
            de_encryption = de_encryption + new_character
            
        elif c.islower():
                
            c_unicode = ord(c)
            c_index = ord(c) - ord("a")
            new_index = (c_index - shift) % 26
            new_unicode = new_index + ord("a")
            new_character = chr(new_unicode)
            de_encryption = de_encryption + new_character 
            
        elif(ord(c) > 47 and ord(c) < 58):
            
            tmp = int(c)
            new_character = (tmp - shift) % 9
            de_encryption = de_encryption + str(new_character)
            
    return de_encryption

def readfile():
    
    url = input("Especifique el nombre o ruta del archivo: ")
    f = open(url, "r")
    txt = f.read()
    f.close()
    return txt

def writefile(txt):
    
    directory = getpwd()
    if os.path.isdir(directory.strip('\n')+"/output/"):
    
        print("")
        out = input("Especifique el nombre del archivo de salida: ")
        f = open("./output/"+out, "w")
        f.write(txt)
        f.close()
            
        print("")

        if platform.system() == "Linux":

            print("Archivo guardado en " + directory.strip('\n') + "/output/" + out)

        if platform.system() == "Windows":

            print("Archivo guardado en " + directory.strip('\n') + "\output" + chr(92) + out)
            
    else:
            
        os.mkdir(directory.strip('\n')+"/output/")
        writefile(txt)

def opt1():
    
    txt = readfile()
    passwd = input("Digite la clave de seguridad: ");

    for c in passwd:
        
        shift = int(c)
        txt = cesarenc(shift,txt)

    writefile(txt)
    print("")
    input("Presione cualquier tecla para continuar...")

def opt2():
    
    txt = readfile()
    passwd = input("Digite la clave de seguridad: ");
    
    for c in passwd:
        
        shift = int(c)
        txt = cesardec(shift,txt)
    
    writefile(txt)
    print("")
    input("Presione cualquier tecla para continuar...")

def opt3():
    
    txt = input("Digite el texto que desea cifrar: ");
    passwd = input("Digite la clave de seguridad: ");
    
    for c in passwd:
        
        shift = int(c)
        txt = cesarenc(shift,txt)
        
    print("")
    print("Su texto cifrado es: " + txt)
    print("")
    input("Presione cualquier tecla para continuar...")
    
def opt4():
    
    txt = input("Digite el texto que desea decifrar: ");
    passwd = input("Digite la clave de seguridad: ");
    
    for c in passwd:
        
        shift = int(c)
        txt = cesardec(shift,txt)
    
    print("")
    print("Su texto decifrado es: " + txt)
    print("")
    input("Presione cualquier tecla para continuar...")

def menu():
    
    clearconsole()
    print ("Gl0kyCrypt v1.1")
    print ("")
    print ("Cesar")
    print ("------------------------------------------")    
    print ("[1]: Encriptar un archivo.")
    print ("[2]: Desencriptar un archivo.")
    print ("[3]: Encriptar una cadena de texto.")
    print ("[4]: Desencriptar una cadena de texto.")
    print ("[5]: Salir.")
    print ("")
    str_opt = input ("Elija que opcion desea usar: ")
    
    try:
        
        opt = int(str_opt)
        
    except ValueError:
        
        clearconsole()
        print ("Introduzca numero decimal...")
        time.sleep(2)
        main()
         
    if (opt == 1):
        
        clearconsole()
        print ("Gl0kyCrypt v1.0")
        print ("")
        print ("Cesar -> [1]: Encriptar un archivo.")
        print ("------------------------------------------")    
        opt1()
        main()
        
    if (opt == 2):  
         
        clearconsole()
        print ("Gl0kyCrypt v1.0")
        print ("")
        print ("Cesar -> [2]: Desencriptar un archivo.")
        print ("------------------------------------------")  
        opt2()
        main()
    
    if (opt == 3): 
          
        clearconsole()
        print ("Gl0kyCrypt v1.0")
        print ("")
        print ("Cesar -> [3]: Encriptar una cadena de texto.")
        print ("------------------------------------------")
        opt3()
        main()
    
    if (opt == 4):
        
        clearconsole()
        print ("Gl0kyCrypt v1.0")
        print ("")
        print ("Cesar -> [4]: Desencriptar una cadena de texto.")
        print ("------------------------------------------")    
        opt4()
        main()

    if (opt == 5):
        
        clearconsole()
        print ("Gracias por usar...")
        time.sleep(2)
        sys.exit(1)
        return False;
    
    else:

        clearconsole()
        print("Opcion invalida...")
        time.sleep(2)
        return True;
              
def main():
    
    while(menu() == True):
        
        clearconsole()
        menu()
        
if __name__ == "__main__":
    main()



