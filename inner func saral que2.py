#######saral question 2
#  def perfect(number):
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

########saral question 3
# def function_1(num1,num2,num3):
#     sum=num1+num2+num3
#     print(sum)
#     def function_2(sum):
#         avg=sum*3%100
#         print(avg)
#     function_2(sum)
# num_1=int(input("enter number1"))
# num_2=int(input("enter number2"))
# num_3=int(input("enter number3"))
# function_1(num_1,num_2,num_3)

######saral question 4
# def showNumber(limit):
#     i=0
#     while i<=limit:
#         if i%2==0:
#             print(i,"even number")
#         else:
#             print(i,"odd number")
#         i+=1
# showNumber(100)

#######saral question 5
# def showNumber(limit_1):
#     i=1
#     while i<=limit_1:
#         if i%3==0:
#             print(i)
#         if i%5==0:
#             print(i)
#         i+=1
# showNumber(10)

#######saral question 6
# def speed(speed_naam):
#     i=0
#     count=0
#     point=5
#     if speed_naam<=70:
#         print("ok")
#     elif 70<speed_naam:
#         sub=speed_naam-70
#         points=sub/5
#         print(points)
#         if points>12:
#             print("lincense suspended")
# speed_naam=int(input("enter a number"))
# speed(speed_naam) 

#######saral question 7
# def min(x,y):
#     a=len(x)
#     b=len(y)
#     if a>b:
#         print(x,a)
#     elif b>a:
#         print(y,b)
#     elif a==b:
#         print(x,a)
#         print(y,b)
# x=input("enter name")
# y=input("enter name")
# min(x,y)

#######saral question 8
# def square(number):
#     i=1
#     while i<=number:
#         a=i*i
#         print(i,":",a)
#         i+=1
# number=int(input("enter number"))
# square(number)

#######code output saral question 1
# def employee(name,salary=20000):
#         print(name,"your salary is:-",salary)
# employee("kartik",30000)
# employee("deepak")

######code output saral question 3
# def greet(*names):
#     for name in names:
#                print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")

######code output saral question 4
# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10
#     return sum
# number=int(input("enter number"))
# print(sumofdigits(number))

######debugs code saral question 1
# def calculate_sum(a,b):
#     sum = a+b
#     print(sum)
# calculate_sum(4,5)

#######debugs code saral quetion 2 
# def function_multi(a,b):
#     multi=a*b
#     return multi
# print(4,5)
# function_multi(6,7)
 
######debugs code saral question 3
# def avg(number1,number2,number3):
#     avg=number1+number2+number3/3
#     print(avg)
# avg(4,6,8)
 
######debugs code saral question 4
# def voter(age):
#     if age>18:
#         print("eligible")
#     else:
#         print("not eligible")
# age=int(input("enter age"))
# voter(age)
 
######debugs code saral question 5
# def distance(kms):
#     if kms<=20:
#         print("close")
#     elif kms<=50:
#         print("median")
#     else:
#         print("far")
# kms=int(input("enter kms"))
# distance(kms) 





