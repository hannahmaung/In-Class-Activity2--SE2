def get_divisors(n):
  for i in range(n):
    x = len([i for i in range(1,n+1) if not n % i])
  return x
    
userinput = int(input("Enter a number: "))
print("The divisors are: ")
print(get_divisors(userinput3))