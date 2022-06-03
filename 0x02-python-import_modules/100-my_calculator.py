#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = ["+", "-", "*", "/"]
    from calculator_1 import add, sub, mul, div
    funct = [add, sub, mul, div]
    for x, y in enumerate(op):
        if argv[2] == y:
            print("{} {} {} = {}".format(a, y, b, funct[x](a, b)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
