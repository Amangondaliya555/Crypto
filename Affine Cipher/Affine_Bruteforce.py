import enchant

#gcd Computation
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



#decrypt function
def decrypt(Message, a, b): 
	return ''.join([ chr((( modinv(a, 26)*(ord(i) - ord('A') - b)) 
					% 26) + ord('A')) for i in Message ]) 




d = enchant.Dict("en_US")

print('<---Please select one of the options given below--->\n')
Value = int(input('1 : Want all the possible results\n2 : Only English words as a result\n-->')) 



	

		

if(Value == 1):
	Message = raw_input("Please Enter Your MESSAGE : ")
	Message = Message.upper()
	
	for a in [ 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23,25]:
		for b in range(0,25):	
	
			decrypt = decrypt(Message,a,b)	
			print("Decrypted Message : ", decrypt)
		


elif(Value == 2):
	Message = raw_input("Please Enter Your MESSAGE : ")
	Message = Message.upper()
	for a in [ 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23,25]:
		for b in range(0,25):	
	
			message = decrypt(Message,a,b)	
			if d.check(message):	
				print("Decrypted Message :" + message)
			else: pass

else:
    print('Please Select the Valid Option')
