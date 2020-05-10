
import enchant

'''
def zipping(message, alphabet, tebahpla):
    word = "".join(message.translate({ord(x): y for (x, y) in zip(alphabet, tebahpla)}))	
    return word
'''


a = "abcdefghijklmnopqrstuvwxyz"


b = ['zyxwvutsrqponmlkjihgfedcba', 'yxwvutsrqponmlkjihgfedcbaz', 'wvutsrqponmlkjihgfedcbazyx', 'tsrqponmlkjihgfedcbazyxwvu', 'ponmlkjihgfedcbazyxwvutsrq', 'kjihgfedcbazyxwvutsrqponml', 'edcbazyxwvutsrqponmlkjihgf', 'xwvutsrqponmlkjihgfedcbazy', 'ponmlkjihgfedcbazyxwvutsrq', 'gfedcbazyxwvutsrqponmlkjih', 'wvutsrqponmlkjihgfedcbazyx', 'lkjihgfedcbazyxwvutsrqponm', 'zyxwvutsrqponmlkjihgfedcba', 'mlkjihgfedcbazyxwvutsrqpon', 'yxwvutsrqponmlkjihgfedcbaz', 'jihgfedcbazyxwvutsrqponmlk', 'tsrqponmlkjihgfedcbazyxwvu', 'cbazyxwvutsrqponmlkjihgfed', 'kjihgfedcbazyxwvutsrqponml', 'rqponmlkjihgfedcbazyxwvuts', 'xwvutsrqponmlkjihgfedcbazy', 'cbazyxwvutsrqponmlkjihgfed', 'gfedcbazyxwvutsrqponmlkjih', 'jihgfedcbazyxwvutsrqponmlk', 'lkjihgfedcbazyxwvutsrqponm']


d = enchant.Dict("en_US")





print('<---Please select one of the options given below--->\n')
Value = int(input('1 : Want all the possible results\n2 : Only English words as a result\n-->'))

if (Value == 1):
    message = input("Please Enter Your MESSAGE (Cipher Text) : ")
    message = message.lower()
    for z in b:
        k = message.translate({ord(x): y for (x, y) in zip(a, z)})
        print("Encrypted Message :" + k)



elif Value == 2:
    message = input("Please Enter Your MESSAGE (Cipher Text) : ")
    message = message.lower()
    for z in b:
        k = message.translate({ord(x): y for (x, y) in zip(a, z)})
        if d.check(k):	
            print("Decrypted Message :" + k)
        else: pass
    		

else:
    print('Please Select the valid Option')
    
    
    
    
    
    
    
    
