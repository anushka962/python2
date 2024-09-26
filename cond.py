#CONDSTATEMENT
#condition statement will check cond is true or not
#to check the condition we use if else
#WAP to check user eligible for voting
userage = int(input("enter your age"))
#note the default input function return type is string
#for vote userage must be greater than 18
if userage > 18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")

#to check user can sit in thr first compartment in nature
usergender = input("enter your gender")
#to check user is male or female
if usergender =="male":
    print("you can't sit in first compartment")
elif usergender =="female":
    print("you can sit in the first compartment")
else:
    print("you can sit any compartment")

#WAP if gender is female and age greater then 18 --> govt job apply
#else male age greater than 18 --> private job apply 
usergender =input("enter your gender= ")
userage =int(input("enter your age"))
if usergender =="female" and userage>=18:
    print("you are eligible for govt job")
elif usergender=="male" and userage<=18:
    print("you are eligible for private job")
else:
    print("not elligible")






    





