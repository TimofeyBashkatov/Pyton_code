Guests = ["Ivan", "Aleksey", "Dmitriy"]
for i in Guests:
    print(f"Hello, {i}! I want to invite you to my dinner.")

Missing_Guest = Guests.pop(0)
print(Missing_Guest)

print("Wow! We can invite 3 more guests to our dinner!")

Guests.insert(0, "Aleksandr")
Guests.insert(0, "Egor")
Guests.insert(0, "Evgeniy")



for i in Guests:
    print(f"Hello, {i}! I want to invite you to my dinner.")

print("Oops! I can invite just 2 guests!")

a = len(Guests)
if a > 2:
    Missing_Guests = Guests.pop()
    for i in Guests:
        print(f"Sorry {i}! You can't come to dinner!")
    a - 1
    print(Missing_Guests)
elif a == 2:
    print("There only 2 guests.")

for i in Guests:
    print(f"Hello, {i}! You still can come to my dinner.")


print(Guests)




    




