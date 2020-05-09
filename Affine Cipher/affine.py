#gcd computation
def egcd(a, b): 
    x,y, u,v = 0,1, 1,0
    while a != 0: 
        q, r = b//a, b%a 
        m, n = x-u*q, y-v*q 
        b,a, x,y, u,v = a,r, u,v, m,n 
    gcd = b 
    return gcd, x, y 



#mod inverse  
def modinv(a, m): 
    gcd, x, y = egcd(a, m) 
    if gcd != 1: 
        return None   
    else: 
        return x % m 


#encryption
def encrypt(message, a, b):
    return ''.join([ chr((( a*(ord(i) - ord('A')) + b ) % 26)  
                  + ord('A')) for i in message.replace(' ', '') ]) 




#decryption
def decrypt(message, a, b):
    return ''.join([ chr((( modinv(a, 26)*(ord(j) - ord('A') - b))  
                    % 26) + ord('A')) for j in message ]) 




#driver program
print('<---Please select one of the options given below--->\n')
Value = int(input('1 : Encryption\n2 : Decryption\n-->'))

if(Value == 1):
    Message = str(input("Please Enter Your MESSAGE (Plain Text) : "))
    Message = Message.upper()
    a = int(input("Enter key value (a) : "))
    b = int(input("Enter key value (b) : "))
    print("Encrypted Message : ", encrypt(Message, a, b))


elif(Value == 2):
    Message = str(input("Please Enter Your MESSAGE (Cipher Text) : "))
    Message = Message.upper()
    a = int(input("Enter key value (a) : "))
    b = int(input("Enter key value (b) : "))
    print("Decrypted Message : ", decrypt(Message, a, b))

else:
    print('Please Select the Valid Option')
