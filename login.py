pass1 = 234
pass2 = eval(input("enter the pass"))
n =2

while(n>0):
    if(pass2 != pass1):
        n = n-1
        pass2 = eval(input("enter pass again"))
    else:
        print("login successfull")
        break
print("login unsuccessfull")
