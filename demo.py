import numpy as np

#create numpy array to store
#friends name, edit

myfriends = np.array(["anushka         ","anshu  ","wani  ","anjali  "])
print(myfriends)
#print(type(myfriends))
#print(myfriends[2])
#for i in range(0,4):
#    print(myfriends[i])

for name in myfriends:
    print(name)

myfriends[0] = "anushka sharma"
print(myfriends)
print(myfriends[0]) 
myfriends.sort()
print(myfriends)
mydata = np.flip(myfriends)
print(mydata)