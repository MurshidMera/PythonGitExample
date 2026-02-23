instance={
   "id": "i-12312123214",
    "state": "running",
    "public_ip": "53.12.12.34",
    "private_ip": "10.1.1.2",
    "vpc": {
        "cidr": "10.0.0.0/16",
        "nat": "yes",
        "pub_subnet": ["10.0.0.0/24", "10.0.1.0/24"]

    }

}
#Both ways to printing the values.
#print(instance["id"])
#print(instance.get("id"))
##############
instance["region"]="ap-south-1" # Adding the value to dictionary.
print(instance)
instance["state"]="stoped"
print(instance)

# printing the vlaue of  "pub_subnet": ["10.0.0.0/24", "10.0.1.0/24"]
print(instance.get("vpc").get("pub_subnet")[0])
#printing the value without get method of dictionary
print(instance["vpc"]["pub_subnet"][0])