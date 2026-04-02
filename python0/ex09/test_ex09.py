from ft_package_smuravye import ft_tqdm, get_morse, count_in_list
import time as rolex

if __name__ == "__main__":
    print("Testing imported ft_tqdm!")
    print()
    for elem in ft_tqdm(range(333)):
        rolex.sleep(0.005)
    print()
    print("\nTesting import morse translator")
    print(get_morse("sos"))
    print("\nTesting count_in_list as per the exo")
    print(count_in_list(["toto", "tata", "toto"], "toto"))
    print(count_in_list(["toto", "tata", "toto"], "tutu"))
