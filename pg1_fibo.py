def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

# take input from the user
n_num = int(input("How many numbers? "))

# check if the number of terms is valid
if n_num <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence is:")
   for i in range(n_num):
       print(fibonacci(i))