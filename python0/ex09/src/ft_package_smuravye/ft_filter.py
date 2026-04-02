def ft_filter(function, iterable):
    """
    Takes an iterable and returns
    a list of where function is true

    Args:
        function(item)
        iterable: list[any]

    Return:
        Filtered list (list[any]) | None
    """
    if iterable is None or function is None:
        return None
    return [x for x in iterable.split() if function(x)]


if __name__ == "__main__":
    print(filter.__doc__)
