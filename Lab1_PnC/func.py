import math
import sys


def GetRoots(a, b, c):
    D = b * b - 4 * a * c
    roots_t = lambda a, b, D:( [] if D < 0 else
                                [- b / (2 * a)] if D == 0 else
                                [(- b - math.sqrt(D)) / (2 * a), (- b + math.sqrt(D)) / (2 * a)])

    roots_x = map(lambda t:([] if t < 0 else
                          [0] if t == 0 else
                          [math.sqrt(t), -math.sqrt(t)]),roots_t(a, b, D))
    flat_roots = lambda lists: sum(lists, [])
    return set(flat_roots(roots_x))


def PrintRoots(roots):
    print("Корней нет" if len(roots) == 0 else
                        " ".join(f"{round(root, 3)}" for root in roots))

def main():
    try:
        a, b, c = map(int, sys.argv[1:4])
        if a == 0:
            raise ValueError()
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
    PrintRoots(roots)


if (__name__ == "__main__"):
    main()
