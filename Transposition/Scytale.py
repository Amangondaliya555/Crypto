import math

def scytale_encrypt(plaintext, key):
	chars = [c.upper() for c in plaintext if c not in (' ',',','.','?','!',':',';',"'")]
	chunks = math.ceil(len(chars) / float(key))
	inters, i, j = [], 1, 1

	while i <= chunks:
		inters.append(tuple(chars[j - 1:(j + key) - 1]))
		i += 1
		j += key

	cipher, k = [], 0
	while k < key:
		l = 0
		while l < chunks:
			if k >= len(inters[l]):
				cipher.append('.')
			else:
				cipher.append(inters[l][k])
			l += 1
		k += 1

	return ''.join(cipher)


def scytale_decrypt(ciphertext, key):
	chars = [c for c in ciphertext]
	chunks = int(math.ceil(len(chars) / float(key)))
	inters, i, j = [], 1, 1

	while i <= key:
		inters.append(tuple(chars[j - 1:(j + chunks) -1]))
		i += 1
		j += chunks

	plain, k = [], 0
	while k < chunks:
		l = 0
		while l < len(inters):
			plain.append(inters[l][k])
			l += 1
		k += 1

	return ''.join(plain)

			
plaintext = "Amangondaliya555"
band = 2
ciphertext = scytale_encrypt(plaintext, band)
print("Cipher Text: ",ciphertext)

ciphertext = "AAGNAIA5MNODLY55"
band = 2
plaintext = scytale_decrypt(ciphertext, band)
print("Plain Text: ",plaintext)

