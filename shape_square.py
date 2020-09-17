shape = input()
if shape == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = float((a + b + c) / 2)
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)
elif shape == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)
elif shape == 'круг':
    r = int(input())
    print(3.14 * r * r)
