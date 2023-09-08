import datetime


def get_greeting():
    curr = datetime.datetime.now()
    hour = curr.hour

    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 20:
        return "Good evening"
    else:
        return "Good night"


def main():
    username = input("Enter your username: ")
    greeting = get_greeting()
    print(f"{greeting}, {username}!")


main()
