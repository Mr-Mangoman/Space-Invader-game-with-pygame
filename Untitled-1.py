x = int(input('Enter your English Marks '))
y = int(input('Enter your Maths Marks '))
z = int(input('Enter your Science Marks '))
a = int(input('Enter your SsT Marks '))
b = int(input('Enter your Computer Science Marks '))

Total = x+y+z+a+b

Percentage = (Total/500)*100

print("The total is " , Total)
print("the percentage is " , Percentage , "%" )

if Percentage >= 90:
     print('You ARe a Topper') 
else : 
    print("You are second")