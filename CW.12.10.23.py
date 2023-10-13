#Задание 1

def is_even(n):
    return not n % 2

#Задание 2

def remove_exclamation_marks(s):
    x = s.replace("!","")
    return x

#Задание 3

def number_to_string(num):
    return str(num)

#Задание 4

def square(n):
    return n ** 2

#Задание 5

def paperwork(n, m):
    if m<0 or n<0:
        return 0
    else:
        return n*m

#Задание 6

def main(verb, noun): 
    return verb + noun

#Задание 7

def add_five(num):
    return num + 5

#Задание 8

def unusual_five():
    return(len('zzzzz'))

#Задание 9

def bin_to_decimal(inp):
    return int(inp, 2)

#Задание 10

def switch_it_up(number):
    number_converter={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
    return number_converter[number]
