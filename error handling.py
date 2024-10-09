#error
#print(x)
#error handling
#try:
 #   print(x)
#except nameerror:
 #   print("'x' is not defined")

#error 2
#y=1/0
#try:
 #   y=1/0
#except ZeroDivisionError:
#    print("divide by zero error")

#error 3
name="anushka"
#no=int(name)
#try:
 #   no=int(name)
#except ValueError:
#    print("string cannot convert into ineger")

#error 4
#friends = ["ivan","anshu","wani"]
#friends[4]
#try:
#    friends[4]
#except IndexError:
#    print("your are calling wrong index")

#error 5
amount = 500
email ="a@gmail.com"
#total=amount+email
try:
    total =amount+email
except TypeError:
    print("this error is data type error")

#error 6 