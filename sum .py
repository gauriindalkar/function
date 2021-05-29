#######saral question debug the code question 1
# def sum(y):
#     x=12
#     print(x+y)
# sum(13)

######saral question debug the code question 2
# def welcome():
#     print("welcome to function")
# welcome()

######saral question debug the code question 3
# def isEven():
#     if (12%2==0):
#         print("even number")
#     else:
#         print("odd number")
# isEven()

######function argument question 1
# number_list=[1,2,3,4,5,6,7,10,-2]
# print(max(number_list))

######function argument question 2
# a=[1,2,3,4,5,6]
# print(len(a))

######function argument question 3
# def say_hello(name):
#     print("Hello",name)
#     print("aap kahase ho?")
# say_hello("aatif")

######multiple function argument question 1
# def add_numbers(number1,number2):
#     print("main do number ko add karunga")
#     print(number1+number2)
# add_numbers(120,50)
# num_x=134
# name="rinki"
# add_numbers(num_x,name)

######multiple function argument question 2
# def say_hello_people(name_x,name_y,name_z,name_a):
#     print("namaste",name_x)
#     print("alha hafis",name_y)
#     print("bonjour",name_z)
#     print("hello",name_a)
# say_hello_people("imitiyaz","rishabh","rahul","vidya")
# say_hello_people("steve","saswata","shakrundin","rajeev")

######python aredtery argument que 1
# def icecream(*flavours):
#     print("i love",*flavours)
# icecream("chocleate","vanella","strobary","betterscoch")

######default parameter value
# def attendence(name,status="absent"):
#     print(name,"is",status,"today")
# attendence("kartik","present")
# attendence("sonu")
# attendence("vishal","present")
# attendence("umesh")

#######debug code question 1
# def greet(name):
#         print("welcome",name)
# greet("rinki")
# greet("vishal")
# greet("kartik")
# greet("bijendra")

######debug code question 2
# def info(name,age):
#     print(name,"is",age,"years old")
# info("sonu",12)
# info("sana",17)
# info("umesh",18)

######debug code question 3
# def studentditeails(name,currentmilstone,mentorname):
#     print("hello",name,"your",currentmilstone,"concept","is clear with the help of",mentorname)
# studentditeails("gauri","loop","chhaya")

#######saral question 2
# def function_lines():
#     print("mera naam rishabh hai","main navgurukul ka co-founder hun")
# function_lines()

#######saral question 3 part 1)
# def student_naam(student_list):
#     print(student_list)
# student_naam("gauri")
# student_naam("saniya")
# student_naam("supriya")
# student_naam("mayuri")

######saral question 3 part 2)
# def graterthan20(a,b):
#     print(max(a,b))
# graterthan20(20,60)
 
######saral question 4 part 1
# def add_numbers(number1,number2):
#     print(number1+number2)
# add_numbers(int(input("enter number")),int(input("enter numbre")))

#######saral question 4 part 2
# def add_numbers_list(list1,list2):
#     i=0
#     while i<len(list1):
#         j=0
#         while j<len(list2):
#             if list1[i]<list2[j]:
#                 print([[list[i]]+[list2[j]]])
#             j+=1
#         i+=1
# add_numbers_list([1,2,3],[4,5,6])

######saral question 5 part 1
# def check_numbers(number):
#     if number%2==0:
#         print("even number")
#     else:
#         print("odd number")
# check_numbers(int(input("enter number")))

#######saral question 5 part 2
# def check_numbers(list1,list2):
#     i=0
#     while i<len(list1):
#         if list1[i]%2==0 and list2[i]%2==0:
#             print("even number")
#         else:
#             print("odd number")
#         i+=1
# check_numbers([2,6,18,10,3,75],[6,19,24,12,3,87])

#######return value from a function
# def menu(day):
#     if day=="monday":
#         food="better chicken"
#     elif day=="tuesday":
#         food="mutton chaop"
#     else:
#         food="chole bhature"
#     print("kya mein print ho paungi?:-(")
#     return food
#     print("lekin mein toh paka nahi print hoga:'(")
# print(menu("monday"))

#######saral question 6
# def calculator(number_x,number_y,opertion):
#     if opertion=="addition":
#         print(number_x+number_y)
#     elif opertion=="substract":
#         print(number_x-number_y)
#     elif opertion=="multiply":
#         print(number_x*number_y)
#     elif opertion=="divide":
#         print(number_x/number_y)
#     else:
#         print(number_x%number_y)
# num1=int(input("enter first number"))
# num2=int(input("enter secound number"))
# op=input("enter opertion")
# calculator(num1,num2,op)


#######simple return concept
# def add(a,b):
#     c=a+b
#     return c
# a=5
# b=6
# z=add(a,b)
# print(z)