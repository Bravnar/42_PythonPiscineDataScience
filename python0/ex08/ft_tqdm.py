from os import get_terminal_size
import time


def update(progress_bar, iters):
    intervals = progress_bar["intervals"]
    t_size = progress_bar["terminal_size"]
    bodies = int((iters + 1) / intervals * t_size)
    ret = progress_bar["ends"]
    ret += progress_bar["body"] * bodies
    ret += progress_bar["pointer"]
    ret += " " * (progress_bar["terminal_size"] - bodies + 1)
    ret += progress_bar["ends"]
    return ret


def ft_tqdm(lst: range) -> None:
    terminal_size = get_terminal_size().columns - 100
    intervals = len(lst)
    progress_bar = {
        "terminal_size": terminal_size,
        "ends": "|",
        "body": "=",
        "pointer": ">",
        "bucket": terminal_size // intervals,
        "progress": 0,
        "intervals": intervals,
    }
    for iters in lst:
        progress_bar["progress"] = (iters + 1) * 100 / progress_bar["intervals"]
        bar = f"Loading: {iters + 1} / {progress_bar['intervals']} "
        bar += f"{update(progress_bar, iters)}"
        bar += f"{progress_bar['progress']}% Done"
        print(bar, end="\r")
        time.sleep(0.1)


if __name__ == "__main__":
    ft_tqdm(range(100))
    # print(tqdm().__doc__)
