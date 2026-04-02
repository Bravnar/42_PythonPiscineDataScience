from ft_package_smuravye.ft_tqdm import ft_tqdm
import time as rolex

if __name__ == "__main__":
    for elem in ft_tqdm(range(333)):
        rolex.sleep(0.005)
