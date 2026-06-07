def saveuser(name,age):
    with open("users.txt","w") as file:
        file.write(f"{name},{age}\n")
        
def showuser():
    with open("users.txt","r") as file:
        print(file.read())
        
name = input("Enter your name: ")
age = int(input("Enter your age "))

saveuser(name,age)
showuser()