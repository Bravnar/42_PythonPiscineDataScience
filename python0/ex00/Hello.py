if __name__ == "__main__":
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    ft_list[-1] = "World!"
    ft_tuple = ("Hello", "Switzerland!")
    ft_set.clear()
    ft_set.add("Hello")
    ft_set.add("Lausanne!")
    ft_dict["Hello"] = "42Lausanne!"

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)
