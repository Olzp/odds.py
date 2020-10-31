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
#numbr = abs(input("Введите целое положительное число: "))




#ex5
profit = float(input("Введите сумму дохода фирмы:"))
costs = float(input("Введите издержки фирмы:"))
if profit > costs:
    print("Фирма работает в прибыль")
    workers = int(input("Введите численность сотрудников фирмы:"))
    print("Прибыль фирмы в расчете на одного сотрудника составляет:", {profit / workers})
else:
    print("Фирма работает в убыток")

#ex6
a = float(input("Введите результат после первого дня пробежки в километрах:"))
b = float(input("Введите желаемый результат в километрах:"))
days = 1
km_result = a
while km_result < b:
    a = a + a * 0.1
    days += 1
    km_result += a
print("Спортсмен достигнет желаемого результата в", b, " км на", days)



