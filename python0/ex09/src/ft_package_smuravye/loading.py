import time
import sys
from tqdm import tqdm


def ft_tqdm(lst: range):
    """
    Function that wraps a range and yields a progress bar
    Works similarly to tqdm but with less bizzaze

    Args:
        lst (range): An iterable object
        to be wrapped by the progress bar

    Yields:
        any: The items from the orginal iterable 'lst'
    """
    total = len(lst)
    line_size = 50
    for i, item in enumerate(lst):
        progress = i + 1
        percent = (progress / total) * 100
        filled_length = int(line_size * progress // total)
        bar = "=" * (filled_length - 1) + ">" if filled_length > 0 else ""
        space = " " * (line_size - len(bar))
        out = f"\rProgress: |{bar}{space}| {percent:.1f}% [{progress}/{total}]"

        sys.stdout.write(out)
        sys.stdout.flush()

        yield item


def main() -> None:
    """
    Main entry function that compares ft_tqdm
    with tqdm

    Args:
        None

    Returns:
        None
    """
    for elem in ft_tqdm(range(333)):
        time.sleep(0.005)
    print()
    for elem in tqdm(range(333)):
        time.sleep(0.005)
    print()


if __name__ == "__main__":
    main()
