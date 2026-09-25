name = "Ashish"        # str — text, always in quotes
age = 29               # int — whole number
height = 5.9           # float — decimal number
is_active = True       # bool — True or False only
nothing = None         # NoneType — absence of value
videos = [1, 2, 3]    # list — collection of items


print(type("Ashish"))
print(type(None))

print("29"+"1")
print("29"+1)
print(29.01+1)
print("Ashish"+"Pratap")


# writting the function to describing the value

def describe_value(value):
    return{
        "type": type(value).__name__,
        "value": value
    }

print(describe_value("Ashish"))
print(describe_value(23))
print(describe_value(23.8))
print(describe_value(True))
print(describe_value(None))

#====================

def describe_value_2(value):
    return{
        "type": type(value).__name__,
        "value": value,
        "can_do_maths": type(value).__name__ =="int" or type(value).__name__ =="float"
    }

print(describe_value_2("Ashish"))
print(describe_value_2(5))
print(describe_value_2(5.9))
print(describe_value_2(True))
#=========

int("38")
str(32)
float("43")
bool(0)
bool(3)