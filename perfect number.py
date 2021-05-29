# 7.Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
# [An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].
# def perfect(number):
#     sum=0
#     i=1
#     while i<number:
#         if number%i==0:
#             sum=sum+i
#             i=i+1
#     if sum==number:
#         print("it is perfect number")
#     else:
#         print("it is not perfect number")
# number=int(input("enter number"))
# perfect(number)