def fun1():
    print('access funtion 2 [y/n]')
    ch = input()
    if ch == 'y':
        fun2()
    elif ch == 'n':
        print('Exiting...')
        exit(0)
    else:
        print('Wrong Choice')
        exit(0)


def fun2():
    print('In function 2 ')


def main():
    fun1()


main()
