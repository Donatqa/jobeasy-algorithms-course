# Rewrite code, which will return only needed element of Fib sequence

# n = input('Enter the numbers: ')
#
#
# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return (fibo(n - 1) + fibo(n - 2))
#
#
# for i in range(int(n)):
#     print(fibo(i))


#Use datetime library to solve problem Seconds to Date


# def sec_to_date(seconds):
#     days = seconds // 86400
#     seconds = seconds - days * 86400
#     hours = seconds // 3600
#     seconds = seconds - hours * 3600
#     minutes = seconds // 60
#     seconds = seconds - minutes * 60
#     return f'{days}:{hours}:{minutes}:{seconds}'
# print(sec_to_date(9876543))




#Zeros not for Heros

# a = int(input("Enter a random numbers: "))
# b = 0
# while b == 0:
#     b = a % 10
#     if b == 0:
#         a = a // 10
#
# print(a)


#Digital root is the recursive sum of all the digits in a number.


# n = int(input('Enter the number: '))
# sum = 0
# while n // 10 > 0:
#     while n != 0:
#         sum = sum + n % 10
#         n = n // 10
#     n = sum
#     sum = 0
# print(n)

