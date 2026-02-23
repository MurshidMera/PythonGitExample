# servers = ["Web-1","web-2","api-1","db-1"]
# print(servers[0])#Printing by index position 
# print(servers[-1]+servers[3]) #Printing last one by negative number.
# print(servers[1:3]) #Slicing to print by start position to end position. 1:3

servers = ["Web-1","web-2","api-1","db-1","dev","stage","prod"]
servers.append("db-7") # Append always at End.
print(servers)
#servers.insert(2,"Web-3") # Insert add at index.
#print(servers)
#servers.extend(["Mong-1","Mongo-3"]) #extend use for multiple values to add.
#print(servers)

#Remove the value from List
servers.remove("db-1")
#print("After Removing the value ",servers)
#Counts
#print(servers.count("web-2"))

#Sort
servers.sort()
#print(servers)

listservers = ["Web-1","web-2","api-1","db-1","db-1","dev","stage","prod",True,["India","Pakistan"]]
#listservers.sort()      # Not work
#listservers.reverse()
#print(listservers)
#print(listservers[8]) #fetching data using Index.
indices=[i for i, v in enumerate(listservers) if v=="db-1"]
print(indices) # Doubt, how two values is stroe in indices, while its not declared as array
#print(listservers.index("db-1")) #it print first occurence of index position of string.

