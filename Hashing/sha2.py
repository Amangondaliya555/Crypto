import hashlib
  
# initialize a string
str = "Crypto"
  
# encode the string
encoded_str = str.encode()
  
# create sha-2 hash objects initialized with the encoded string
hash_obj_sha224 = hashlib.sha224(encoded_str)   # SHA224
hash_obj_sha256 = hashlib.sha256(encoded_str)   # SHA256
hash_obj_sha384 = hashlib.sha384(encoded_str)   # SHA384
hash_obj_sha512 = hashlib.sha512(encoded_str)   # SHA512
   
# print
print("\nSHA224 Hash: ", hash_obj_sha224.hexdigest())
print("\nSHA256 Hash: ", hash_obj_sha256.hexdigest())
print("\nSHA384 Hash: ", hash_obj_sha384.hexdigest())
print("\nSHA512 Hash: ", hash_obj_sha512.hexdigest())
