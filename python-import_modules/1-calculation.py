#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    result_add = "{} + {} = {}".format(a, b, add(a, b))
    result_sub = "{} - {} = {}".format(a, b, sub(a, b))
    result_mul = "{} * {} = {}".format(a, b, mul(a, b))
    result_div = "{} / {} = {}".format(a, b, div(a, b))
    print(result_add, result_sub, result_mul, result_div, sep="\n")
