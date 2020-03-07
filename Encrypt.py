from Functions import *
import sys
cmd=sys.argv[1:]
if "--help" in cmd:
    Introduction()
    sys.exit()
new_key=input("Do You wish to generate a new key(Y/N)\n")
if new_key.upper()=="Y":
    Generate_key()
encrypt_or=input("Do you wish to \nencrypt files press '1' or \ndecrypt files press '2'\n")
if encrypt_or=='1':
    Encrytp_any_file()
elif encrypt_or=='2':
    Decrypt_any_file()
else:
    sys.exit()

