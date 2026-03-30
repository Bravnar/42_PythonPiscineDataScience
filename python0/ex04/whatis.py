import sys


def get_arg() -> int:
    if len(sys.argv) == 1:
        sys.exit(0)
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided.")
    try:
        return int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer.") from None


def whatis(x: int) -> None:
    print("I'm Odd.") if x % 2 else print("I'm Even.")


def main() -> None:
    try:
        whatis(get_arg())
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
