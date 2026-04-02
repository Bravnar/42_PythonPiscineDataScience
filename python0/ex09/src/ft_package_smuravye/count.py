def count_in_list(iterable: any, to_count: any) -> int:
    """
    Counts the given to_count parameter within
    the list and return the count int

    Args:
        iterable: list[any] the iterable to count in
        to_count: any, what to count
    Return:
        count of to_cout in l
    """
    count = 0
    for i in iterable:
        if i == to_count:
            count += 1
    return count


if __name__ == "__main__":
    print(count_in_list(["toto", "tata", "toto"], "toto"))
    print(count_in_list(["toto", "tata", "toto"], "tutu"))
