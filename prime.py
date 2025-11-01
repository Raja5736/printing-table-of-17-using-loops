#Write a Python program to take a number as input from the user and check whether it is a prime number or not.
num=int(input("Enter a number"))
prime=True
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("Not a prime number")
            prime=False       
            break
    if prime==True:
        print("Its a prime number")


        



