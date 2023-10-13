#Задание 1

def make_negative(number):
    if number >= 0:
        return (0 - number)
    else:
        return number

#Задание 2

def include(arr,item):
    for i in arr:
        if i == item:
            return True
    return False

#Задание 3

def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    return number*9

#Задание 4

websites = 1000 * ["codewars"]

#Задание 5

def between(a,b):
    arr = []
    for i in range(a, b + 1):
        arr.append(i)
    return arr

#Задание 6

def double_char(s):
    res = ''
    for i in s:
        res += i*2
    return res

#Задание 7

def maps(a):
    return [f*2 for f in a]

#Задание 8

def no_boring_zeros(n):
    if n == 0:
        return 0
    else:
        return int(str(n).strip('0'))

#Задание 9

def area_or_perimeter(l , w):
    if l == w:
        tot = l * w
    else:
        tot = l * 2 + w * 2
    return tot

#Задание 10

def greet():
    return "hello world!"
