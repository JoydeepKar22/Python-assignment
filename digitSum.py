#3rd question
num = 1234


while(num >= 10 ):
    sum = 0
    while num>0:
        sum += num%10
        num= num//10
    num = sum
print(num)
    
