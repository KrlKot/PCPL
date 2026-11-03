import json
import sys
from unique import Unique
from field import field
from gen_random import gen_random
from cm_timer import cm_timer_1
from print_result import print_result

path = '/home/krlkot/PCPL_course/Lab2_PnC/data_light.json'

with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True), key=str.lower)


@print_result
def f2(arg):
    return list(filter(lambda s: s.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda s: s+' с опытом Python', arg))


@print_result
def f4(arg):
    salaries = gen_random(len(arg), 100000, 200000)
    return list(f'{job} - {sal} руб\n' for job, sal in zip(arg, salaries))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
