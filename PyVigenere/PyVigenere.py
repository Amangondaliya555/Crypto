def Key_Generator(message, key):
    key = list(key)
    if len(message) == len(key):
        return (key)
    else:
        for i in range(len(message) -
                       len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))



def encrypt(message, key):
    Encrypted_Message = []
    for i in range(len(message)):
        m = (ord(message[i]) +
             ord(key[i])) % 26
        m += ord('A')
        Encrypted_Message.append(chr(m))
    return ("".join(Encrypted_Message))



def decrypt(cipher_text, key):
    Decrypted_Message = []
    for i in range(len(cipher_text)):
        m = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        m += ord('A')
        Decrypted_Message.append(chr(m))
    return ("".join(Decrypted_Message))



print('<---Please select one of the options given below--->\nNOTE: Do not forget to use capital letters only :)')
Value = int(input('1 : Encryption\n2 : Decryption\n-->'))


if(Value == 1):
    Message = input("Please Enter Your MESSAGE (Plain Text) : ")
    key = input('Please Enter the desired SHIFT KEY : ')
    key = Key_Generator(Message, key)
    print("Encrypted Message : ", encrypt(Message, key))


elif(Value == 2):
    Message = input("Please Enter Your MESSAGE (Cipher Text) : ")
    key = input('Please Enter the desired SHIFT KEY : ')
    key = Key_Generator(Message, key)
    print("Decrypted Message : ", decrypt(Message, key))

else:
    print('Please Select the Valid Option')


