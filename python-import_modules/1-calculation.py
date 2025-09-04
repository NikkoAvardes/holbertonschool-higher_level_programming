#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
	a = 10
	b = 5
	c = "{} + {} = {}".format(a, b, add(a, b))
	k = "{} - {} = {}".format(a, b, sub(a, b))
	l = "{} * {} = {}".format(a, b, mul(a, b))
	p = "{} / {} = {}".format(a, b, div(a, b))
	print(c,k,l,p, sep="\n")