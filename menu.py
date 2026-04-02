import os
import sys
import subprocess


def draw_header():
    header = """
/* ************************************************************************* */
/*                                                                           */
/*                                                       :::      ::::::::   */
/*  pythonPiscine                                      :+:      :+:    :+:   */
/*                                                   +:+ +:+         +:+     */
/*  By: smuravye <smuravye@student.42.fr>          +#+  +:+       +#+        */
/*                                               +#+#+#+#+#+   +#+           */
/*  Created by smuravye                               #+#    #+#             */
/*  Maintained by smuravye                           ###   ########.ch       */
/*                                                                           */
/* ************************************************************************* */
"""
    print(header)


def list_dir(cwd, sel="day"):
    starts = "python" if sel == "day" else "ex"
    display_list = []
    list_dir = [x for x in os.listdir(cwd) if x.startswith(starts)]
    for i, item in enumerate(list_dir):
        if len(os.listdir(os.path.abspath(item))) == 0:
            print(f"{i}.\t{item} -> WIP")
            display_list.append(item)
        else:
            print(f"{i}.\t{item}")
            display_list.append(item)

    return display_list


def select(ldays, sel="day"):
    print()
    prompt = f"Please select {sel}:\n>>>\t"
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            prompt = f"Please select a valid {sel}:\n>>>\t"
            continue
        except KeyboardInterrupt:
            print("\n\nSelection cancelled by user, exiting...")
            exit(0)
        if user_input > len(ldays) - 1:
            prompt = f"Enter {sel} within range 0..{len(ldays) - 1}:\n>>>\t"
            continue
        break
    ret_dir = ldays[user_input].split("\t")[-1]
    return os.path.abspath(ret_dir)


def run_exercise(selection):
    os.chdir(selection)
    cwd = os.getcwd()
    files = [x for x in os.listdir(cwd) if x.endswith(".py")]
    files.sort()
    if not files:
        print(f"No python files found in {selection}")
        return
    for i, item in enumerate(files):
        print(f"{i}. {item}")
    exo = select(files, "file to run")
    try:
        print(f"\n--- Executing: {exo} ---\n")
        subprocess.run([sys.executable, exo])
    except Exception as e:
        raise Exception(f"{type(e).__name__}: {e}") from None


def main() -> None:
    try:
        cwd = os.getcwd()
        if cwd == "/home/bravnar/Documents/Python/py_42/PythonPiscine42":
            os.chdir("/home/bravnar/Documents/Python/py_42/PythonPiscine42")
            cwd = os.getcwd()
        draw_header()
        ldays = list_dir(cwd)
        selection = select(ldays)
        os.chdir(selection)
        cwd = os.getcwd()
        lexo = list_dir(cwd, "exercise")
        selection = select(lexo, "exercise")
        run_exercise(selection)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
