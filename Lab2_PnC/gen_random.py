import random
def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randrange(begin, end+1)

for x in gen_random(5, 1, 3):
    print(x, end =' ')
print()
