
# if we usage this 2 line code and give any alfabet then we get 'ValueError'
"""
age = int(input('Age: '))

print(age)
"""
try:
    age = int(input('Age :'))
    income = 20000
    risk = income / age
    print(f"you are {age}")
except ZeroDivisionError:
    print("Age can't be 0")
except ValueError:
    print('Invalid value')
