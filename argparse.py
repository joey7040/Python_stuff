import argparse

def fib(n):
    a, b= 0,1 
    for i in range():
        a, b = b, a+b
        return a

def main():
    parser = argparse.ArgumentParser()
    paser.add_argument("num", help= "The fibonacci number you wish to calculate.", type =int)

    args = parser.parse_args()

    result = fib(args.num)
    print("The " + str(args.num) + "The fibonnaci number is " + str(result))

if __name__ == '__main__':
    main()

