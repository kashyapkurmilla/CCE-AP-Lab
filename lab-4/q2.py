import cmath


def main():
    n = complex(input("Enter number :"))
    sinVal = cmath.sin(n)
    print(f'sine value : {sinVal}\n')
    sqrtVal = cmath.sqrt(n)
    print(f'Square root value : {sqrtVal} \n')
    logVal = cmath.log(n)
    print(f'log Value : {logVal}')

main()