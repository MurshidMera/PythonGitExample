print("hi python");
pods=["web-1","Web-2","api-1","db-1"]#List example to deploy
#tuple use , when data is not going to change, e.g connection string , url.
#Set => when we want to see the existing or not. e.g ip whitelisting or blocklisting. ip is lso not duplicate.
#print(pods[-2])#Negative indexing allow
print(pods[1:3])
pods.append("api-2")# always add at the end.
pods.insert(2,"db-2")#Add at index.
pods.extend(["db-3","web-3","api-3"])# add multiple
print(pods)

#Remove value
pods.remove("db-1")
print("After removing",pods)
#print(pods.count)
pods.sort()