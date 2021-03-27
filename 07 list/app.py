num = [1, 2, 3, 4, 5]

# new number add in the last of num

num.append(20)
print(num)

# new number add in the mid of num

num.insert(0, 10)
print(num)

# remove number form num
num.remove(10)
print(num)

# remove last number of the list
num.pop()
print(num)


# remove all number
num.clear()
print(num)


# --------------------

num = [1, 2, 3, 4, 5]


# find number possition in num
print(num.index(3))


# not present of number
print(50 in num)

# ---------------

num = [5, 1, 2, 3, 4, 5]


# count how much time one number present there
print(num.count(5))


# number sort seriyaly
num.sort()
print(num)

# number make  reverse
num.reverse()
print(num)

# ---------copy_number---------
num = [1, 2, 3, 4, 5]
num_2 = num.copy()
num.append(10)
print(num)
print(num_2)
