"""
import random

print(random.randrange(1, 10))
"""
float_string ='5.67'
print(float_string)
print(type(float_string))

converted = float(float_string)
print(converted)
print(type(converted))

new_int = int(converted)
print(new_int)
print(type(new_int))
    


x = 3.6 + 3
print(round(x))
print(str(x))
# Type conversions or Type casting

# In Implicit type conversion, Python automatically converts one data type to another data type without any user's need.
# Explicit type conversion, also known as type casting, in Python refers to the process of manually converting a value from one data type to another using built-in functions like int(), float(), or str().
m = 8
n = 2
print(f"{m + n}")