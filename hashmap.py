# Try HashMap
n = int(input('Please enter an integer: ').strip())
check = {True: "Not Weird", False: "Weird"}
print(check[n%2==0 and (n in range(2,6) or n > 20)])