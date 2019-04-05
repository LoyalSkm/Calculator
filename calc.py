print('''
           Это не самый лучший калькулятор, 
         но если вам не повезло то ладно уж...
         он может только +  - Сумирывать
                         -  - Вычитать
                         /  - Делить
                         // - Возвращать не полное частное от деления
                         *  - Умножать
                         ** - Возводить в степень
                         %  - Делить по модул
                         cos - Синус
                         sin - Косинус
                         tan - Тангенс
                         ctg - Котангенс
                                                                 ''')
import sys, math

def zapros_val(mes):
    while True:
        try:
            val = float(input(mes))
            return val
        except ValueError:
            print("Вы не ввели число, попробуйте снова")

def zapros_op():
    mes = ""
    op  = ("+", "-", "/", "//", "*", "**", "%", "sin", "cos")
    while mes not in op:
        o = input("Укажите операцию: ")
        oper = o.strip()  # удаляем пробелы
        if oper in op:
            return oper
        else:
            print("Вы ввели не сущиствующий оператор, повторите")

def result():
    for i in oper:
        if oper == "sin":
            res1 = str(math.sin(int(first)))
            print("{} {} = {}".format(oper, first, res1))
            sys.exit()
        elif oper == "cos":
            res1 = str(math.cos(int(first)))
            print ("{} {} = {}".format(oper, first, res1))
            sys.exit()
        if oper == "//":
            res = first // second
        elif oper == "**":
            res = first ** second
        elif oper == "+":
            res = first + second
        elif oper == "-":
            res = first - second
        elif oper == "%":
            res = first % second
        elif oper == "/":
            if second == 0:
                res = "ZeroDivisionError"
            else:
                res = first / second
        elif oper == "*":
            res = first * second
        print("{} {} {} = {}".format(first, oper, second, res))

first = zapros_val("Введите первое число: ")
oper = zapros_op()
# if oper == "sin":
#     res1 = str(math.sin(int(first)))
#     print("{} {} = {}".format(oper, first, res1))
#     sys.exit()
# elif oper == "cos":
#     res1 = str(math.cos(int(first)))
#     print("{} {} = {}".format(oper, first, res1))
#     sys.exit()
second = (zapros_val("Введите второе число: "))
res = result()