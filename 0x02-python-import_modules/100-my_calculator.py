#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    op = ""
    a = 0
    b = 0
    result = 0

    if len(sys.argv) != 4:
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if op != "+" and op != "-" and op != "*" and op != "/":
        print("Unkown operator. Available operators: +, -, * and /")
        exit(1)
    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    else:
        result = div(a, b)
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, result))
