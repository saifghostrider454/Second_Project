# List Comprehensions

lst = [x for x in range(1, 16)]
print(lst)

lst = [1, 2, 3, 4, 5]
new = []
for i in lst:
    new.append(i * i)
print(new)

# syntax
# [operation for x in something condition]
# Like=> [x**3 for x in lst if x % 2 == 0]

lst1 = [x ** 2 for x in lst]
print(lst1)

lst2 = [x ** 3 for x in lst if x % 2 == 0]

print(lst2)

lst3 = [x ** 2 for x in lst if x % 2 != 0]

lst4 = [x ** 3 if x % 2 == 0 else x ** 2 for x in lst]
print(lst4)

for i in range(1, 6):
    for j in range(1, 6):
        if i % 2 == 0 and j % 2 != 0:
            print((i, j))

l1 = [(i, j) for i in range(1, 6) if i % 2 == 0 for j in range(1, 6) if j % 2 != 0]

print(l1)

grades = [78, 85, 60, 59, 36, 91]
grade = ['A' if i >= 90 else 'B' if i >= 80 else 'C' if i >= 70 else 'D' if i >= 60 else 'D' for i in grades]
print(grade)

grade_set = {'A' if i >= 90 else 'B' if i >= 80 else 'C' if i >= 70 else 'D' if i >= 60 else 'D' for i in grades}
print(grade_set)

grade_tuple = tuple('A' if i >= 90 else 'B' if i >= 80 else 'C' if i >= 70 else 'D' if i >= 60 else 'D' for i in grades)
print(grade_tuple)

dic_books = {'Titanic': 15, 'Jurasic Park': 5, 'Silent': 11, 'Corner': 6}

books_dict = {i: j for i, j in dic_books.items() if dic_books[i] >= 10}
print(books_dict)

grades = {'Alice': 80, 'Bob': 55, 'Charlie': 75, 'Dave': 90}

names = [key for key, value in grades.items() if value >= 70]
print(names)

# Lambda Function

# lambda Arguments: Expression

a = lambda x, y: x + y

b = lambda x, y, z: x + y - z

divide = lambda x, y: 'undefined' if y == 0 else x / y

# Filter

# filter(function, iterable)

numbers1 = [x for x in range(1, 11)]

print(list(filter(lambda x: x % 2 != 0, numbers1)))


# Map Function

# map(function, iterable)

def reverse(x):
    return x[::-1]


squares = map(lambda x: x ** 3, numbers1)

print(list(squares))

python_words = ['asif', 'saif', 'kaif']
print(list(map(reverse, python_words)))
print(list(map(lambda x: x[::-1], python_words)))





x = [i**+1 for i in range(3)]
print(x)