#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if str(argv[2]) not in ["+", "-", "*", "/"]:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(argv[1])
            b = int(argv[3])
            op = argv[2]
        
            if op == "+":
                print("{:d} + {:d} = {:d}".format(a, b, calc.add(a, b)))
            elif op == "-":
                print("{:d} - {:d} = {:d}".format(a, b, calc.sub(a, b)))
            elif op == "*":
                print("{:d} * {:d} = {:d}".format(a, b, calc.mul(a, b)))
            else:
                print("{:d} / {:d} = {:d}".format(a, b, calc.div(a, b)))
