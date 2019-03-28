print('''
           Это не самый лучший калькулятор, 
         но если вам не повезло то ладно уж...
         он может только +  - Сумирывать
                         -  - Вычитать
                         /  - Делить
                         // - Возвращать не полное частное от деления
                         *  - Умножать
                         ** - Возводить в степень
                         %  - Делить по модулю   
                                            ''')
while True:
    try:
        first = float(input("Укажите 1рвое число: "))
        break
    except ValueError:
        print("Вы не ввели число, попробуйте снова")

oper = ""
op = ("+", "-", "/", "//", "*", "**", "%")
while oper not in op:
    o = input("Укажите операцию: ")
    oper = o.strip()
    if oper in op:
        break
    else:
        print("Вы ввели не сущиствующий оператор, повторите")

while True:
    try:
        second = float(input("Укажите 2рое читсло: "))
        break
    except ValueError:
        print("Вы не ввели число, попробуйте снова")

for i in oper:
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