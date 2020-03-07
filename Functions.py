from cryptography.fernet import Fernet
import csv
import sys
import time
import os
filename="keys.csv"
reading=open(filename,"r")
key=reading.read()
f=Fernet(key)
def Encrytp_any_file():
#Asking for the path to the folder from user
    path_to_folder=input("Please Type the path to the folder\n")
#to check if the path entered is true    
    if (os.path.isdir(path_to_folder)):
        return True
    else:
        print("The path does not exits please try again")
        return False
    extension=input("Please type the file extension \nExample:.exe\n")
#searches for the files enxtension in the folder and the subfolder
    for folderName,subfolders,filenames in os.walk(path_to_folder):
        for filename in filenames:
            if filename.endswith(extension):
                path=folderName+"/"+filename
                try:
                    with open(path,"rb") as file:
                        file_data=file.read()
                        encrypt_data=f.encrypt(file_data)
                    with open(path,"wb") as file:
                        file.write(encrypt_data)
                    print("Encrypting "+filename)
                    time.sleep(5)
                    print("Done!")
#Some files can be read only so we can not write data onto them so it so handle that exception error
                except OSError:
                    print("This"+filename+" could not decrypted due to being read only")
    return
def Decrypt_any_file():
    path_to_folder=input("Please Type the path to the folder\n")
    if (os.path.isdir(path_to_folder)):
        return True
    else:
        print("The path does not exits please try again")
        return False
    extension=input("Please type the file extension that you want to decrypt \nExample:.exe\n")
    for folderName,subfolders,filenames in os.walk(path_to_folder):
        for filename in filenames:
            if filename.endswith(extension):
                path=folderName+"/"+filename
                try:
                    with open(path,"rb") as file:
                        file_data=file.read()
                        decrypt_data=f.decrypt(file_data)
                    with open(path,"wb") as file:
                        file.write(decrypt_data)
                    print("Decrypting "+filename)
                    time.sleep(5)
                    print("Done!")
                except OSError:
                    print("This"+filename+" could not decrypted due to being read only")
    return
def Introduction():
    statement1="This program encryptes files."
    statement2="1. This program Encryptes and Decryptes files with the extension of your choice in the folder of your choice"
    statement3="2.Decrypt the files with the same key you used to encrypt the file"
    print(statement1+"\n"+statement2+"\n"+statement3)
    return
def Generate_key():
    print("Generating Key")
    time.sleep(5)
#To generate the encryption key
    first_key=Fernet.generate_key()
    with open('keys.csv', 'w+') as file:
       writer=csv.writer(file)
       writer.writerow([first_key.decode('utf-8')])
    print("key generated")
    return
