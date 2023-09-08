import math


def main():
    n = int(input("Enter number :"))
    sinVal = math.sin(n)
    print(f'sine value : {sinVal}\n')
    if n >=0:
        sqrtVal = math.sqrt(n)
        print(f'Square root value : {sqrtVal} \n')
    else:
        print('undefined for negative values\n')
    if n>0:
        logVal = math.log(n)
        print(f'log Value : {logVal}')
    else:
        print('undefined for negative values or zero\n')

main()