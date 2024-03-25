Grade = float(input("what's your score: "))

if Grade >= 75 and Grade <= 100:
    print("Excellent, You got an A!")
elif Grade >= 60 and Grade <= 74:
    print("Awesome, You got a B!")
elif Grade >= 50 and Grade <= 59:
    print("Nice, You got a C!")
elif Grade >= 40 and Grade <= 49:
    print("Good, You got a D!")
elif Grade >= 35 and Grade <= 39:
    print("Poor, You got an E!")
elif Grade >= 0 and Grade <= 34:
    print("very poor, you got an F!")
else:
    print(f"Invalid score!\nInput a valid score is {Grade}")