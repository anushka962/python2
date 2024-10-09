#opps in python
#object oriented programming ->objects
#class-> it is a container which collection variable, function
#example ->anu class
#anu.fullname->"anusharma"
#anu.age->18
#anu.sleeping()
#anu.eating()
#anu.watching()
#class syntax
class classname:
    print("this is my class")

class anushka:
    age=18
    fullname="anushka sharma"                                                                                   
    email="anu@gamil.com"
    def pocketmoney(this, amount):
        print("my pocketmoney is",amount)
    def monthlysalary(this, daysalary):
        totalsalary= 31*daysalary
        print("your monthly salary is",totalsalary)

#create class object
#object.classname=classname()
anushka:anushka=anushka()
anushka.pocketmoney(15000)
anushka.monthlysalary(int(input("enter your one day salary ")))
print(anushka.fullname, anushka.age, anushka.email)