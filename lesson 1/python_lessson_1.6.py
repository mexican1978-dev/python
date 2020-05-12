a = int(input("km in first day: "))
b = int(input("km in last day: "))
i = 0
while a < b:
    a = a + a * 0.1
    i += 1
print(f"You need {i + 1} days.")
