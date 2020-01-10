import random
#generates a password based on length and complexity input



# all letters
alpha = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h',
         'H','i','I','j','J','k','K','l','L','m','M','n','N','o','O',
         'p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w',
         'W','x','X','y','Y','z','Z']

# all numbers
numeric = ['0','1','2','3','4','5','6','7','8','9']

# all special characters
special = ['!','#','$','%','&','(',')','*','+','-','.',':',';','<','=',
           '>','?','@','[','^','_','{','|','}','~']
def password():
 # blank password
 password = ""
 # enter length of password
 passlength = input("Length of Password: ")
 for i in range(0,int(passlength)):
     r = random.randint(1,3)
     # alpha
     if r == 1:
         r2 = random.randint(0,len(alpha)-1)
         password += alpha[r2]      
     # numeric    
     elif r == 2:
         r2 = random.randint(0,len(numeric)-1)
         password += numeric[r2]
     # special    
     elif r == 3:
         r2 = random.randint(0,len(special)-1)
         password += special[r2]
 print(password)
