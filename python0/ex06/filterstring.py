import sys
from string import punctuation
from ft_filter import ft_filter


def get_args() -> tuple[str, int]:
    """
    Gets the system arguments.
    Raises AssertionError if not str and int
    Raises AssertionError if punctuation present in string

    Args:
        None

    Return:
        The string and integer args (tuple[str, int])
    """
    args = sys.argv
    if len(args) != 3:
        raise AssertionError("the number of arguments should be 2")
    for i in args[1]:
        if i in punctuation:
            raise AssertionError("the string cannot contain any punctuation")
    try:
        ret_string = args[1]
        ret_num = int(args[2])
        return ret_string, ret_num
    except ValueError:
        raise AssertionError("the second argument must be a number.") from None


def filterstring(S: str, N: int):
    """
    Functions runs ft_filter with a lambda
    To check if each word is bigger than N

    Args:
        S: string to be filtered
        N: integer representing the checked length

    Return:
        List of filtered items from the string (list[str])
    """
    return ft_filter(lambda x: len(x) > N, S.split())


def main() -> None:
    """
    Main function that gets system arguments
    and runs filterstring

    Args:
        None

    Return:
        None
    """
    try:
        s, n = get_args()
        print("My ft_filter(): ")
        print(filterstring(s, n))
        print()
        print("Real filter(): ")
        print(list(filter(lambda x: len(x) > n, s.split())))
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
