#Дистант 1

def multiply(a, b):
return a * b

#Дистант 2

def positive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum

#Дистант 3

def convert_to_negative(number):
    if number >= 1:
        return -number
    else:
        return number
#Дистант 4

def reverse_string(string):
    return string[::-1]

#Дистант 5

def even_or_odd(number):
  if number == 0:
    return "Even"
  elif number % 2 == 0:
    return "Even"
  else:
    return "Odd"
