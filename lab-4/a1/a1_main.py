import l4a1 as rev


def checkPalindrome(s):
    reStr = rev.reverseString(s)
    if s == reStr:
        print("palindrome")
    else:
        print("Not palindrome!")


def main():
    s = input("Enter string:")
    checkPalindrome(s)


main()
