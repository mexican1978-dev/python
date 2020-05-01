profit = int(input("Enter your profit: "))
cost = int(input("Enter your cost: "))
income = profit - cost
if income > 0:
    print('profit')
    rent = income / profit
    print('rent =', rent)
    staff = int(input("Enter staff: "))
    earn = income / staff
    print('earn =', earn)
elif income < 0:
    print('lost')
else:
    print('equal')
