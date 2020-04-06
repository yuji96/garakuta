from itertools import permutations
from operator import add, sub, mul, truediv


def calc_gen(raw_numbers):

    if len(raw_numbers) == 1:
        out = float(raw_numbers[0])
        if out.is_integer() and out > 0:
            yield int(out)
        return

    for pair in permutations(raw_numbers, r=2):

        tmp_numbers = [n for n in raw_numbers if n not in pair]
        for ope in [add, sub, mul, truediv]:
            try:
                yield from calc_gen(tmp_numbers + [ope(*pair)])
            except ZeroDivisionError:
                continue


def calc_func(raw_numbers):

    outs = []

    if len(raw_numbers) == 1:
        out = float(raw_numbers[0])
        if out.is_integer() and out > 0:
            return int(out)
        else:
            return

    for pair in permutations(raw_numbers, r=2):

        tmp_numbers = [n for n in raw_numbers if n not in pair]
        for ope in [add, sub, mul, truediv]:
            try:
                result = calc_func(tmp_numbers + [ope(*pair)])
            except ZeroDivisionError:
                continue
            if result:
                if isinstance(result, int):
                    outs.append(result)
                else:
                    outs.extend(result)

    return sorted(set(outs))


if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    print(sorted(set(calc_gen(numbers))))
    print(calc_func(numbers))
