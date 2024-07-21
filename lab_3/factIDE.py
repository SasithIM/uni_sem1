import math
num = int(input("Enter number to find factorial :"))
fact=0
for i in range (1, num+1):
    fact = fact*i
print("Factorical of ", num, " is ", fact)
