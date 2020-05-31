
print("Hello, world!")


a_list = []
a_list = [1, 2, 3, "aaa", [1, 2, 3]]
print(a_list[4][1])

people = [{'name': 'bob', 'age': 20}, {'name': 'carry', 'age': 38}]
print(people[0]["name"])

person = {'name': 'Yonnie', 'age': 27}
people.append(person)
print(people)


def sumsum(num1, num2):
    return num1+num2


c = sumsum(1, 5)
print(c)

a = 3
if a % 2 == 1:
    print("a is odd")
else:
    print("a is even")


x = 120

if x < 100:
    print(1)
elif x < 200:
    print(2)
else:
    print(3)


a_list = [2, 3, 4, 1, 6, 3]
for a in a_list:
    print(a)

fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']
count_apple = 0
for fruit in fruits:
    if fruit == '사과':
        count_apple = count_apple + 1
print(count_apple)


def count_fruit(fruit_list, fruit_x):
    count = 0
    for fruit in fruit_list:
        if fruit == fruit_x:
            count = count+1
    return count


print(count_fruit([1, 3, 4, 2, 5, 1, 2, 3], 5))

fruits = ['수박', '수박', '멜론', '귤', '감', '수박']
print(count_fruit(fruits, "수박"))
