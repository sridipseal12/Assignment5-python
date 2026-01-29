users = {
    1: {"name": "Alice", "age": 25, "city": "Delhi"},
    2: {"name": "Bob", "age": 30, "city": "Mumbai"},
    3: {"name": "Charlie", "age": 28, "city": "Chennai"}
}

inp = input("Enter the student's name : ")
print(users[2]["name"])
c=0
for i in users:
    if users[i]["name"].lower() == inp.lower():
        print(f"{users[i]["name"]}'s marks : {users[i]["age"]}")
        c=1
        break

if c == 0:
    print("Student not found.")