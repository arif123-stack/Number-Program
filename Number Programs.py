#Number program in python
# 1.Program to Check Disarium number
num=int(input("Enter any number"))
sum=0
j=1
temp=num
while(temp!=0):
    rem=temp%10
    sum=sum*10+rem
    temp=int(temp/10)
temp=sum
sum=0
while(temp!=0):
    rem=temp%10
    sum=sum+pow(rem,j)
    temp=int(temp/10)
    j=j+1
if sum==num:
    print("Number is Disarium")
else:
    print("Number is not Disarium")
#--------------------------------------------------------------------------------------------------------------------------    
# 2.Program to determine whether a given number is a happy number
num=int(input("Enter the number"))
temp=num
while sum!=1 and sum!=4:
    sum=0
    while temp!=0:
        rem=int(temp%10)
        sum=sum+rem*rem
        temp=temp/10
temp=sum
if(sum==1):
    print(num,"Is Happy number")
else:
    print(num,"Is not Happy number")
 #------------------------------------------------------------------------------------------------------------------------------------   
 # 3.Program to determine whether a given number is a Harshad number
num=int(input("Enter the number"))
temp=num
sum=0
while temp>0:
        rem=int(temp%10)
        sum=sum+rem
        temp=temp/10
if(n%sum==0):
    print(num+"is Harshad number")
else:
    print(num+"is Harshad number")






