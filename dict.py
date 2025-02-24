myinfo={"name":"Suyog","age":14,"Address":"Lalitpur","hobbies":["coding","reading","playing"]}
print(myinfo)

myinfo["age"]=17
print("Updated age",myinfo)

myinfo["fav food"]="momo"
print("Updated food",myinfo)


print(myinfo.get("name"))

print(myinfo.clear())