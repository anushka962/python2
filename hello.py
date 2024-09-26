#wap to write your name
print("anushka")
#to comment the multiple lines
#bkdgdfkg
#sgsfg
#kkflenjk

#to comment the multiple lines of string
"""hi
my name is anushka 
email is anushka.96254@gmail.com
mobile 94343423"""

#create a variable to store my salary
salary =10000000
email ="anushka.9534@gmail.com"
name ="anushka sharma"
print(salary)
#print(name +" "+email+salary )#will not run coz salary is not a string integer
#print(name+" "+email+salary)#will use comma to print diff datatypes together

#print(f"my name is{name} and email is{email}and salary is{salary}")# is field required to write when using diff variable

collegename =input("enter your college name")
print(collegename)

fname =input("enter your first name =")
lname=input("enter your last name= ")
print(fname+" "+lname)


#SECOND CLASS
name ="anushka sharma"
age =18
gender="female"
# print("my name is"+ name+"my age is",age," my gender is",+gender)
# by using comma

salary =1000000
smail ="anushka983@gmail.com"
name ="anushka sharma"

print(f"name is {name} and  age is {age} and email is{email} and salary is{salary} gender is{gender}")
# f is dield required tov write when using diff variable of diff data type


ageinstring = str(age)
print("my name is "+name+ "my age is"+ageinstring+"gender is"+gender)


#datatype in python
print(type(name))# type function return datatype of variable
print(type(age))
#1.str  it can store the string data e.g name="anushka sharma"
#2.int  it can store the numeric data e.g age =33
#3.float  it can store the decimal no e.g percentage =70.34


#typecasting in python = conver pne data type to another data type
#e.g= sometime when we purchase item in float we paid in integer
purchaseitemprice = 90.99
paiditemprice = int(purchaseitemprice)
print("paid amount is", paiditemprice)


#to get input from user using input() fuction
collegename = input("enter your college name")
collegefee = input("enter yoour college feee")
print("my college name is  "+ collegename+ collegefee)
#note:- the input function has default return data type str


#CONDSTATEMENT
#condition statement will check cond is true or not
#to check the condition we use if else
#WAP to check user eligible for voting
userage= input("enter your age")
#note the default input function return type is string
#for vote userage must be greater than 18
if userage>18:
    print("you are eligible for cvoting")
else:
    print("you are not eligible for voting")


    










