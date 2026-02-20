#palindrome
s = 1001
s1 = 0

while(s>0):
    s1 = s1*10 + s%10
    s = s//10

if(s == s1):
    print ("palindrome")
else:
    print("not palindrome")

