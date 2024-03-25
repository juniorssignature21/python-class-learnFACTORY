name = input("Input your full name: ").title().strip()
vote_age = int(input("How old are you? "))

if vote_age >= 18:
    print(f"Congratulations!!! {name} \nYou are Eligible to vote")
if vote_age < 18:
    print(f"Dear {name} \nYou are not eligble to vote.")