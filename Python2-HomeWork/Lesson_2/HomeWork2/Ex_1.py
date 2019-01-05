
# Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся
# пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для
# вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь
# вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать
# знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.


def calc():
    a = float(input())
    b = float(input())
    sin = str(input())

    if sin != "0" and sin != "+" and sin != "-" and sin != "*" and sin != "/":
        print("Error, check your sin ")
        return calc()
    else:
        if sin == "0":
            return "Program has end."
        elif sin == "+":
            return a + b
        elif sin == "-":
            return a - b
        elif sin == "*":
            return a * b
        elif sin == '/' and b == 0:
            print("Error, check your sin")
            return calc()
        else:
            return a / b


print('Input two numbers and a sin ')
print(calc())
