def egcd(x, y):
    if x == 0:
        return (y, 0, 1)
    else:
        g, b, a = egcd(y % x, x)
        return (g, a - (y // x) * b, b)


def modinv(coprime, phi_n):
    g, a, b = egcd(coprime, phi_n)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return a % phi_n


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

