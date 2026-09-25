

count =0 

while count < 3:
    print(count)
    count += 1

#-------

def ask_until_valid():
    while True:
        number = int(input("Enter a Number between 1 and 10:"))
        if number>=1 and number<=10:
            return "Valid Number"
        else:
            print("Invalid number, try again")

result = ask_until_valid()
print(result)

#====================
def ask_until_valid():
    while True:
        number = int(input("Enter a Number between 1 and 10:"))
        if number>=1 and number<=10:
            return number
        else:
            print("Invalid number, try again")

result = ask_until_valid()
print(result)


#=======
# Example -2

while True:
    password = input("Enter your Password: ")
    if  password == "python123":
        print("Access Granted")
        break
    else:
        print("Invalid Pass")
