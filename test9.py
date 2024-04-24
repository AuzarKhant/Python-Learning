user = "ak"
pwd = "12345678"

username = input("Enter your username : ")
password = input("Enter your password : ")

if username == user and password == pwd:
    print("Hello " , username)
elif username == user and password != pwd:
    print("Wrong password!")
elif username != user or password != pwd:
    print("Wrong password or username!")
else:
    print("Error, please restart program!")