num = 123444432
dig = eval(input("enter digit"))
count = 0

while(num>0):
    num1 = num%10
    if(num1 == dig):
        count = count+1
    num = num//10

print(count)
