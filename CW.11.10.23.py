#Задание 1

def repeat_string(n, s):
    return s * n

#Задание 2

def converttoinitials(name):
    names = name.split(" ")
    initials = name[0.upper() for name in names]
    return ". ".join(initials)
  
#Задание 2

def abbrev_name(name):
    name = name.upper().split()
    return name[0][0] + "." + name[1][0]

#Задание 3

def reverse_list(l):
  return [r for r in reversed(l)]

#Задание 4

def sum_str(a, b):
    if a == '': a = '0'
    if b == '': b = '0'
    return str(int(a) + int(b))

#Задание 5

def count_sheep(n):
    if n == 1:
        return "1 sheep..."
    else:
        return count_sheep(n - 1) + "{} sheep...".format(n)

  #Задание 6

def shortcut(s):
    for i in ["a","e","i","o","u"]:
        if i in s:
            s = s.replace(i,"")

    return(s)

#Задание 7

def opposite(number):
    return -number

#Задание 8

def sum_mix(arr):
    return sum(list(map(int,arr)))

#Задание 9

def say_hello(name):
    return"Hello, " +name

#Задание 10

def remove(s):
    return s.removesuffix('!')
