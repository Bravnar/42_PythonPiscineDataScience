import sys


def get_morse(text: str) -> str:
    """
    Function that converts given text into morse code
    If character not in the morse dictionary raise
    an AssertionError

    Args:
        text (str)

    Returns:
        Morse string (str)
    """
    morse = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        " ": "/",
    }
    ret = []
    for letter in text:
        morse_char = morse.get(letter.upper())
        if not morse_char:
            raise AssertionError(f"character '{letter}' not in morse.")
        ret.append(morse_char)
    return " ".join(ret)


def get_arg() -> str:
    """
    Gets the string argument from system arguments
    Raises AssertionError if not correct argument length
    or if invalid characters are found in the string

    Args:
        None

    Return:
        argv[1] (str)
    """
    args = sys.argv
    if len(args) != 2:
        raise AssertionError("bad arguments.")
    ok_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
    if not all(x.upper() in ok_chars for x in args[1]):
        raise AssertionError("invalid characters in string.")
    return args[1]


def main() -> None:
    """
    Main function that tries to run get_morse
    and prints Error text in case of any raised errors

    Args:
        None

    Return:
        None
    """
    try:
        print(get_morse(get_arg()))
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
