#reverse the number

s = 34466
s1 = 0

while(s>0):
    s1 = (s1*10) + (s%10)
    s = s // 10

print(s1)
    

