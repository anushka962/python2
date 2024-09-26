#for loop is used to no of iteration

username = "anu shamra"
for  i in username:
    print(i)

#print 1 to 10 using for loop
# for(int i=1;i<11;i++)
for x in range(1,11):
    print(x)

#WAP to create table of any no.
tableno =int(input("enter  the no"))
for a in range(1,11):
    print(tableno*a)

# even no.
for x in range (1,21):
    if x%2==0:
        print(x)

#WAP print this pattern 1  4 7 10 13 using for loop
for y in range(1,14,3):
    print(y)

#WAP print this pattern 1 3 7 11 13 15 using for loop
for b in range(1,16,3):
    if b==9 or b==5:
        continue
    else:
        print(b)
    

