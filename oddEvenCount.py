#4th  question

s = 12345
oddcount = 0
evencount = 0
i =0

while(s>0):
    s1 = s%10
    if(s1 %2 == 0):
        evencount = evencount +1
    else:
        oddcount = oddcount+1

    s = s//10


print(evencount,oddcount)

        