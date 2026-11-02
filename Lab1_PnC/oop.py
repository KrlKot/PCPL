import math
import sys


class BiQuadratic:
    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("При a = 0 это уравнение не биквадратное")
        self.a = a
        self.b = b
        self.c = c
        self.roots = []


    def GetRoots(self):
        self.roots = []
        a, b, c = self.a, self.b, self.c
        D = b * b - 4 * a * c
        if D < 0:
            pass
        else:
            sqD = math.sqrt(D)
            for i in (- b - sqD, - b + sqD):
                if ((i / (2 * a)) >= 0):
                    self.roots.append(math.sqrt(i / (2 * a)))
                    self.roots.append(- math.sqrt(i / (2 * a)))


    def PrintRoots(self):
        if len(self.roots) == 0:
            print("Корней нет")
        else:
            for root in set(self.roots):
                print(round(root, 3), end = ' ')
        print()


def main():
    try:
        equation = BiQuadratic(*map(float, sys.argv[1:4]))
    except (ValueError, TypeError) as e:
        print(e)
        while True:
            try:
                equation = BiQuadratic(*map(float, input("Введите коэффециенты: ").split()))
                break
            except (ValueError, TypeError) as e:
                print(e)
    equation.GetRoots()
    equation.PrintRoots()


if (__name__ == "__main__"):
    main()
