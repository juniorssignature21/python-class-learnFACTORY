x = int(input("what's x? "))

print("x = ",x)
if x%2==0:
    if x%3==0:
        print("Divisible by 2 and 3")
    else:
        print("Divisible by 2 and not divisible by 3")
else:
    if x%3==0:
        print("Divisibke bt 3 not divisible by 2")
    else:
        print("not divisible by 3 not divisible by 2")