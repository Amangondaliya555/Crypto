def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(coprime, phi_n):
    g, x, y = egcd(coprime, phi_n)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % phi_n


encrypt():

decrypt():
  
  

print("Select the option from the below :\n")
print("1. Encryption\n")
print("2. Decryption\n")
x = input()

if x==1:
  encrypt()
elif x==2:
  decrypt()
else:
  print("Enter a valid number!")

