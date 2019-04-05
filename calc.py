print('''
           Это не самый лучший калькулятор, 
         но если вам не повезло то ладно уж...
         он может только +  - Сумирывать
                         -  - Вычитать
                         /  - Делить
                         // - Возвращать не полное частное от деления
                         *  - Умножать
                         ** - Возводить в степень
                         √  - Находить корень квадратный
                         %  - Делить по модул
                         sin - Находить синус
                         cos - Находить косинус
                                                                  ''')
import sys, math
#тут я принимаю число пользователя, проверяю его на float
def zapros_val(mes):
    while True:
        try:
            val = float(input(mes))
            return val
        except ValueError:
            print("Вы не ввели число, попробуйте снова")
#тут запрашиваю оператор и проверяю может ли мой калькулятор работать с получеными оператором
def zapros_op():
    empty_list = ""
    list  = ["+", "-", "/", "//", "*", "**", "√", "%", "sin", "cos"]
    while empty_list not in list:
        o = input("Укажите операцию: ")
        op = o.strip()  # удаляем пробелы
        if op in list:
            return op
        else:
            print("Вы ввели не сущиствующий оператор, повторите")
    print(len(list))
#Функция обрабатывающая полученные значения
def result(a, b):
    if oper == "sin":
        res1 = str(math.sin(int(a)))
        print("{} {} = {}".format(oper, a, res1))
        sys.exit()
    elif oper == "cos":
        res1 = str(math.cos(int(a)))
        print ("{} {} = {}".format(oper, a, res1))
        sys.exit()
    elif oper == "√":
        res1 = str(math.sqrt(int(a)))
        print ("{} {} = {}".format(oper, a, res1))
        sys.exit()
    elif oper == "//":
        res = a // b
    elif oper == "**":
        res = a ** b
    elif oper == "+":
        res = a + b
    elif oper == "-":
        res = a - b
    elif oper == "%":
        res = a % b
    elif oper == "/":
        if second == 0:
            res = "ZeroDivisionError"
        else:
            res = a / b
    elif oper == "*":
        res = first * second
    print("{} {} {} = {}".format(a, oper, b, res))



first = zapros_val("Введите первое число: ")
oper = zapros_op()
if oper == "sin" or oper == "cos" or oper == "√":
    res = result(first, 0)
else:
    second = (zapros_val("Введите второе число: "))
    res = result(first, second)