

numbers =[1,2,3,4,5]

for number in numbers:
    print(number)

#------

words =["n8n","python","claude code","codex"]

for i in words:
    print(f"I am learning {i}")
#_____________


def calculate(a,b,operation):
    if operation == "add":
        return a+b
    elif operation == "multiply":
        return a*b
    elif operation == "m":
        return a-b
    else:
        return "No operation"
    

calculation = [(2,4,"add"),(3,4,"multiply"),(4,4,"sub")]

for item in calculation:
    print(calculate(item))