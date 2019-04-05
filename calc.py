print('''
                    С помощю калькулятора можна:                                  
                                    
+ - Сумирывать                                  √ - Находить корень квадратный
- - Вычитать                                    % - Делить по модул
/ - Делить                                      sin - Находить синус
// - Возвращать не полное частное от деления    cos - Находить косинус
* - Умножать                                    tan - Находить Тангенс
** - Возводить в степень
                                                                  ''')
import sys, math
# Тут я принимаю число пользователя, проверяю его на float
def zapros_val(mes):
    while True:
        try:
            val = float(input(mes))
            return val
        except ValueError:
            print("Вы не ввели число, попробуйте снова")
            
# Тут запрашиваю оператор и проверяю может ли мой калькулятор работать с получеными оператором
def zapros_op():
    empty_list = ""
    list  = ["+", "-", "/", "//", "*", "**", "√", "%", "sin", "cos", "tan"]
    while empty_list not in list:
        o = input("Укажите операцию: ")
        op = o.strip()  # удаляем пробелы
        if op in list:
            return op
        else:
            print("Вы ввели не сущиствующий оператор, повторите")
    print(len(list))

# Функция обрабатывающая полученные значения
def result(pervoe_chislo, vtoroe_chislo):
    def print_result(a, oper, b, res):      # Функция которая выводит результат
        if oper == "sin" or oper == "cos" or oper == "tan" or oper == "√":
            fun ="{} {} = {}".format(oper, a, res)
            return fun
        else:
            fun = "{} {} {} = {}".format(a, oper, b, res)
            return fun

    if oper == "sin":
        res = math.sin(int(pervoe_chislo))
        print(print_result(pervoe_chislo, oper, 1, res))
        sys.exit()
    elif oper == "cos":
        res = math.cos(int(pervoe_chislo))
        print(print_result(pervoe_chislo, oper, 1, res))
        sys.exit()
    elif oper == "tan":
        res = math.tan(int(pervoe_chislo))
        print(print_result(pervoe_chislo, oper, 1, res))
        sys.exit()
    elif oper == "√":
        res = math.sqrt(int(pervoe_chislo))
        print(print_result(pervoe_chislo, oper, 1, res))
        sys.exit()
    elif oper == "//":
        res = pervoe_chislo // vtoroe_chislo
    elif oper == "**":
        res = pervoe_chislo ** vtoroe_chislo
    elif oper == "+":
        res = pervoe_chislo + vtoroe_chislo
    elif oper == "-":
        res = pervoe_chislo - vtoroe_chislo
    elif oper == "%":
        res = pervoe_chislo % vtoroe_chislo
    elif oper == "/":
        if second == 0:
            res = "нельзя делить на 0 *("
        else:
            res = pervoe_chislo / vtoroe_chislo
    elif oper == "*":
        res = first * second
    print(print_result(pervoe_chislo, oper, vtoroe_chislo, res))



first = zapros_val("Введите первое число: ")
oper = zapros_op()
if oper == "sin" or oper == "cos" or oper == "tan" or oper == "√":
    res = result(first, 0)
else:
    second = (zapros_val("Введите второе число: "))
    res = result(first, second)