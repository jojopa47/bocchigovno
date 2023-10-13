#Задание 1

def solution(string):
    return string[::-1]

#Задание 2

def make_upper_case(strng):
    return strng.upper()

#Задание 3

def remove_char(s):
    return s[1:-1]

#Задание 4

def areYouPlayingBanjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return name + ' plays banjo'
    return name + ' does not play banjo'

#Задание 5

def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"
