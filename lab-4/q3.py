import os


def main():
    env_var = os.environ
    for i in env_var.items():
        print(f'{i}')


main()
