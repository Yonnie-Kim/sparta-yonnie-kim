print("let's practice Python")

# 주석이 한 줄 일때는 이렇게!
'''
주석 여러줄 넣을 땐 따옴표 3개
'''

a = 3
b = a
a = a+1
num1 = a*b
num2 = 99


a_list = []
a_list.append(1)
a_list.append([2, 3])
print(a_list)
print(a_list[1])
print(a_list[1][1])

a_dict = {'name': 'bob', 'age': 20}
print(a_dict['name'])
a_dict['height'] = 178
print(a_dict)

people = [{'name': 'bob', 'age': 20, 'height': 178},
          {'name': 'Yon', 'age': 27, 'height': 158}]
person = {'name': 'Hyon', 'age': 27, 'height': 167}
people.append(person)
print(people)

print(people[2]['height'])


def f(x):
    return 2*x+3


y = f(3)
print(y)
'''
javascript의 함수형은
function f(x){
    이렇게 중괄호로 감싸주지만
}

python의 함수형은
def f(x):
    감싸주는 것 없이 : 콜론 뒤에 처리내용이 들어가기때문에
    indentation을 신경써줘야 한다. (탭 1칸 = 스페이스 4칸 표준)
'''


def sum_all(a, b, c):
    return a+b+c


def mul(a, b):
    return a*b


result = sum_all(1, 2, 3) + mul(10, 10)
print(result)


def oddeven(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(oddeven(20))


def is_adult(age):
    if age > 20:
        print('성인입니다')
    else:
        print('청소년이에요')


is_adult(30)

# 파이썬에서의 반복문은, 리스트의 요소들을 하나씩 꺼내쓰는 형태입니다.

fruits = ['사과', '수박', '배', '감', '딸기', '귤', '수박']

count = 0
for fruit in fruits:
    if fruit == '수박':
        count = count+1
print(count)
