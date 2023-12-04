#calculate the factorial of a number:

user = int(input("enter the number: "))
def factorial(user):
    if user == 0:
        return  1
    else:
        return user * factorial(user-1)


print(factorial(user))