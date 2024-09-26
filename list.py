#list can store multiole data, data can be different types int str 
#list can store the duplicate data 
#list is an ordered data set -->aorting asending descending 

#create list and store the your friend name
friendlist = ["ivan", "anshu", "anjali", "wani"]

#print the list of friend name
#print(friendlist)

#add the age of your friends into list
#append will add the data into end of the list 
friendlist.append(36)
friendlist.append(26)
friendlist.append(36)
friendlist.append(5)
#print(friendlist)

#add the data into list using index no
friendlist.insert(0, "ayush")
friendlist.insert(3, "anushka")
print(friendlist[3])

#to delete the data from the list
friendlist.remove("ivan")
print(friendlist) 

#pop will delete the data using index
friendlist.pop(3)
print(friendlist)

friendlist.pop(0)
print(friendlist)    


#access the complete list
#for name in friendlist:
#    print(name)

#add the 5 fact city name in list
#add my favt city kasol in first index 0
#remove the last city in list 
#sorting the list data
#print the list data
city= ["dehradhun", "ghaziabad"," amritsar","kasol",]
city.insert(0,"nodia")
city.pop()
print(city)