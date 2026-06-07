with open("data.txt","w") as file:
    file.write("Hello Devops\n")
    
#read file

with open("data.txt","r") as file:
    content = file.read()
    print(content)
    
with open("users.txt", "a") as file:
    file.write("Atharva\n")