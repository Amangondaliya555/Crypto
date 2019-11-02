decrypted_msg = []

alphabet = "abcdefghijklmnopqrstuvwxyz"
tebahpla = "zyxwvutsrqponmlkjihgfedcba"



print('<---Please select one of the options given below--->\n')
Value = int(input('1 : Encryption\n2 : Decryption\n-->'))

if (Value == 1):
    message = input("Please Enter Your MESSAGE (Plain Text) : ")
    message = message.lower()
    word1 = message.translate({ord(x): y for (x, y) in zip(tebahpla, alphabet)})
    print("Encrypted Message : ", word1)



elif Value == 2:
    message = input("Please Enter Your MESSAGE (Cipher Text) : ")
    message = message.lower()
    word2 = message.translate({ord(x): y for (x, y) in zip(alphabet, tebahpla)})
    print("Decrypted Message : ", word2)

else:
    print('Please Select the valid Option')
