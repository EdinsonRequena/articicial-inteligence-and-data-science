
def is_palindrome(arg: str) -> bool:
    """Returns true if is a palindrome, Returns false is not a palindrome"""
    arg = arg.replace(' ', '').lower()
    return arg == arg[::-1]


def main():
    """Main function"""
    print(is_palindrome("Ana"))


if __name__ == '__main__':

    main()
