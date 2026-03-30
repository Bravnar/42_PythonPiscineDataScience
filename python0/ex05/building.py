import sys


def get_arg() -> str:
    """
    Fetches the args given in the command line.

    Args: None

    Returns:
        the 1st positional argument,
        raises AssertionError if more than 2 (incl .py)
        requests a user input if no arguments are given
    """
    if len(sys.argv) == 1:
        return input("Enter a string:\n")
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided.")
    return sys.argv[1]


def building(text: str) -> None:
    """
    Counts all the symbols in the text independently,
    prints the output by type of char

    Args:
        text (str): the string to count the characters of

    Returns:
        None
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    whitespace = " \t\n\r\v\f"
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    count_upper = len([x for x in text if x in alphabet.upper()])
    count_lower = len([x for x in text if x in alphabet])
    count_punct = len([x for x in text if x in punctuation])
    count_space = len([x for x in text if x in whitespace])
    count_digit = len([x for x in text if x.isdigit()])
    print(f"The text contains {len(text)} characters:")
    print(f"{count_upper} upper letters")
    print(f"{count_lower} lower letters")
    print(f"{count_punct} punctuation marks")
    print(f"{count_space} spaces")
    print(f"{count_digit} digits")


def main() -> None:
    building(get_arg())


if __name__ == "__main__":
    main()
