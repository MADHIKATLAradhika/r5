num=int(input("Enter a number: "));
if(num==0):
    print("Number is zero")
elif(num%2==0):
    print("Number is even")
elif(num%5==0):
    print("Number is not divisible by 5")
elif(num%6==0):
    print("Number is not divisible by 6")
else:
    print("Number is odd")