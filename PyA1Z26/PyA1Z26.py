import re

def lifechanger(message):
    message = re.split(' ',message)
    return message


def encrypt(message):
    message = message.upper()
    Encrypted_Message = ""
    message = "".join(message.split())
    for i in range(0, len(message)):

        c = ord(message[i]) - 64
        Encrypted_Message += str(c) + " "
    return (Encrypted_Message)


def decrypt1(message):

    Decrypted_Message = ""
    message = lifechanger(message)
    for c in message:

        x = ""
        c = re.split('-',c)


        for i in c:
            c = chr(int(i) + 64)
            x += c

        Decrypted_Message = Decrypted_Message + " " + x
    return (Decrypted_Message)


def decrypt2(message):

    Decrypted_Message = ""
    message = message.split()

    for c in message:
        c = chr(int(c) + 64)
        Decrypted_Message += c
    return (Decrypted_Message)


print('<---Please select one of the options given below--->\nNOTE: Please remove the symbols like (:,#,@,%,any quotes), You can use "-" as it is very common for A1Z26')
Value = int(input('1 : Encryption\n2 : Decryption\n-->'))


if(Value == 1):
    Message = input("Please Enter Your MESSAGE (Plain Text) : ")
    print("Encrypted Message : ", encrypt(Message))


elif(Value == 2):

    print("Are you going to use symbols ('-' only) between numbers\n?")
    value = int(input('1 : YES\n2 : NO, NO SYMBOLS\n-->'))
    if value ==1:
        Message = input("Please Enter Your MESSAGE (Cipher Text) : ")
        print("Decrypted Message : ", decrypt1(Message))
    if value ==2:
        Message = input("Please Enter Your MESSAGE (Cipher Text) : ")
        print("Decrypted Message : ", decrypt2(Message))
else:
    print('Please Select the Valid Option')
