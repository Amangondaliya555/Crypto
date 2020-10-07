def is_coprime_phi(phi, coprime_to_check):
    while phi % coprime_to_check == 0:
        coprime_to_check = input("Enter a prime number, to check if coprime with phi")
        e = coprime_to_check
    return True


if not is_coprime_phi(phi,e):
    raise ValueError("e is not coprime with phi_n")


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


  
p=
q=
e=

n=p*q
phi=(p-1)*(q-1)  


x = input("Select the option from the below :\n 1. Encryption\n 2. Decryption\n")

if x==1:
  encrypt()
elif x==2:
  decrypt()
else:
  print("Enter a valid number!")

