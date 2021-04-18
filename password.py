import random

password = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

userinput = int(input("Enter how long you want your password to be: "))
length =  "".join(random.sample(password,userinput))
print(length)45