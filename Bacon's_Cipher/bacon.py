table = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb','E':'aabaa',
    'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
    'K':'abaab', 'L':'ababa', 'M':'ababb', 'N':'abbaa', 'O':'abbab',
    'P':'abbba', 'Q':'abbbb', 'R':'baaaa', 'S':'baaab', 'T':'baaba',
    'U':'babaa', 'V':'babab', 'W':'babaa', 'X':'babab', 'Y':'babba', 
    'Z':'babbb'}
    
    
def encrypt(message):
    cipher = ''
    for letter in message:
        if(letter != ' '):
            cipher += table[letter]
        else:
            cipher += ' '

    return cipher


def decrypt(message):
    decode = ''
    i = 0
    
    while True :
        
        if(i < len(message)-4):
            
            s_s = message[i:i+5]
         
            if(s_s[0] != ' '):
                decode += list(table.keys())[list(table.values()).index(s_s)]
                i += 5 
            else:
                decode += ' '
                i += 1 
        else:
            break 

    return decode
    
    
print('<---Please select one of the options given below--->\n')
Value = int(input('1 : Encryption\n2 : Decryption\n-->'))

if (Value == 1):
    message = input("Please Enter Your MESSAGE (Plain Text) : ")
    message = message.upper()
    word1 = encrypt(message)
    print("Encrypted Message : ", word1)



elif Value == 2:
    message = input("Please Enter Your MESSAGE (Cipher Text) : ")
    message = message.lower()
    word2 = decrypt(message)
    print("Decrypted Message : ", word2)

else:
    print('Please Select the valid Option')
