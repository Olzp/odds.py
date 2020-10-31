from datetime import datetime
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21,23, 25, 27, 29, 31, 33, 35, 37,
        39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]
right_this_minute = datetime.today().minute
if right_this_minute in odds:
    print("This minute seems a little odd")
else:
    print("Not an odd minute")

#ex 1
a = 8
b = 2
print("Переменные a и b:", a,",", b)

number1 = int(input("Введите любое число:"))
number2 = int(input("Введите еще одно число:"))
string1 = input("Введите слово:")
string2 = input("Введите еще одно слово:")
print(number1, number2, string1, string2)

name = input("Введите ваше имя:")
print("Здраствуйте, ", name)

#ex2
ask_time = int(input("Введите время в секундах:"))
hours = ask_time // 3600
minutes = (ask_time - hours * 3600) // 60
seconds = ask_time - (hours * 3600 + minutes * 60)
print("Время в формате чч:мм:сс ",  hours, ":", minutes, ":", seconds)

#ex3
ask_number = int(input("Введите положительное число:"))
x = (ask_number +  int(str(ask_number) + str(ask_number)) + int(str(ask_number) + str(ask_number) + str(ask_number)) )
print(x)

#ex 4
numbr = int(input("Введите целое положительное число: "))


#ex5


