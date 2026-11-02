import math
import sys

def GetRoots(a, b, c):
    D = b * b - 4 * a * c
    if D < 0:
        return []
    else:
        roots = []
        sqD = math.sqrt(D)
        for i in (- b - sqD, - b + sqD):
            if ((i / (2 * a)) >= 0):
                roots.append(math.sqrt(i / (2 * a)))
                roots.append(- math.sqrt(i / (2 * a)))
        return roots


def main():
    try:
        a, b, c = map(int, sys.argv[1:4])
    except:
        while True:
            try:
                a, b, c = map(float, input("Введите коэффециенты: ").split())
                if a == 0:
                    print("При a = 0 это уравнение не биквадратное")
                    continue
                break
            except ValueError:
                print("Должны быть введены 3 числа")
    roots = GetRoots(a, b, c)
    if len(roots) == 0: print("Корней нет")
    else:
        for root in set(roots):
            print(round(root, 3), end = ' ')
    print()

if (__name__ == "__main__"):
    main()
