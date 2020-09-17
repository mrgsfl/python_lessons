x1 = float(input())
x2 = float(input())
action = input()
if action == "+":
    print(x1 + x2)
elif action == "*":
    print(x1 * x2)
elif action == "-":
    print(x1 - x2)
elif action == "pow":
    print(x1 ** x2)
elif action in ("/", "mod", 'div') and x2 == 0:
    print("Деление на 0!")
elif action == "/":
    print(x1 / x2)
elif action == "mod":
    print(x1 % x2)
elif action == "div":
    print(x1 // x2)
