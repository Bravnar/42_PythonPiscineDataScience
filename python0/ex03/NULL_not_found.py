def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: None {type(object)}")
    elif isinstance(object, float):
        print(f"Cheese: nan {type(object)}")
    elif isinstance(object, int) and not isinstance(object, bool):
        print(f"Zero: 0 {type(object)}")
    elif isinstance(object, str) and len(object) == 0:
        print(f"Empty: {type(object)}")
    elif isinstance(object, bool):
        print(f"Fake: False {type(object)}")
    else:
        print("Type not found")

    return 1
